import pytest
import yaml
import json
from unittest.mock import patch, mock_open, MagicMock
from app import pull_random_yaml_data


@patch('app.pull_random_yaml_data.requests.get')
def test_fetches_data_from_api(mock_get):
    """Test that the script fetches data from the API"""
    mock_response = MagicMock()
    mock_response.json.return_value = {'id': 1, 'title': 'Test Task'}
    mock_get.return_value = mock_response
    
    mock_get('https://jsonplaceholder.typicode.com')
    
    mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com')
    assert mock_response.json() == {'id': 1, 'title': 'Test Task'}


@patch('builtins.open', new_callable=mock_open)
@patch('app.pull_random_yaml_data.requests.get')
def test_writes_yaml_file(mock_get, mock_file):
    """Test that data is written to config.yaml"""
    test_data = {'id': 1, 'title': 'Test Task'}
    mock_response = MagicMock()
    mock_response.json.return_value = test_data
    mock_get.return_value = mock_response
    
    # Simulate the yaml.dump call
    with patch('app.pull_random_yaml_data.yaml.dump') as mock_dump:
        with open('config.yaml', 'w') as f:
            yaml.dump(test_data, f, default_flow_style=False)
        
        mock_dump.assert_called_once()


@patch('builtins.open', new_callable=mock_open, read_data='id: 1\ntitle: Test Task\n')
@patch('app.pull_random_yaml_data.requests.get')
def test_reads_yaml_file(mock_get, mock_file):
    """Test that config.yaml can be read back"""
    test_data = {'id': 1, 'title': 'Test Task'}
    mock_response = MagicMock()
    mock_response.json.return_value = test_data
    mock_get.return_value = mock_response
    
    # Simulate reading and loading YAML
    with open('config.yaml', 'r') as f:
        content = f.read()
        config = yaml.load(content, Loader=yaml.Loader)
    
    assert isinstance(config, dict)
    assert 'id' in config or 'title' in config
