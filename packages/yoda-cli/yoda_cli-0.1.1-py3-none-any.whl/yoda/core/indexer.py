"""Codebase indexer using Faiss and LlamaIndex."""

import pickle
from llama_index.core import (
    Document,
    Settings,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.schema import TextNode
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing import Any, Dict, List, Optional

try:
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
except ImportError:
    from llama_index_embeddings_huggingface import HuggingFaceEmbedding

from yoda.utils.config import YodaConfig
from yoda.utils.file_parser import CodeParser, ParsedFile

console = Console()


class CodebaseIndexer:

    def __init__(self, config: YodaConfig):
        self.config = config
        self.parser = CodeParser()
        self.index: Optional[VectorStoreIndex] = None

        Settings.embed_model = HuggingFaceEmbedding(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        Settings.chunk_size = config.chunk_size
        Settings.chunk_overlap = config.chunk_overlap

    def build_index(self, force: bool = False) -> VectorStoreIndex:
        if not force and self._index_exists():
            try:
                return self.load_index()
            except Exception as e:
                console.print(f"[yellow]Warning: Failed to load existing index: {e}[/yellow]")
                console.print("[yellow]Rebuilding index...[/yellow]")

        console.print(f"[cyan]Indexing codebase at {self.config.project_path}[/cyan]")

        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("Parsing source files...", total=None)
                parsed_files = self.parser.parse_directory(self.config.project_path)
                progress.update(task, completed=True)

                if not parsed_files:
                    raise RuntimeError("No source files found to index")

                console.print(f"[green]✓[/green] Parsed {len(parsed_files)} files")

                task = progress.add_task("Creating documents...", total=None)
                documents = self._create_documents(parsed_files)

                wisdom_path = self.config.project_path / "WISDOM.md"
                if wisdom_path.exists():
                    try:
                        with open(wisdom_path, 'r', encoding='utf-8') as f:
                            wisdom_content = f.read()
                            wisdom_doc = Document(
                                text=wisdom_content,
                                metadata={
                                    'file_path': 'WISDOM.md',
                                    'language': 'markdown',
                                    'size': len(wisdom_content),
                                    'type': 'documentation',
                                    'description': 'Project overview and architecture documentation'
                                },
                                id_='WISDOM.md'
                            )
                            documents.append(wisdom_doc)
                            console.print(f"[green]✓[/green] Added WISDOM.md to index")
                    except Exception as e:
                        console.print(f"[yellow]Warning: Failed to add WISDOM.md: {e}[/yellow]")

                progress.update(task, completed=True)

                console.print(f"[green]✓[/green] Created {len(documents)} documents")

                task = progress.add_task("Building vector index...", total=None)
                self.index = VectorStoreIndex.from_documents(
                    documents,
                    show_progress=False
                )
                progress.update(task, completed=True)

                task = progress.add_task("Saving index to disk...", total=None)
                self.save_index()
                progress.update(task, completed=True)

                console.print(f"[green]✓[/green] Index saved to {self.config.index_path}")

                return self.index

        except Exception as e:
            raise RuntimeError(f"Failed to build index: {e}")

    def _create_documents(self, parsed_files: List[ParsedFile]) -> List[Document]:
        documents = []

        for pf in parsed_files:
            metadata = {
                'file_path': str(pf.path.relative_to(self.config.project_path)),
                'language': pf.language,
                'size': pf.size,
                'functions': pf.functions[:10],
                'classes': pf.classes[:10],
            }

            summary = self.parser.get_file_summary(pf)
            content = f"{summary}\n\n{'='*80}\n\n{pf.content}"

            doc = Document(
                text=content,
                metadata=metadata,
                id_=str(pf.path)
            )
            documents.append(doc)

        return documents

    def update_index(self) -> VectorStoreIndex:
        console.print("[cyan]Updating codebase index...[/cyan]")

        return self.build_index(force=True)

    def load_index(self) -> VectorStoreIndex:
        try:
            storage_context = StorageContext.from_defaults(
                persist_dir=str(self.config.index_path)
            )
            self.index = load_index_from_storage(storage_context)
            console.print(f"[green]✓[/green] Loaded index from {self.config.index_path}")
            return self.index

        except Exception as e:
            raise RuntimeError(f"Failed to load index: {e}")

    def save_index(self) -> None:
        if not self.index:
            raise RuntimeError("No index to save")

        try:
            self.config.index_path.mkdir(parents=True, exist_ok=True)
            self.index.storage_context.persist(
                persist_dir=str(self.config.index_path)
            )

        except Exception as e:
            raise RuntimeError(f"Failed to save index: {e}")

    def _index_exists(self) -> bool:
        if not self.config.index_path:
            return False

        index_path = Path(self.config.index_path)
        return (
            index_path.exists()
            and (index_path / "docstore.json").exists()
        )

    def get_or_build_index(self) -> VectorStoreIndex:
        if self.index:
            return self.index

        if self._index_exists():
            return self.load_index()

        return self.build_index()

    def query(self, query_text: str, top_k: int = 5) -> List[Dict[str, Any]]:
        if not self.index:
            self.get_or_build_index()

        try:
            retriever = self.index.as_retriever(similarity_top_k=top_k)
            nodes = retriever.retrieve(query_text)

            results = []
            for node in nodes:
                results.append({
                    'text': node.node.text,
                    'metadata': node.node.metadata,
                    'score': node.score
                })

            return results

        except Exception as e:
            raise RuntimeError(f"Failed to query index: {e}")
