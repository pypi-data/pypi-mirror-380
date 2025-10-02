"""File parsing utilities using tree-sitter."""

import os
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass

from tree_sitter import Language, Parser
import tree_sitter_python
import tree_sitter_javascript


@dataclass
class ParsedFile:
    """Represents a parsed source file."""

    path: Path
    language: str
    content: str
    functions: List[str]
    classes: List[str]
    imports: List[str]
    size: int


class CodeParser:
    """Parses source code files using tree-sitter."""

    # File extensions to language mapping
    LANGUAGE_MAP = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'javascript',
        '.tsx': 'javascript',
    }

    # Files and directories to ignore
    IGNORE_PATTERNS = {
        '.git', '.yoda', '__pycache__', 'node_modules', '.venv', 'venv',
        'env', '.env', 'dist', 'build', '.cache', '.pytest_cache',
        '.mypy_cache', '.tox', 'htmlcov', 'coverage', '.coverage',
        '*.pyc', '*.pyo', '*.pyd', '.DS_Store', '*.so', '*.dylib',
        '*.egg-info', '.eggs'
    }

    def __init__(self):
        """Initialize code parser with tree-sitter languages."""
        self.parsers: Dict[str, Parser] = {}
        self._build_parsers()

    def _build_parsers(self) -> None:
        """Build tree-sitter parsers for supported languages."""
        try:
            # Python parser
            python_lang = Language(tree_sitter_python.language())
            python_parser = Parser(python_lang)
            self.parsers['python'] = python_parser

            # JavaScript/TypeScript parser
            js_lang = Language(tree_sitter_javascript.language())
            js_parser = Parser(js_lang)
            self.parsers['javascript'] = js_parser

        except Exception as e:
            raise RuntimeError(f"Failed to build tree-sitter parsers: {e}")

    def get_language(self, file_path: Path) -> Optional[str]:
        """Get language for a file based on extension.

        Args:
            file_path: Path to the file

        Returns:
            Language name or None if not supported
        """
        suffix = file_path.suffix.lower()
        return self.LANGUAGE_MAP.get(suffix)

    def should_ignore(self, path: Path) -> bool:
        """Check if a path should be ignored.

        Args:
            path: Path to check

        Returns:
            True if path should be ignored
        """
        path_str = str(path)
        name = path.name

        # Check if any ignore pattern matches
        for pattern in self.IGNORE_PATTERNS:
            if pattern.startswith('*.'):
                # Extension pattern
                if name.endswith(pattern[1:]):
                    return True
            elif pattern in path_str.split(os.sep):
                # Directory name pattern
                return True

        return False

    def parse_file(self, file_path: Path) -> Optional[ParsedFile]:
        """Parse a single source file.

        Args:
            file_path: Path to the file to parse

        Returns:
            ParsedFile object or None if parsing failed
        """
        language = self.get_language(file_path)
        if not language or language not in self.parsers:
            return None

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            parser = self.parsers[language]
            tree = parser.parse(bytes(content, 'utf8'))

            # Extract structural information
            functions = self._extract_functions(tree.root_node, language)
            classes = self._extract_classes(tree.root_node, language)
            imports = self._extract_imports(tree.root_node, language)

            return ParsedFile(
                path=file_path,
                language=language,
                content=content,
                functions=functions,
                classes=classes,
                imports=imports,
                size=len(content)
            )

        except Exception as e:
            print(f"Warning: Failed to parse {file_path}: {e}")
            return None

    def _extract_functions(self, node, language: str) -> List[str]:
        """Extract function names from AST.

        Args:
            node: Tree-sitter node
            language: Language name

        Returns:
            List of function names
        """
        functions = []

        if language == 'python':
            if node.type == 'function_definition':
                name_node = node.child_by_field_name('name')
                if name_node:
                    functions.append(name_node.text.decode('utf8'))

        elif language == 'javascript':
            if node.type in ('function_declaration', 'method_definition', 'arrow_function'):
                name_node = node.child_by_field_name('name')
                if name_node:
                    functions.append(name_node.text.decode('utf8'))

        # Recursively process children
        for child in node.children:
            functions.extend(self._extract_functions(child, language))

        return functions

    def _extract_classes(self, node, language: str) -> List[str]:
        """Extract class names from AST.

        Args:
            node: Tree-sitter node
            language: Language name

        Returns:
            List of class names
        """
        classes = []

        if language == 'python':
            if node.type == 'class_definition':
                name_node = node.child_by_field_name('name')
                if name_node:
                    classes.append(name_node.text.decode('utf8'))

        elif language == 'javascript':
            if node.type == 'class_declaration':
                name_node = node.child_by_field_name('name')
                if name_node:
                    classes.append(name_node.text.decode('utf8'))

        # Recursively process children
        for child in node.children:
            classes.extend(self._extract_classes(child, language))

        return classes

    def _extract_imports(self, node, language: str) -> List[str]:
        """Extract import statements from AST.

        Args:
            node: Tree-sitter node
            language: Language name

        Returns:
            List of import statements
        """
        imports = []

        if language == 'python':
            if node.type in ('import_statement', 'import_from_statement'):
                imports.append(node.text.decode('utf8'))

        elif language == 'javascript':
            if node.type in ('import_statement', 'import_clause'):
                imports.append(node.text.decode('utf8'))

        # Recursively process children
        for child in node.children:
            imports.extend(self._extract_imports(child, language))

        return imports

    def parse_directory(self, directory: Path) -> List[ParsedFile]:
        """Parse all supported files in a directory recursively.

        Args:
            directory: Directory to parse

        Returns:
            List of ParsedFile objects
        """
        parsed_files = []

        for root, dirs, files in os.walk(directory):
            root_path = Path(root)

            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not self.should_ignore(root_path / d)]

            for file_name in files:
                file_path = root_path / file_name

                # Skip ignored files
                if self.should_ignore(file_path):
                    continue

                # Parse file if supported
                parsed = self.parse_file(file_path)
                if parsed:
                    parsed_files.append(parsed)

        return parsed_files

    def get_file_summary(self, parsed_file: ParsedFile) -> str:
        """Generate a text summary of a parsed file.

        Args:
            parsed_file: ParsedFile object

        Returns:
            Text summary
        """
        lines = [
            f"File: {parsed_file.path}",
            f"Language: {parsed_file.language}",
            f"Size: {parsed_file.size} bytes",
        ]

        if parsed_file.imports:
            lines.append(f"Imports: {len(parsed_file.imports)}")

        if parsed_file.classes:
            lines.append(f"Classes: {', '.join(parsed_file.classes[:5])}")
            if len(parsed_file.classes) > 5:
                lines.append(f"  ... and {len(parsed_file.classes) - 5} more")

        if parsed_file.functions:
            lines.append(f"Functions: {', '.join(parsed_file.functions[:5])}")
            if len(parsed_file.functions) > 5:
                lines.append(f"  ... and {len(parsed_file.functions) - 5} more")

        return "\n".join(lines)
