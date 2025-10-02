
import os
from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from yoda.cli import app

runner = CliRunner()


@patch("yoda.cli.ConfigManager")
@patch("yoda.cli.ModelManager")
@patch("yoda.cli.CodebaseIndexer")
def test_init(mock_indexer, mock_model_manager, mock_config_manager):
    result = runner.invoke(app, ["init", "--force"])
    assert result.exit_code == 0
    assert "Yoda initialization complete" in result.stdout


@patch("yoda.cli.ConfigManager")
@patch("yoda.cli.ModelManager")
@patch("yoda.cli.Wisdom")
def test_wisdom(mock_wisdom, mock_model_manager, mock_config_manager):
    mock_config_manager.return_value.exists.return_value = True
    mock_config_manager.return_value.load_config.return_value = MagicMock(model_name="test_model")
    mock_model_manager.return_value.ensure_ollama_running.return_value = True
    mock_model_manager.return_value.ensure_model.return_value = True
    mock_wisdom.return_value.generate.return_value = "/path/to/wisdom.md"

    result = runner.invoke(app, ["wisdom"])
    assert result.exit_code == 0
    assert "Wisdom generation complete" in result.stdout


@patch("yoda.cli.ConfigManager")
@patch("yoda.cli.ModelManager")
@patch("yoda.cli.SeekEngine")
def test_seek(mock_seek_engine, mock_model_manager, mock_config_manager):
    mock_config_manager.return_value.exists.return_value = True
    mock_config_manager.return_value.load_config.return_value = MagicMock(model_name="test_model")
    mock_model_manager.return_value.ensure_ollama_running.return_value = True
    mock_model_manager.return_value.ensure_model.return_value = True

    # Since seek is an interactive session, we just check if it starts up correctly
    result = runner.invoke(app, ["seek"], input="exit\n")
    assert result.exit_code == 0


@patch("yoda.cli.ConfigManager")
@patch("yoda.cli.CodebaseIndexer")
def test_update(mock_indexer, mock_config_manager):
    mock_config_manager.return_value.exists.return_value = True
    mock_config_manager.return_value.load_config.return_value = MagicMock()

    result = runner.invoke(app, ["update"])
    assert result.exit_code == 0
    assert "Index update complete" in result.stdout

