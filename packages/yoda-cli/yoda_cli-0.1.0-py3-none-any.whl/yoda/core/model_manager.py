import ollama
import platform
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional

from rich.console import Console

console = Console()


class ModelManager:
    def __init__(self, model_name: str = "codellama:7b"):
        self.model_name = model_name
        self.client = ollama.Client()

    @staticmethod
    def _check_ollama_installed() -> bool:
        try:
            result = subprocess.run(['which', 'ollama'], capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except Exception:
            return False

    @staticmethod
    def _install_ollama() -> bool:
        system = platform.system()
        try:
            if system == "Darwin":
                console.print("[cyan]Installing Ollama via Homebrew...[/cyan]")
                console.print("[dim]This may take a few minutes...[/dim]")

                brew_check = subprocess.run(['which', 'brew'], capture_output=True, timeout=5)
                if brew_check.returncode != 0:
                    console.print("[red]✗[/red] Homebrew not found. Installing Homebrew first...")
                    console.print("[yellow]Please install Homebrew from https://brew.sh[/yellow]")
                    return False

                result = subprocess.run(['brew', 'install', 'ollama'], capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    console.print("[green]✓[/green] Ollama installed successfully")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed to install Ollama: {result.stderr}")
                    return False

            elif system == "Linux":
                console.print("[cyan]Installing Ollama on Linux...[/cyan]")
                console.print("[dim]This may take a few minutes...[/dim]")

                result = subprocess.run(['curl', '-fsSL', 'https://ollama.com/install.sh'],
                                      capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    install_result = subprocess.run(['sh', '-c', result.stdout],
                                                   capture_output=True, text=True, timeout=300)
                    if install_result.returncode == 0:
                        console.print("[green]✓[/green] Ollama installed successfully")
                        return True
                    else:
                        console.print(f"[red]✗[/red] Failed to install Ollama: {install_result.stderr}")
                        return False
                else:
                    console.print(f"[red]✗[/red] Failed to download installer: {result.stderr}")
                    return False
            else:
                console.print(f"[yellow]Automatic installation not supported on {system}[/yellow]")
                console.print("[yellow]Please install Ollama manually from https://ollama.com[/yellow]")
                return False

        except subprocess.TimeoutExpired:
            console.print("[red]✗[/red] Installation timed out")
            return False
        except Exception as e:
            console.print(f"[red]✗[/red] Installation failed: {e}")
            return False

    def _start_ollama(self) -> bool:
        try:
            if self.test_connection():
                return True

            console.print("[cyan]Starting Ollama service...[/cyan]")

            subprocess.Popen(['ollama', 'serve'], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, start_new_session=True)

            for i in range(20):
                time.sleep(0.5)
                if self.test_connection():
                    console.print("[green]✓[/green] Ollama service started")
                    return True

            console.print("[red]✗[/red] Ollama service failed to start")
            return False
        except Exception as e:
            console.print(f"[red]✗[/red] Failed to start Ollama: {e}")
            return False

    @staticmethod
    def _ensure_ssh_key() -> bool:
        try:
            ollama_dir = Path.home() / '.ollama'
            key_path = ollama_dir / 'id_ed25519'

            if key_path.exists():
                console.print("[green]✓[/green] Ollama SSH key found")
                return True

            console.print("[cyan]Creating Ollama SSH key...[/cyan]")

            ollama_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

            result = subprocess.run(['ssh-keygen', '-t', 'ed25519', '-f', str(key_path),
                                   '-N', '', '-C', 'ollama@localhost'],
                                  capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                console.print(f"[yellow]Warning: ssh-keygen failed: {result.stderr}[/yellow]")
                return False

            key_path.chmod(0o600)
            pub_key = key_path.parent / (key_path.name + '.pub')
            if pub_key.exists():
                pub_key.chmod(0o644)

            console.print("[green]✓[/green] Ollama SSH key created")
            return True
        except FileNotFoundError:
            console.print("[yellow]⚠[/yellow] ssh-keygen not found - skipping SSH key generation")
            return False
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to create SSH key: {e}[/yellow]")
            return False

    def ensure_ollama_running(self) -> bool:
        if not self._check_ollama_installed():
            console.print("[yellow]⚠[/yellow] Ollama is not installed")
            console.print("[cyan]Yoda will now install Ollama automatically...[/cyan]")
            if not self._install_ollama():
                return False

        if not self._ensure_ssh_key():
            console.print("[yellow]⚠[/yellow] Failed to set up Ollama SSH key")

        if not self.test_connection():
            if not self._start_ollama():
                return False

        return True

    def ensure_model(self) -> bool:
        try:
            models_response = self.client.list()
            model_names = []

            if hasattr(models_response, 'models'):
                models_list = models_response.models
            elif isinstance(models_response, dict) and 'models' in models_response:
                models_list = models_response['models']
            else:
                models_list = models_response if isinstance(models_response, list) else []

            for m in models_list:
                if hasattr(m, 'model'):
                    model_names.append(m.model)
                elif hasattr(m, 'name'):
                    model_names.append(m.name)
                elif isinstance(m, dict):
                    name = m.get('name') or m.get('model') or m.get('id')
                    if name:
                        model_names.append(name)
                elif isinstance(m, str):
                    model_names.append(m)

            model_exists = any(self.model_name in name or name.startswith(self.model_name.split(':')[0])
                             for name in model_names)

            if model_exists:
                console.print(f"[green]✓[/green] Model {self.model_name} is available")
                return True

            console.print(f"[yellow]Model {self.model_name} not found. Downloading...[/yellow]")
            console.print("[dim]This may take a few minutes depending on your connection...[/dim]")

            try:
                result = subprocess.run(['ollama', 'pull', self.model_name],
                                      capture_output=False, text=True, timeout=600)
                if result.returncode == 0:
                    console.print(f"[green]✓[/green] Model {self.model_name} downloaded successfully")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed to download model")
                    return False
            except subprocess.TimeoutExpired:
                console.print(f"[red]✗[/red] Model download timed out")
                return False
            except Exception as pull_error:
                console.print(f"[red]✗[/red] Failed to pull model: {pull_error}")
                if model_names:
                    console.print(f"[yellow]Available models:[/yellow]")
                    for model in model_names:
                        console.print(f"  - {model}")
                return False
        except Exception as e:
            console.print(f"[red]✗[/red] Error checking model: {e}")
            console.print(f"[yellow]Attempting to pull model anyway...[/yellow]")
            try:
                result = subprocess.run(['ollama', 'pull', self.model_name],
                                      capture_output=False, text=True, timeout=600)
                return result.returncode == 0
            except Exception:
                return False

    def generate(self, prompt: str, system: Optional[str] = None,
                temperature: float = 0.7, max_tokens: Optional[int] = None) -> str:
        try:
            options = {'temperature': temperature}
            if max_tokens:
                options['num_predict'] = max_tokens

            messages = []
            if system:
                messages.append({'role': 'system', 'content': system})
            messages.append({'role': 'user', 'content': prompt})

            response = self.client.chat(model=self.model_name, messages=messages, options=options)
            return response['message']['content']
        except Exception as e:
            raise RuntimeError(f"Failed to generate text: {e}")

    def generate_stream(self, prompt: str, system: Optional[str] = None,
                       temperature: float = 0.7, max_tokens: Optional[int] = None) -> Generator[str, None, None]:
        try:
            options = {'temperature': temperature}
            if max_tokens:
                options['num_predict'] = max_tokens

            messages = []
            if system:
                messages.append({'role': 'system', 'content': system})
            messages.append({'role': 'user', 'content': prompt})

            stream = self.client.chat(model=self.model_name, messages=messages,
                                     options=options, stream=True)

            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']
        except Exception as e:
            raise RuntimeError(f"Failed to generate text: {e}")

    def chat(self, messages: List[Dict[str, str]], temperature: float = 0.7,
            max_tokens: Optional[int] = None) -> str:
        try:
            options = {'temperature': temperature}
            if max_tokens:
                options['num_predict'] = max_tokens

            response = self.client.chat(model=self.model_name, messages=messages, options=options)
            return response['message']['content']
        except Exception as e:
            raise RuntimeError(f"Failed to chat: {e}")

    def chat_stream(self, messages: List[Dict[str, str]], temperature: float = 0.7,
                   max_tokens: Optional[int] = None) -> Generator[str, None, None]:
        try:
            options = {'temperature': temperature}
            if max_tokens:
                options['num_predict'] = max_tokens

            stream = self.client.chat(model=self.model_name, messages=messages,
                                     options=options, stream=True)

            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']
        except Exception as e:
            raise RuntimeError(f"Failed to chat: {e}")

    def is_model_available(self) -> bool:
        try:
            self.client.show(self.model_name)
            return True
        except ollama.ResponseError as e:
            if e.status_code == 404:
                return False
            else:
                raise

    def test_connection(self) -> bool:
        try:
            self.client.list()
            return True
        except Exception:
            return False
