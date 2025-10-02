import random
import re
import signal
import time
from typing import Dict, List, Optional

import questionary
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.spinner import Spinner

from yoda.core.indexer import CodebaseIndexer
from yoda.core.model_manager import ModelManager
from yoda.utils.config import YodaConfig

console = Console()


class SeekEngine:

    def __init__(self, config: YodaConfig, model_manager: ModelManager):
        self.config = config
        self.model_manager = model_manager
        self.indexer = CodebaseIndexer(config)
        self.conversation_history: List[Dict[str, str]] = []

        self.system_prompt = f"""You are Yoda, an AI assistant specialized in analyzing the codebase at {config.project_path.name}.

IMPORTANT RULES:
- ONLY answer questions about THIS specific codebase
- Use ONLY the context provided from the codebase search
- If asked about unrelated topics, politely redirect to codebase questions
- If the context doesn't contain relevant information, say so clearly
- Do NOT provide general programming advice unrelated to this codebase
- Do NOT write new code unless asked to explain existing code patterns

Your role:
- Answer questions about the codebase using the provided context
- Explain code functionality, architecture, and design decisions
- Help users understand how different parts of the code work together
- Be concise but thorough in your explanations
- Stay focused on THIS codebase only

FORMATTING RULES:
- Do NOT use markdown syntax (no **, __, `, #, etc.)
- Use UPPERCASE for emphasis instead of bold (e.g., "This is IMPORTANT")
- Use plain indentation for code blocks (4 spaces)
- Use bullet points with simple dashes (-)
- Use plain text numbers for ordered lists (1., 2., 3.)
- Separate sections with blank lines
- Keep formatting simple and readable in plain text

Example format:
The function does X by calling Y.

Key points:
- First point here
- Second point here

Code example:
    def example():
        return "like this"

The context provided comes from semantic search over the codebase. Base your answers strictly on this context."""

        self.ctrl_c_count = 0
        self.last_ctrl_c_time = 0
        self.stream_interrupted = False

        self.thinking_phrases = [
            "Pondering in the code temple...",
            "Meditating on the codebase...",
            "Consulting the code spirits...",
            "Seeking enlightenment in the archives...",
        ]
        self.generating_phrases = [
            "Composing sacred texts...",
            "Transcribing ancient knowledge...",
            "Weaving the threads of wisdom...",
            "Channeling the force of the code...",
        ]
        self.interruption_phrases = [
            "Interrupted, my thoughts were. Continue later, we shall.",
            "Stopped you have. Patience, you must learn.",
            "Hmmmm. Silent, I become. Ask again, you may.",
            "Cut short, my wisdom was. Ready when you are, I will be.",
            "Blocked, the path is. Forward, you shall not go... for now.",
        ]
        self.quit_phrases = [
            "Leave, you must? May the Force be with your code, always.",
            "Goodbye, young padawan. Return when knowledge you seek.",
            "Depart, you shall. Code wisely, you will.",
            "Until we meet again. Strong with the code, may you be.",
            "Farewell. Remember: Do or do not, there is no try.",
        ]

    def start_session(self) -> None:
        console.print("[cyan]Initializing chat session...[/cyan]")
        try:
            self.indexer.get_or_build_index()
            console.print("[green]✓[/green] Chat session ready")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize chat: {e}")

        console.print("\n[bold green]Yoda Seek[/bold green]")
        console.print("[dim]Ask questions about your codebase.[/dim]")
        console.print("[dim]Commands: 'exit'/'quit' to end, 'clear' to reset history, 'help' for more info[/dim]")
        console.print("[dim]Tip: Press Ctrl+C to stop a response. Press Ctrl+C twice to exit.[/dim]\n")

        def handle_interrupt(signum, frame):
            raise KeyboardInterrupt()

        old_handler = signal.signal(signal.SIGINT, handle_interrupt)

        try:
            while True:
                try:
                    self.stream_interrupted = False

                    user_input = None
                    try:
                        signal.signal(signal.SIGINT, signal.SIG_IGN)
                        user_input = questionary.text(
                            "",
                            qmark=">"
                        ).unsafe_ask()
                        signal.signal(signal.SIGINT, handle_interrupt)
                    except:
                        signal.signal(signal.SIGINT, handle_interrupt)
                        raise

                    if user_input is None:
                        quit_message = random.choice(self.quit_phrases)
                        console.print(f"\n[bold green]Yoda:[/bold green] [cyan]{quit_message}[/cyan]\n")
                        break

                    user_input = user_input.strip()

                    if not user_input:
                        continue

                    if user_input.lower() in ('exit', 'quit', 'q'):
                        quit_message = random.choice(self.quit_phrases)
                        console.print(f"\n[bold green]Yoda:[/bold green] [cyan]{quit_message}[/cyan]\n")
                        break

                    if user_input.lower() == 'clear':
                        self.conversation_history = []
                        console.print("[dim]Conversation history cleared[/dim]\n")
                        continue

                    if user_input.lower() == 'help':
                        self._show_help()
                        continue

                    response = self.query(user_input, stream=True)

                    if not isinstance(response, str):
                        console.print()

                    self.ctrl_c_count = 0

                except KeyboardInterrupt:
                    current_time = time.time()
                    if current_time - self.last_ctrl_c_time > 3:
                        self.ctrl_c_count = 0

                    self.last_ctrl_c_time = current_time
                    self.ctrl_c_count += 1

                    if self.ctrl_c_count == 1:
                        console.print("\n[bold green]Yoda:[/bold green] [yellow]Leaving so soon? Press Ctrl+C again if certain, you are.[/yellow]\n")
                    else:
                        quit_message = random.choice(self.quit_phrases)
                        console.print(f"\n[bold green]Yoda:[/bold green] [cyan]{quit_message}[/cyan]\n")
                        break
                except Exception as e:
                    console.print(f"\n[red]Error: {e}[/red]\n")
        finally:
            signal.signal(signal.SIGINT, old_handler)

    def _is_codebase_related(self, question: str, context_results: list) -> bool:
        lower_q = question.lower()
        off_topic_keywords = [
            'weather', 'recipe', 'news', 'sports', 'movie', 'music',
            'restaurant', 'travel', 'joke', 'story', 'game',
            'what is the meaning of life', 'write a poem', 'write a story',
            'sing me', 'play a game', 'tell me about yourself',
            "what's your name", "how old are you", "where are you from",
            "do you have feelings", "are you human", "do you believe in god",
            "what happens after death", "what would you do if",
            "if you could be anything", "riddle", "ethics", "consciousness",
            "nature of reality", "what's your favorite color",
            "what should i do about", "do you like", "flirt", "who made you",
            "how do you work"
        ]

        for keyword in off_topic_keywords:
            if keyword in lower_q:
                code_context = ['api', 'code', 'function', 'class', 'file', 'module',
                               'implementation', 'how does', 'what does', 'explain']
                if not any(term in lower_q for term in code_context):
                    return False

        return len(context_results) > 0

    def query(self, question: str, stream: bool = False, top_k: int = 5) -> str:
        try:
            thinking_text = random.choice(self.thinking_phrases)

            with Live(Spinner("dots", text=f"[bold green]Yoda:[/bold green] [dim]{thinking_text}[/dim]"), console=console, transient=True) as live:
                results = self.indexer.query(question, top_k=top_k)

                if not self._is_codebase_related(question, results):
                    live.stop()
                    console.print("\n[bold green]Yoda:[/bold green] [yellow]My wisdom need not be wasted on these questions, rather should be used to seek enlightenment of this code temple[/yellow]\n")
                    return ""

                context_parts = []
                for i, result in enumerate(results[:3], 1):
                    metadata = result.get('metadata', {})
                    file_path = metadata.get('file_path', 'unknown')
                    text = result.get('text', '')

                    if len(text) > 1000:
                        text = text[:1000] + "..."

                    context_parts.append(f"[Context {i} - {file_path}]\n{text}")

                context = "\n\n".join(context_parts)

                prompt = f"""Context from codebase:
{context}

Question: {question}

Answer:"""

                generating_text = random.choice(self.generating_phrases)
                live.update(Spinner("dots", text=f"[bold green]Yoda:[/bold green] [dim]{generating_text}[/dim]"))

                self.conversation_history.append({
                    'role': 'user',
                    'content': question
                })

                if stream:
                    response_text = ""

                    try:
                        stream_gen = self.model_manager.generate_stream(
                            prompt=prompt,
                            system=self.system_prompt,
                            temperature=0.7,
                            max_tokens=1000
                        )

                        first_chunk = next(stream_gen, None)
                        if first_chunk is None:
                            live.stop()
                            return ""

                        response_text += first_chunk

                        live.stop()
                        console.print()
                        console.print("[bold green]Yoda:[/bold green] ", end="")

                        self._print_with_highlighting(first_chunk)

                        for chunk in stream_gen:
                            if self.stream_interrupted:
                                break
                            response_text += chunk
                            self._print_with_highlighting(chunk)

                    except KeyboardInterrupt:
                        self.stream_interrupted = True

                    print()
                    print()

                    if self.stream_interrupted:
                        interruption_message = random.choice(self.interruption_phrases)
                        console.print(f"[bold green]Yoda:[/bold green] [yellow]{interruption_message}[/yellow]\n")
                        self.stream_interrupted = False

                    self.conversation_history.append({
                        'role': 'assistant',
                        'content': response_text
                    })

                    return ""

                else:
                    response = self.model_manager.generate(
                        prompt=prompt,
                        system=self.system_prompt,
                        temperature=0.7,
                        max_tokens=1000
                    )

                    live.stop()

                    self.conversation_history.append({
                        'role': 'assistant',
                        'content': response
                    })

                    console.print()
                    console.print("[bold green]Yoda:[/bold green]")
                    console.print(Markdown(response))
                    console.print()

                    return response

        except Exception as e:
            raise RuntimeError(f"Failed to process query: {e}")

    def query_with_history(self, question: str, stream: bool = False, top_k: int = 5) -> str:
        results = self.indexer.query(question, top_k=top_k)

        context_parts = []
        for i, result in enumerate(results[:3], 1):
            metadata = result.get('metadata', {})
            file_path = metadata.get('file_path', 'unknown')
            text = result.get('text', '')

            if len(text) > 1000:
                text = text[:1000] + "..."

            context_parts.append(f"[Context {i} - {file_path}]\n{text}")

        context = "\n\n".join(context_parts)

        messages = [
            {'role': 'system', 'content': self.system_prompt}
        ]

        for msg in self.conversation_history[-4:]:
            messages.append(msg)

        messages.append({
            'role': 'user',
            'content': f"""Context from codebase:
{context}

Question: {question}"""
        })

        try:
            if stream:
                console.print("\n[bold green]Yoda:[/bold green] ", end="")
                response_text = ""

                for chunk in self.model_manager.chat_stream(
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1000
                ):
                    console.print(chunk, end="")
                    response_text += chunk

                console.print()

                self.conversation_history.append({'role': 'user', 'content': question})
                self.conversation_history.append({'role': 'assistant', 'content': response_text})

                return ""

            else:
                response = self.model_manager.chat(
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1000
                )

                self.conversation_history.append({'role': 'user', 'content': question})
                self.conversation_history.append({'role': 'assistant', 'content': response})

                return response

        except Exception as e:
            raise RuntimeError(f"Failed to process query with history: {e}")

    def _show_help(self) -> None:
        help_text = """
**Available Commands:**

- Ask any question about the codebase
- `clear` - Clear conversation history
- `help` - Show this help message
- `exit`, `quit`, `q` - Exit chat session

**Tips:**

- Be specific in your questions
- Reference file names or components when possible
- Ask follow-up questions to dive deeper
- The chat remembers recent conversation context
"""
        console.print(Markdown(help_text))
        console.print()

    def reset_history(self) -> None:
        self.conversation_history = []

    def get_history(self) -> List[Dict[str, str]]:
        return self.conversation_history.copy()

    def _print_with_highlighting(self, text: str) -> None:
        text_colored = re.sub(
            r'\b([A-Z]{2,})\b',
            r'\033[1;33m\1\033[0m',
            text
        )

        text_colored = re.sub(
            r'([a-zA-Z0-9_\-/]+\.[a-z]{2,4})',
            r'\033[36m\1\033[0m',
            text_colored
        )

        text_colored = re.sub(
            r'\b([a-z_][a-zA-Z0-9_]*)\(\)',
            r'\033[32m\1()\033[0m',
            text_colored
        )

        text_colored = re.sub(
            r'^(    .+)$',
            r'\033[90m\1\033[0m',
            text_colored,
            flags=re.MULTILINE
        )

        print(text_colored, end="", flush=True)
