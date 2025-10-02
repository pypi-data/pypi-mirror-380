
from pathlib import Path
from unittest.mock import MagicMock, patch

from yoda.core.indexer import CodebaseIndexer
from yoda.utils.config import YodaConfig


@patch("yoda.core.indexer.CodeParser.parse_directory")
@patch("llama_index.core.VectorStoreIndex.from_documents")
@patch("llama_index.core.SimpleDirectoryReader")
def test_indexer_build_index(mock_reader, mock_from_documents, mock_parse_directory):
    config = YodaConfig(project_path=Path("/tmp"), model_name="test_model", index_path=Path("/tmp/index"))
    indexer = CodebaseIndexer(config)

    mock_parse_directory.return_value = [MagicMock()]
    mock_reader.return_value.load_data.return_value = [MagicMock()]
    with patch("yoda.core.indexer.CodebaseIndexer.save_index") as mock_save_index:
        indexer.build_index(force=True)

    mock_from_documents.assert_called_once()


@patch("llama_index.core.indices.loading.load_indices_from_storage", return_value=[MagicMock()])
@patch("llama_index.core.storage.StorageContext.from_defaults", return_value=MagicMock())
def test_indexer_get_or_build_index_exists(mock_from_defaults, mock_load_indices):
    config = YodaConfig(project_path=Path("/tmp"), model_name="test_model", index_path=Path("/tmp/index"))
    indexer = CodebaseIndexer(config)

    with patch.object(Path, "exists") as mock_exists:
        mock_exists.return_value = True
        indexer.get_or_build_index()

    mock_load_indices.assert_called_once()

