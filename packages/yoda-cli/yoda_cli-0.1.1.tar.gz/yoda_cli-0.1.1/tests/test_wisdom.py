
from pathlib import Path
from unittest.mock import MagicMock, patch

from yoda.core.wisdom import Wisdom
from yoda.utils.config import YodaConfig


@patch("yoda.core.wisdom.CodebaseIndexer")
@patch("yoda.core.wisdom.ModelManager")
@patch("yoda.core.wisdom.Wisdom._analyze_structure")
def test_wisdom_generate(mock_analyze_structure, mock_model_manager, mock_indexer):
    config = YodaConfig(project_path=Path("/tmp"), model_name="test_model")
    wisdom = Wisdom(config, mock_model_manager)

    mock_indexer.return_value.get_or_build_index.return_value = MagicMock()
    mock_analyze_structure.return_value = {
        'total_files': 0,
        'languages': {},
        'total_functions': 0,
        'total_classes': 0,
        'file_tree': {},
        'parsed_files': []
    }
    mock_model_manager.generate.return_value = "Generated wisdom"

    with patch("builtins.open", MagicMock()):
        wisdom_content = wisdom.generate()

    assert isinstance(wisdom_content, str)

