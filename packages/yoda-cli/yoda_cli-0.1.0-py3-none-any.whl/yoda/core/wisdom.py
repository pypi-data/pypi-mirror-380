import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from yoda.core.indexer import CodebaseIndexer
from yoda.core.model_manager import ModelManager
from yoda.utils.config import YodaConfig

console = Console()


class Wisdom:

    def __init__(self, config: YodaConfig, model_manager: ModelManager):
        self.config = config
        self.model_manager = model_manager
        self.indexer = CodebaseIndexer(config)

    def generate(self, output_path: Optional[Path] = None) -> str:
        if output_path is None:
            output_path = self.config.project_path / "WISDOM.md"

        console.print("[cyan]Generating wisdom...[/cyan]")

        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("Loading codebase index...", total=None)
                index = self.indexer.get_or_build_index()
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing codebase structure...", total=None)
                structure = self._analyze_structure()
                progress.update(task, completed=True)

                sections = {}

                task = progress.add_task("Generating overview...", total=None)
                sections['overview'] = self._generate_overview(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing technology stack...", total=None)
                sections['tech_stack'] = self._generate_tech_stack(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Generating architecture section...", total=None)
                sections['architecture'] = self._generate_architecture(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Generating dependencies...", total=None)
                sections['dependencies'] = self._generate_dependencies(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing code structure...", total=None)
                sections['code_structure'] = self._generate_code_structure(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Generating getting started guide...", total=None)
                sections['getting_started'] = self._generate_getting_started(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Identifying core modules...", total=None)
                sections['core_modules'] = self._generate_core_modules()
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing data flow...", total=None)
                sections['data_flow'] = self._generate_data_flow(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Identifying key features...", total=None)
                sections['key_features'] = self._generate_key_features()
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing configuration...", total=None)
                sections['configuration'] = self._generate_configuration(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing testing setup...", total=None)
                sections['testing'] = self._generate_testing(structure)
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing performance...", total=None)
                sections['performance'] = self._generate_performance()
                progress.update(task, completed=True)

                task = progress.add_task("Analyzing security...", total=None)
                sections['security'] = self._generate_security()
                progress.update(task, completed=True)

                task = progress.add_task("Generating deployment guide...", total=None)
                sections['deployment'] = self._generate_deployment()
                progress.update(task, completed=True)

                task = progress.add_task("Compiling wisdom...", total=None)
                wisdom_content = self._compile_wisdom(sections, structure)
                progress.update(task, completed=True)

                task = progress.add_task("Validating markdown format...", total=None)
                is_valid, issues = self._validate_markdown(wisdom_content)
                progress.update(task, completed=True)

                if not is_valid:
                    console.print(f"[yellow]⚠ Found {len(issues)} formatting issue(s):[/yellow]")
                    for issue in issues:
                        console.print(f"  [yellow]•[/yellow] {issue}")

                    task = progress.add_task("Fixing formatting issues...", total=None)
                    wisdom_content = self._fix_markdown_issues(wisdom_content)
                    progress.update(task, completed=True)

                    is_valid_after_fix, remaining_issues = self._validate_markdown(wisdom_content)
                    if is_valid_after_fix:
                        console.print(f"[green]✓[/green] All formatting issues resolved")
                    else:
                        console.print(f"[yellow]⚠ {len(remaining_issues)} issue(s) remain:[/yellow]")
                        for issue in remaining_issues:
                            console.print(f"  [yellow]•[/yellow] {issue}")

                task = progress.add_task("Saving wisdom...", total=None)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(wisdom_content)
                progress.update(task, completed=True)

                console.print(f"[green]✓[/green] Wisdom saved to {output_path}")

                return wisdom_content

        except Exception as e:
            raise RuntimeError(f"Failed to generate wisdom: {e}")

    def _analyze_structure(self) -> Dict[str, Any]:
        from yoda.utils.file_parser import CodeParser

        parser = CodeParser()
        parsed_files = parser.parse_directory(self.config.project_path)

        languages = {}
        total_files = len(parsed_files)
        total_functions = 0
        total_classes = 0
        file_tree = {}

        for pf in parsed_files:
            languages[pf.language] = languages.get(pf.language, 0) + 1

            total_functions += len(pf.functions)
            total_classes += len(pf.classes)

            rel_path = pf.path.relative_to(self.config.project_path)
            parts = rel_path.parts

            current = file_tree
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            current[parts[-1]] = None

        return {
            'total_files': total_files,
            'languages': languages,
            'total_functions': total_functions,
            'total_classes': total_classes,
            'file_tree': file_tree,
            'parsed_files': parsed_files
        }

    def _generate_overview(self, structure: Dict[str, Any]) -> str:
        project_name = self.config.project_path.name

        lang_summary = ", ".join([f"{count} {lang}" for lang, count in structure['languages'].items()])

        key_files = []
        for pf in structure['parsed_files'][:20]:
            key_files.append(pf.path.name)

        context = f"""
Project: {project_name}
Total files: {structure['total_files']}
Languages: {lang_summary}
Total functions: {structure['total_functions']}
Total classes: {structure['total_classes']}
Key files: {', '.join(key_files[:10])}
"""

        prompt = f"""Analyze this codebase and write a detailed project overview (3-4 paragraphs).
Include:
- What the project does (infer from structure, file names, and directory organization)
- Main functionality and unique features
- Target users or use cases
- Overall technology philosophy and approach

Context:
{context}

Write a comprehensive, professional overview that captures the essence of this project:"""

        system = "You are a technical writer with deep software engineering expertise. Write clear, comprehensive, and insightful documentation."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.7,
                max_tokens=800
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate overview: {e}[/yellow]")
            return f"A {list(structure['languages'].keys())[0]} project with {structure['total_files']} files, containing {structure['total_functions']} functions and {structure['total_classes']} classes."

    def _generate_architecture(self, structure: Dict[str, Any]) -> str:
        def tree_to_text(tree: Dict, prefix: str = "", max_depth: int = 3, current_depth: int = 0) -> List[str]:
            if current_depth >= max_depth:
                return []

            lines = []
            items = sorted(tree.items())
            for i, (name, subtree) in enumerate(items):
                is_last = i == len(items) - 1
                current_prefix = "└── " if is_last else "├── "
                lines.append(f"{prefix}{current_prefix}{name}")

                if subtree is not None and isinstance(subtree, dict):
                    next_prefix = prefix + ("    " if is_last else "│   ")
                    lines.extend(tree_to_text(subtree, next_prefix, max_depth, current_depth + 1))

            return lines

        tree_text = "\n".join(tree_to_text(structure['file_tree']))

        top_dirs = list(structure['file_tree'].keys())[:8]

        prompt = f"""Analyze this project structure and write 2-3 paragraphs describing its high-level architecture and design decisions.

Focus on:
- Overall architectural approach (monolithic, microservices, layered, etc.)
- How directories are organized and why
- Module structure and responsibilities
- Code organization patterns and principles
- Separation of concerns

Project structure (top-level):
{', '.join(top_dirs)}

Total files: {structure['total_files']}
Total classes: {structure['total_classes']}
Total functions: {structure['total_functions']}

Describe the architecture in detail:"""

        system = "You are a senior software architect. Describe architecture clearly, focusing on high-level design decisions and organization principles."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.7,
                max_tokens=600
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate architecture: {e}[/yellow]")
            return f"The project follows a structured architecture with {structure['total_files']} files organized across multiple modules. The codebase contains {structure['total_classes']} classes and {structure['total_functions']} functions, demonstrating a well-organized approach to code organization."

    def _generate_key_components(self) -> str:
        queries = [
            "main entry point and initialization",
            "core functionality and business logic",
            "API endpoints and routes",
            "data models and schemas",
            "utility functions and helpers"
        ]

        component_contexts = []
        for query in queries:
            try:
                results = self.indexer.query(query, top_k=2)
                if results:
                    component_contexts.append(f"Query: {query}")
                    for result in results[:1]:
                        metadata = result.get('metadata', {})
                        file_path = metadata.get('file_path', 'unknown')
                        component_contexts.append(f"File: {file_path}")
            except Exception:
                pass

        context = "\n".join(component_contexts[:10])

        prompt = f"""Based on this codebase analysis, describe the key components (3-5 components).
For each component:
- Name and purpose
- Main responsibilities
- Key files

Analysis:
{context}

List key components:"""

        system = "You are a technical writer. Describe software components clearly."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.7,
                max_tokens=600
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate components: {e}[/yellow]")
            return "Key components to be included in the wisdom."

    def _generate_dependencies(self, structure: Dict[str, Any]) -> str:
        dependency_files = []
        dep_content_map = {}

        for pf in structure['parsed_files']:
            if pf.path.name in ('requirements.txt', 'package.json', 'Pipfile', 'pyproject.toml', 'go.mod', 'Cargo.toml', 'pom.xml', 'build.gradle'):
                try:
                    with open(pf.path, 'r', encoding='utf-8') as f:
                        content = f.read()[:1500]
                        dependency_files.append(pf.path.name)
                        dep_content_map[pf.path.name] = content
                except Exception:
                    pass

        if dependency_files:
            context_parts = []
            for filename in dependency_files[:3]:
                content = dep_content_map.get(filename, '')
                context_parts.append(f"**{filename}:**\n```\n{content[:800]}\n```")

            context = "\n\n".join(context_parts)

            prompt = f"""Analyze these dependency files and provide:

1. **Core Dependencies**: List 5-8 critical production dependencies with their versions and primary roles
2. **Development Dependencies**: List key development and test dependencies with their purposes
3. Brief explanation of the dependency management approach

Dependency files:
{context}

Provide a comprehensive dependencies analysis:"""

            system = "You are a technical writer specializing in dependency management. Provide clear, structured analysis of dependencies."

            try:
                description = self.model_manager.generate(
                    prompt=prompt,
                    system=system,
                    temperature=0.6,
                    max_tokens=700
                )

                return description
            except Exception as e:
                console.print(f"[yellow]Warning: Failed to generate dependencies: {e}[/yellow]")
                return f"Dependency files found: {', '.join(dependency_files)}\n\nSee these files for complete dependency information."
        else:
            return "No standard dependency files found in the codebase."

    def _generate_tech_stack(self, structure: Dict[str, Any]) -> str:
        languages = structure['languages']
        total = sum(languages.values())
        lang_percentages = {lang: (count / total) * 100 for lang, count in languages.items()}

        tech_info = f"Languages: {', '.join([f'{lang} ({pct:.1f}%)' for lang, pct in lang_percentages.items()])}"

        dependency_info = []
        for pf in structure['parsed_files']:
            if pf.path.name in ('requirements.txt', 'package.json', 'go.mod', 'Cargo.toml', 'pom.xml'):
                dependency_info.append(pf.path.name)

        context = f"{tech_info}\nDependency files found: {', '.join(dependency_info) if dependency_info else 'None'}"

        prompt = f"""List the main programming languages, frameworks, runtimes, build tools, databases, testing frameworks, and other critical tools used in this project.

Context:
{context}

Provide a clear, structured list of technologies:"""

        system = "You are a technical writer. List technologies clearly and concisely."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=500
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate tech stack: {e}[/yellow]")
            return context

    def _generate_code_structure(self, structure: Dict[str, Any]) -> str:
        def tree_to_text(tree: Dict, prefix: str = "", path: str = "") -> List[str]:
            lines = []
            items = sorted(tree.items())
            for i, (name, subtree) in enumerate(items):
                is_last = i == len(items) - 1
                current_prefix = "└── " if is_last else "├── "
                current_path = f"{path}/{name}" if path else name

                description = ""
                if subtree is not None and isinstance(subtree, dict):
                    if name in ('src', 'source'):
                        description = " [Core source code]"
                    elif name in ('test', 'tests', '__tests__'):
                        description = " [Test files]"
                    elif name in ('docs', 'documentation'):
                        description = " [Documentation]"
                    elif name in ('config', 'conf', 'configuration'):
                        description = " [Configuration files]"
                    elif name in ('build', 'dist', 'out', 'target'):
                        description = " [Build artifacts]"
                    elif name in ('lib', 'libs', 'vendor', 'node_modules'):
                        description = " [Dependencies]"
                    elif name in ('utils', 'utilities', 'helpers'):
                        description = " [Utility functions]"
                    elif name in ('core', 'engine'):
                        description = " [Core functionality]"

                lines.append(f"{prefix}{current_prefix}{name}{description}")

                if subtree is not None and isinstance(subtree, dict) and len(lines) < 30:
                    next_prefix = prefix + ("    " if is_last else "│   ")
                    lines.extend(tree_to_text(subtree, next_prefix, current_path))

            return lines

        tree_text = "\n".join(tree_to_text(structure['file_tree']))
        return f"```\n{tree_text}\n```"

    def _generate_getting_started(self, structure: Dict[str, Any]) -> str:
        setup_files = []
        for pf in structure['parsed_files']:
            if pf.path.name.lower() in ('readme.md', 'setup.py', 'makefile', 'dockerfile', 'package.json'):
                setup_files.append(pf.path.name)

        context = f"Setup files found: {', '.join(setup_files)}\nLanguages: {', '.join(structure['languages'].keys())}"

        prompt = f"""Based on this project structure, provide:
1. Prerequisites (required software, versions)
2. Installation steps (clear, numbered commands)
3. Configuration requirements (env variables, config files)
4. Commands to run the project in development
5. Commands to run tests

Context:
{context}

Provide a comprehensive getting started guide:"""

        system = "You are a technical writer. Create clear, step-by-step instructions."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=700
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate getting started: {e}[/yellow]")
            return "See project documentation for setup instructions."

    def _generate_core_modules(self) -> str:
        queries = [
            "main entry point initialization startup",
            "core business logic functionality",
            "API routes endpoints handlers",
            "data models database schemas",
            "authentication authorization security"
        ]

        module_contexts = []
        for query in queries:
            try:
                results = self.indexer.query(query, top_k=2)
                if results:
                    for result in results[:1]:
                        metadata = result.get('metadata', {})
                        file_path = metadata.get('file_path', 'unknown')
                        module_contexts.append(f"- {file_path}")
            except Exception:
                pass

        context = "\n".join(module_contexts[:15])

        prompt = f"""Describe the top 4-6 core modules/components in this project. For each:
- Location (file/directory)
- Purpose and responsibility
- Key classes or functions
- How it interacts with other modules

Key files found:
{context}

Describe the core modules:"""

        system = "You are a software architect. Describe system components clearly."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.7,
                max_tokens=700
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate core modules: {e}[/yellow]")
            return "Core modules documentation to be generated."

    def _generate_data_flow(self, structure: Dict[str, Any]) -> str:
        prompt = f"""Explain how data moves through this system in 4-6 main steps.
Include aspects like:
- User requests or input
- Authentication/validation
- Business logic processing
- Data persistence
- Response formatting

Languages: {', '.join(structure['languages'].keys())}

Describe the data flow:"""

        system = "You are a software architect. Explain data flow clearly and concisely."

        try:
            description = self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.7,
                max_tokens=500
            )

            diagram = """
```mermaid
flowchart LR
    A[User Request] --> B{Authentication}
    B -->|Valid| C[Business Logic]
    B -->|Invalid| D[Error Response]
    C --> E[Database Query]
    E --> F[Data Processing]
    F --> G[Response Formatting]
    G --> H[Client Response]
```
"""
            return f"{description}\n\n### Data Flow Diagram\n{diagram}"
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate data flow: {e}[/yellow]")
            return "Data flow documentation to be generated."

    def _generate_key_features(self) -> str:
        queries = [
            "main features functionality capabilities",
            "user interface API endpoints",
            "data processing analysis",
            "integration external services"
        ]

        feature_contexts = []
        for query in queries:
            try:
                results = self.indexer.query(query, top_k=2)
                if results:
                    for result in results[:1]:
                        text = result.get('text', '')[:200]
                        feature_contexts.append(text)
            except Exception:
                pass

        context = "\n\n".join(feature_contexts[:8])

        prompt = f"""List and describe 4-6 major features of this project.
For each feature:
- What it does
- Why it's important
- How it impacts users or the system

Code context:
{context}

Describe the key features:"""

        system = "You are a product manager. Describe features clearly and their value."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.7,
                max_tokens=600
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate key features: {e}[/yellow]")
            return "Key features documentation to be generated."

    def _generate_configuration(self, structure: Dict[str, Any]) -> str:
        config_files = []
        for pf in structure['parsed_files']:
            if any(name in pf.path.name.lower() for name in ['.env', 'config', 'settings', '.yaml', '.toml', '.ini']):
                config_files.append(pf.path.name)

        context = f"Config files found: {', '.join(config_files[:10]) if config_files else 'None detected'}"

        prompt = f"""Describe the configuration approach for this project:
- Environment variables needed
- Configuration files and their purposes
- Security considerations for configuration
- Any relevant dependencies for configuration management

Context:
{context}

Describe the configuration:"""

        system = "You are a DevOps engineer. Explain configuration clearly."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=500
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate configuration: {e}[/yellow]")
            return context

    def _generate_testing(self, structure: Dict[str, Any]) -> str:
        test_files = []
        for pf in structure['parsed_files']:
            if 'test' in pf.path.name.lower() or 'spec' in pf.path.name.lower():
                test_files.append(pf.path.name)

        context = f"Test files found: {len(test_files)}\nSample test files: {', '.join(test_files[:5]) if test_files else 'None detected'}"

        prompt = f"""Describe the testing setup for this project:
- Testing frameworks used
- Test structure and organization
- Types of tests (unit, integration, e2e)
- How to run tests
- Coverage expectations

Context:
{context}

Describe the testing approach:"""

        system = "You are a test engineer. Explain testing practices clearly."

        try:
            description = self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=500
            )

            diagram = """
```mermaid
graph TD
    A[Test Suite] --> B[Unit Tests]
    A --> C[Integration Tests]
    A --> D[E2E Tests]
    B --> E[Services]
    B --> F[Utilities]
    C --> G[API Endpoints]
    C --> H[Database Operations]
    D --> I[User Workflows]
```
"""
            return f"{description}\n\n### Test Architecture\n{diagram}"
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate testing: {e}[/yellow]")
            return context

    def _generate_performance(self) -> str:
        queries = [
            "caching performance optimization",
            "database queries indexing",
            "async asynchronous concurrent parallel",
            "scalability load balancing"
        ]

        perf_contexts = []
        for query in queries:
            try:
                results = self.indexer.query(query, top_k=1)
                if results:
                    metadata = results[0].get('metadata', {})
                    file_path = metadata.get('file_path', '')
                    if file_path:
                        perf_contexts.append(f"- {file_path}")
            except Exception:
                pass

        context = "\n".join(perf_contexts[:8]) if perf_contexts else "No specific performance optimizations detected"

        prompt = f"""Discuss performance considerations for this project:
- Caching strategies
- Database optimization
- Scalability approaches
- Async/concurrent processing

Files with potential performance code:
{context}

Describe performance considerations:"""

        system = "You are a performance engineer. Explain optimization strategies clearly."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=500
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate performance: {e}[/yellow]")
            return "Performance considerations to be documented."

    def _generate_security(self) -> str:
        queries = [
            "authentication authorization security",
            "encryption hashing password",
            "input validation sanitization",
            "CORS security headers middleware"
        ]

        security_contexts = []
        for query in queries:
            try:
                results = self.indexer.query(query, top_k=1)
                if results:
                    metadata = results[0].get('metadata', {})
                    file_path = metadata.get('file_path', '')
                    if file_path:
                        security_contexts.append(f"- {file_path}")
            except Exception:
                pass

        context = "\n".join(security_contexts[:8]) if security_contexts else "No specific security implementations detected"

        prompt = f"""Detail the security measures in this project:
- Authentication mechanisms
- Authorization and access control
- Data protection (encryption, hashing)
- Input validation
- Security headers and middleware

Files with security code:
{context}

Describe security measures:"""

        system = "You are a security engineer. Explain security measures clearly."

        try:
            return self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=500
            )
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate security: {e}[/yellow]")
            return "Security measures to be documented."

    def _generate_deployment(self) -> str:
        queries = [
            "docker deployment container",
            "CI CD pipeline",
            "production build deploy",
            "kubernetes orchestration"
        ]

        deploy_contexts = []
        for query in queries:
            try:
                results = self.indexer.query(query, top_k=1)
                if results:
                    metadata = results[0].get('metadata', {})
                    file_path = metadata.get('file_path', '')
                    if file_path:
                        deploy_contexts.append(f"- {file_path}")
            except Exception:
                pass

        context = "\n".join(deploy_contexts[:8]) if deploy_contexts else "No specific deployment configurations detected"

        prompt = f"""Describe the deployment approach for this project:
- Deployment architecture
- Build and deployment process
- Production environment setup
- Monitoring and logging

Deployment-related files:
{context}

Describe deployment:"""

        system = "You are a DevOps engineer. Explain deployment clearly."

        try:
            description = self.model_manager.generate(
                prompt=prompt,
                system=system,
                temperature=0.6,
                max_tokens=500
            )

            diagram = """
```mermaid
graph TB
    A[Load Balancer] --> B[App Server 1]
    A --> C[App Server 2]
    B --> D[Database Primary]
    C --> D
    D --> E[Database Replica]
    B --> F[Redis Cache]
    C --> F
```
"""
            return f"{description}\n\n### Deployment Architecture\n{diagram}"
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to generate deployment: {e}[/yellow]")
            return "Deployment documentation to be generated."

    def _compile_wisdom(self, sections: Dict[str, str], structure: Dict[str, Any]) -> str:
        project_name = self.config.project_path.name
        languages = structure['languages']
        total = sum(languages.values())
        lang_percentages = {lang: (count / total) * 100 for lang, count in languages.items()}

        arch_diagram = """```mermaid
graph TB
    A[Client/Frontend] --> B[API Layer]
    B --> C[Business Logic]
    C --> D[Data Access Layer]
    D --> E[Database]
    B --> F[External Services]
    C --> G[Cache Layer]
```"""

        dep_diagram = """```mermaid
graph LR
    A[Main App] --> B[Framework]
    A --> C[Database Driver]
    A --> D[Utility Library]
    B --> E[HTTP Server]
    C --> F[Connection Pool]
```"""

        wisdom = f"""# 🏛️ {project_name} - Wisdom from the Code Temple

## 📜 Overview

{sections.get('overview', 'Project overview to be generated.')}

## 🛠️ Technology Stack

{sections.get('tech_stack', 'Technology stack to be analyzed.')}

**Language Distribution:**
{chr(10).join([f'- {lang}: {pct:.1f}%' for lang, pct in sorted(lang_percentages.items(), key=lambda x: x[1], reverse=True)])}

## 🏗️ Architecture

{sections.get('architecture', 'Architecture description to be generated.')}

### System Architecture Diagram

{arch_diagram}

### Core Components

{sections.get('core_modules', 'Core components to be identified.')}

### Design Patterns

Based on the codebase structure, this project follows common architectural patterns including modular design, separation of concerns, and layered architecture approaches.

## 📦 Dependencies

{sections.get('dependencies', 'Dependencies to be analyzed.')}

### Dependency Graph

{dep_diagram}

## 📁 Code Temple Structure

{sections.get('code_structure', 'Code structure to be generated.')}

## 🚀 Getting Started

{sections.get('getting_started', 'Setup instructions to be generated.')}

## 💡 Core Modules

{sections.get('core_modules', 'Core modules documentation to be generated.')}

## 🔄 Data Flow

{sections.get('data_flow', 'Data flow documentation to be generated.')}

## 🎯 Key Features

{sections.get('key_features', 'Key features to be documented.')}

## 🔐 Configuration & Environment

{sections.get('configuration', 'Configuration documentation to be generated.')}

## 🧪 Testing

{sections.get('testing', 'Testing documentation to be generated.')}

## 📊 Performance Considerations

{sections.get('performance', 'Performance considerations to be documented.')}

## 🔒 Security

{sections.get('security', 'Security measures to be documented.')}

## 🚢 Deployment

{sections.get('deployment', 'Deployment documentation to be generated.')}

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:
- Follow the existing code style and conventions
- Write tests for new features
- Update documentation as needed
- Submit pull requests for review

## 📄 License

See LICENSE file in the project root for license information.

## 📚 Additional Resources

- Project documentation (if available in docs/)
- API documentation
- Architecture decision records
- Changelog

---

*🤖 This wisdom was automatically generated by Yoda CLI - May the Force of understanding be with you.*
"""

        return wisdom

    @staticmethod
    def _validate_markdown(content: str) -> Tuple[bool, List[str]]:
        issues = []

        code_fence_pattern = r'```'
        code_fences = re.findall(code_fence_pattern, content)
        if len(code_fences) % 2 != 0:
            issues.append(f"Unbalanced code fences: found {len(code_fences)} ``` markers (should be even)")

        inline_code_pattern = r'(?<!`)`(?!`)'
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                continue
            inline_backticks = re.findall(inline_code_pattern, line)
            if len(inline_backticks) % 2 != 0:
                issues.append(f"Line {i}: Unbalanced inline code backticks")

        mermaid_blocks = re.finditer(r'```mermaid\n(.*?)```', content, re.DOTALL)
        for match in mermaid_blocks:
            diagram_content = match.group(1).strip()
            if not diagram_content:
                issues.append("Empty Mermaid diagram block found")
            elif not any(keyword in diagram_content for keyword in ['graph', 'flowchart', 'sequenceDiagram', 'classDiagram']):
                issues.append("Mermaid diagram missing diagram type declaration")

        incomplete_code_blocks = re.finditer(r'```\s*\n\s*```', content)
        if list(incomplete_code_blocks):
            issues.append("Empty or incomplete code blocks found")

        single_backtick_lines = re.finditer(r'^\s*```\s*$', content, re.MULTILINE)
        count = len(list(single_backtick_lines))
        if count > 0 and count % 2 != 0:
            issues.append(f"Potential incomplete code block markers found")

        dangling_commands = re.finditer(r'^```\s*\w+\s*$(?!\n.*?```)', content, re.MULTILINE)
        if list(dangling_commands):
            issues.append("Code blocks with language specifier but no closing marker")

        return len(issues) == 0, issues

    @staticmethod
    def _fix_markdown_issues(content: str) -> str:
        lines = content.split('\n')
        fixed_lines = []
        in_code_block = False
        code_block_start_line = -1

        for i, line in enumerate(lines):
            if line.strip().startswith('```'):
                if in_code_block:
                    in_code_block = False
                    fixed_lines.append(line)
                else:
                    in_code_block = True
                    code_block_start_line = i
                    fixed_lines.append(line)
                continue

            fixed_lines.append(line)

        if in_code_block:
            fixed_lines.append('```')
            console.print(f"[yellow]Auto-closed unclosed code block at line {code_block_start_line + 1}[/yellow]")

        fixed_content = '\n'.join(fixed_lines)

        fixed_content = re.sub(r'```\s*\n\s*```\n?', '', fixed_content)

        def fix_empty_mermaid(match):
            return """```mermaid
graph LR
    A[Component A] --> B[Component B]
```"""

        fixed_content = re.sub(
            r'```mermaid\s*\n\s*```',
            fix_empty_mermaid,
            fixed_content
        )

        fixed_content = re.sub(r'\n{4,}', '\n\n\n', fixed_content)

        return fixed_content
