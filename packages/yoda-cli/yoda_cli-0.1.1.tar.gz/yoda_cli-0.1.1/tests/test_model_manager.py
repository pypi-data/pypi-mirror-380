
from unittest.mock import MagicMock, patch

from yoda.core.model_manager import ModelManager


@patch("ollama.Client")
def test_ensure_model_already_exists(mock_client):
    mock_client.return_value.list.return_value = {
        "models": [{"name": "test_model:latest"}]
    }
    manager = ModelManager(model_name="test_model")
    assert manager.ensure_model() is True


@patch("ollama.Client")
@patch("subprocess.run")
def test_ensure_model_download(mock_subprocess_run, mock_client):
    mock_client.return_value.list.return_value = {"models": []}
    mock_subprocess_run.return_value = MagicMock(returncode=0)
    manager = ModelManager(model_name="test_model")
    assert manager.ensure_model() is True


@patch("yoda.core.model_manager.ModelManager._check_ollama_installed", return_value=True)
@patch("yoda.core.model_manager.ModelManager._ensure_ssh_key", return_value=True)
@patch("yoda.core.model_manager.ModelManager.test_connection", return_value=True)
def test_ensure_ollama_running_already_running(mock_test_connection, mock_ensure_ssh_key, mock_check_installed):
    manager = ModelManager()
    assert manager.ensure_ollama_running() is True


@patch("yoda.core.model_manager.ModelManager._check_ollama_installed", return_value=False)
@patch("yoda.core.model_manager.ModelManager._install_ollama", return_value=True)
@patch("yoda.core.model_manager.ModelManager._ensure_ssh_key", return_value=True)
@patch("yoda.core.model_manager.ModelManager.test_connection", side_effect=[False, True])
@patch("subprocess.Popen")
def test_ensure_ollama_running_install_and_start(mock_popen, mock_test_connection, mock_ensure_ssh_key, mock_install, mock_check_installed):
    manager = ModelManager()
    assert manager.ensure_ollama_running() is True

