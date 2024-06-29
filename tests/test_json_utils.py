import pytest
import json
from unittest.mock import patch, mock_open
from datetime import datetime
from decimal import Decimal
from json_utils import default_serializer, save_data_to_json


def test_default_serializer():
    assert default_serializer(datetime(2024, 1, 1, 12, 0, 0)) == "01/01/2024, 12:00:00"
    assert default_serializer(Decimal('105.105')) == 105.105

@patch('builtins.open', new_callable=mock_open)
def test_save_data_to_json(mock_open):
    data = [
        {'id': 1, 'name': 'test', 'datetime': datetime(2024, 1, 1, 12, 0, 0), 'decimal': Decimal('105.105')}
    ]

    file_path = "output.json"

    save_data_to_json(data, file_path)

    mock_open.assert_called_once_with(file_path, 'w', encoding='utf-8')
    
    handle = mock_open()
    handle.write.assert_called()

    expected_data = json.dumps(data, ensure_ascii=False, indent=4, default=default_serializer)
    written_data = ''.join(call.args[0] for call in handle.write.call_args_list)

    assert json.loads(written_data) == json.loads(expected_data)
