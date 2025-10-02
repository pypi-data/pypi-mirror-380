"""Configuration utilities for Yoda CLI."""

import json
from pathlib import Path
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class YodaConfig(BaseModel):
    """Configuration model for Yoda project."""

    project_path: Path
    model_name: str = Field(default="codellama:7b")
    chunk_size: int = Field(default=1024)
    chunk_overlap: int = Field(default=200)
    index_path: Optional[Path] = None
    documents_path: Optional[Path] = None

    class Config:
        arbitrary_types_allowed = True


class ConfigManager:
    """Manages Yoda configuration for projects."""

    YODA_DIR = ".yoda"
    CONFIG_FILE = "config.json"

    def __init__(self, project_path: Path):
        """Initialize config manager.

        Args:
            project_path: Path to the project root
        """
        self.project_path = Path(project_path).resolve()
        self.yoda_dir = self.project_path / self.YODA_DIR
        self.config_file = self.yoda_dir / self.CONFIG_FILE

    def initialize(self, model_name: str = "codellama:7b") -> YodaConfig:
        """Initialize Yoda directory and config.

        Args:
            model_name: Name of the Ollama model to use

        Returns:
            YodaConfig instance
        """
        # Create .yoda directory structure
        self.yoda_dir.mkdir(exist_ok=True)
        (self.yoda_dir / "index").mkdir(exist_ok=True)
        (self.yoda_dir / "documents").mkdir(exist_ok=True)

        # Create config
        config = YodaConfig(
            project_path=self.project_path,
            model_name=model_name,
            index_path=self.yoda_dir / "index",
            documents_path=self.yoda_dir / "documents"
        )

        # Save config
        self.save_config(config)
        return config

    def load_config(self) -> Optional[YodaConfig]:
        """Load existing config.

        Returns:
            YodaConfig instance or None if not found
        """
        if not self.config_file.exists():
            return None

        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)

            # Convert string paths back to Path objects
            data['project_path'] = Path(data['project_path'])
            if data.get('index_path'):
                data['index_path'] = Path(data['index_path'])
            if data.get('documents_path'):
                data['documents_path'] = Path(data['documents_path'])

            return YodaConfig(**data)
        except Exception as e:
            raise RuntimeError(f"Failed to load config: {e}")

    def save_config(self, config: YodaConfig) -> None:
        """Save config to file.

        Args:
            config: YodaConfig instance to save
        """
        # Convert Path objects to strings for JSON serialization
        data = config.model_dump()
        data['project_path'] = str(data['project_path'])
        if data.get('index_path'):
            data['index_path'] = str(data['index_path'])
        if data.get('documents_path'):
            data['documents_path'] = str(data['documents_path'])

        with open(self.config_file, 'w') as f:
            json.dump(data, f, indent=2)

    def exists(self) -> bool:
        """Check if Yoda is initialized for this project.

        Returns:
            True if .yoda directory and config exist
        """
        return self.yoda_dir.exists() and self.config_file.exists()

    def get_or_create(self, model_name: str = "codellama:7b") -> YodaConfig:
        """Get existing config or create new one.

        Args:
            model_name: Model name for new config

        Returns:
            YodaConfig instance
        """
        if self.exists():
            return self.load_config()
        return self.initialize(model_name)
