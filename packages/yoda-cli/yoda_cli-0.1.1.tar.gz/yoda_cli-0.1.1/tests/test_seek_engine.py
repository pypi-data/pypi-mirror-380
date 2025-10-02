
from unittest.mock import MagicMock, patch

from yoda.core.seek_engine import SeekEngine
from yoda.utils.config import YodaConfig


@patch("yoda.core.seek_engine.CodebaseIndexer")
@patch("yoda.core.seek_engine.ModelManager")
@patch("questionary.text")
@patch("yoda.core.seek_engine.SeekEngine._is_codebase_related", return_value=True)
@patch("yoda.core.seek_engine.SeekEngine._print_with_highlighting")
def test_seek_engine_start_session(mock_print, mock_is_codebase_related, mock_questionary, mock_model_manager, mock_indexer):
    config = YodaConfig(project_path="/tmp", model_name="test_model")
    seek_engine = SeekEngine(config, mock_model_manager)

    mock_indexer.return_value.get_or_build_index.return_value = MagicMock()
    mock_questionary.return_value.unsafe_ask.side_effect = ["hello", "exit"]
    mock_model_manager.return_value.generate_stream.return_value = iter(["response"])

    seek_engine.start_session()

    assert len(seek_engine.conversation_history) == 2
    assert seek_engine.conversation_history[0]["role"] == "user"
    assert seek_engine.conversation_history[0]["content"] == "hello"
    assert seek_engine.conversation_history[1]["role"] == "assistant"

