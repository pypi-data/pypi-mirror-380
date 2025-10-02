from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.prompt import Confirm
from simple_term_menu import TerminalMenu

from yoda import __version__
from yoda.core.indexer import CodebaseIndexer
from yoda.core.model_manager import ModelManager
from yoda.core.seek_engine import SeekEngine
from yoda.core.wisdom import Wisdom
from yoda.utils.config import ConfigManager, YodaConfig


app = typer.Typer(
    name="yoda",
    help="Offline codebase wisdom and seek tool powered by local LLMs",
    add_completion=False,
)

console = Console()


def version_callback(value: bool):
    if value:
        console.print(f"Yoda CLI v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    ),
):
    pass


@app.command()
def init(
    path: Optional[Path] = typer.Argument(
        None,
        help="Path to the codebase to index (default: current directory)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
    model: str = typer.Option(
        "codellama:7b",
        "--model",
        "-m",
        help="Ollama model to use",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force re-initialization even if already initialized",
    ),
):
    if path is None:
        path = Path.cwd()
    try:
        console.print(f"[cyan]Initializing Yoda for[/cyan] [bold]{path}[/bold]")

        config_manager = ConfigManager(path)
        if config_manager.exists() and not force:
            console.print("[yellow]⚠[/yellow] Yoda is already initialized for this project")
            console.print("[dim]Use --force to re-initialize[/dim]")
            raise typer.Exit(1)

        if force and config_manager.exists():
            console.print("[yellow]Re-initializing (force mode)[/yellow]")

        config = config_manager.initialize(model_name=model)

        console.print(f"[cyan]Setting up Ollama with model:[/cyan] {model}")
        model_manager = ModelManager(model_name=model)

        if not model_manager.ensure_ollama_running():
            console.print(f"[red]✗[/red] Failed to set up Ollama")
            raise typer.Exit(1)

        if not model_manager.ensure_model():
            console.print(f"[red]✗[/red] Failed to set up model {model}")
            raise typer.Exit(1)

        indexer = CodebaseIndexer(config)
        indexer.build_index(force=True)

        console.print("\n[green]✓[/green] [bold]Yoda initialization complete![/bold]")
        console.print("\n[cyan]Next steps:[/cyan]")
        console.print("  • yoda wisdom     - Generate wisdom from the codebase")
        console.print("  • yoda seek       - Start interactive chat session")
        console.print("  • yoda update     - Update index after code changes")

    except typer.Exit:
        raise
    except Exception as e:
        console.print(f"\n[red]✗ Error:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def wisdom(
    path: Path = typer.Option(
        Path.cwd(),
        "--path",
        "-p",
        help="Path to the codebase (default: current directory)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output path for wisdom file (default: WISDOM.md)",
    ),
):
    try:
        config_manager = ConfigManager(path)
        if not config_manager.exists():
            console.print("[yellow]Yoda is not initialized for this project. Initializing now...[/yellow]")
            init(path=path, model="codellama:7b", force=False)
            summon(path=path)
            config_manager = ConfigManager(path)

        config = config_manager.load_config()

        model_manager = ModelManager(model_name=config.model_name)

        if not model_manager.ensure_ollama_running():
            console.print(f"[red]✗[/red] Failed to set up Ollama")
            raise typer.Exit(1)

        if not model_manager.ensure_model():
            console.print(f"[red]✗[/red] Failed to set up model {config.model_name}")
            raise typer.Exit(1)

        generator = Wisdom(config, model_manager)
        generator.generate(output_path=output)

        console.print("\n[green]✓[/green] [bold]Wisdom generation complete![/bold]")

    except typer.Exit:
        raise
    except Exception as e:
        console.print(f"\n[red]✗ Error:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def seek(
    path: Path = typer.Option(
        Path.cwd(),
        "--path",
        "-p",
        help="Path to the codebase (default: current directory)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
):
    try:
        config_manager = ConfigManager(path)
        if not config_manager.exists():
            console.print("[yellow]Yoda is not initialized for this project. Initializing now...[/yellow]")
            init(path=path, model="codellama:7b", force=False)
            summon(path=path)
            config_manager = ConfigManager(path)

        config = config_manager.load_config()

        model_manager = ModelManager(model_name=config.model_name)

        if not model_manager.ensure_ollama_running():
            console.print(f"[red]✗[/red] Failed to set up Ollama")
            raise typer.Exit(1)

        if not model_manager.ensure_model():
            console.print(f"[red]✗[/red] Failed to set up model {config.model_name}")
            raise typer.Exit(1)

        seek_engine = SeekEngine(config, model_manager)
        seek_engine.start_session()

    except typer.Exit:
        raise
    except KeyboardInterrupt:
        console.print("\n\n[cyan]Goodbye![/cyan]")
        raise typer.Exit(0)
    except Exception as e:
        console.print(f"\n[red]✗ Error:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def summon(
    path: Path = typer.Option(
        Path.cwd(),
        "--path",
        "-p",
        help="Path to the codebase (default: current directory)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
):
    try:
        config_manager = ConfigManager(path)
        if not config_manager.exists():
            console.print("[red]✗[/red] Yoda is not initialized for this project")
            console.print("\n[yellow]Initialize first:[/yellow]")
            console.print(f"  yoda init {path}")
            raise typer.Exit(1)

        config = config_manager.load_config()
        current_model = config.model_name

        models = ["starcoder2:7b", "codellama:7b", "deepseek-coder:6.7b"]

        choices = []
        for model_name in models:
            if model_name == current_model:
                choices.append(f"{model_name} (current)")
            else:
                choices.append(model_name)

        terminal_menu = TerminalMenu(choices, title="Choose a model to summon:")
        selected_index = terminal_menu.show()

        if selected_index is None:
            console.print("[yellow]Summoning cancelled.[/yellow]")
            raise typer.Exit()

        new_model = choices[selected_index].replace(" (current)", "")

        if not Confirm.ask(f"Are you sure you want to summon {new_model}?"):
            console.print("[yellow]Summoning cancelled.[/yellow]")
            raise typer.Exit()

        model_manager = ModelManager(model_name=new_model)
        if not model_manager.is_model_available():
            if not Confirm.ask(f"Model {new_model} is not available locally. Download it now?"):
                console.print("[yellow]Summoning cancelled.[/yellow]")
                raise typer.Exit()

        config.model_name = new_model
        config_manager.save_config(config)

        model_manager = ModelManager(model_name=config.model_name)

        if not model_manager.ensure_ollama_running():
            console.print(f"[red]✗[/red] Failed to set up Ollama")
            raise typer.Exit(1)

        if not model_manager.ensure_model():
            console.print(f"[red]✗[/red] Failed to set up model {config.model_name}")
            raise typer.Exit(1)

        console.print(f"\n[green]✓[/green] [bold]Summoned model:[/bold] {new_model}")

    except typer.Exit:
        raise
    except Exception as e:
        console.print(f"\n[red]✗ Error:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def update(
    path: Path = typer.Option(
        Path.cwd(),
        "--path",
        "-p",
        help="Path to the codebase (default: current directory)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
):
    try:
        console.print("[cyan]Updating codebase index...[/cyan]")

        config_manager = ConfigManager(path)
        if not config_manager.exists():
            console.print("[red]✗[/red] Yoda is not initialized for this project")
            console.print("\n[yellow]Initialize first:[/yellow]")
            console.print(f"  yoda init {path}")
            raise typer.Exit(1)

        config = config_manager.load_config()

        indexer = CodebaseIndexer(config)
        indexer.update_index()

        console.print("\n[green]✓[/green] [bold]Index update complete![/bold]")

    except typer.Exit:
        raise
    except Exception as e:
        console.print(f"\n[red]✗ Error:[/red] {e}")
        raise typer.Exit(1)


def main_entry():
    app()


if __name__ == "__main__":
    main_entry()
