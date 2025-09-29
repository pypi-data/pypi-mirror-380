from unittest.mock import patch, MagicMock

import pytest

from asset_model_data_storage.data_storage_service import DataStorageService


# Fixtures and basic structure for DataStorageService tests will be added here.

@pytest.fixture
def mock_system_handler():
    with patch('asset_model_data_storage.data_storage_service.SystemDataStorageService') as mock:
        yield mock


@pytest.fixture
def mock_s3_handler():
    with patch('asset_model_data_storage.data_storage_service.S3DataStorageService') as mock:
        yield mock


def test_get_storage_handler_system(mock_system_handler):
    instance = MagicMock()
    mock_system_handler.return_value = instance
    service = DataStorageService(environment='SYSTEM', base_path='/tmp')
    handler = service.get_storage_handler()
    assert handler == instance
    mock_system_handler.assert_called_once_with(base_path='/tmp')


def test_get_storage_handler_aws(mock_s3_handler):
    instance = MagicMock()
    mock_s3_handler.return_value = instance
    service = DataStorageService(environment='AWS', s3_bucket='bucket')
    handler = service.get_storage_handler()
    assert handler == instance
    mock_s3_handler.assert_called_once_with(bucket_name='bucket')


def test_save_file_delegates_to_handler(mock_system_handler):
    handler = MagicMock()
    mock_system_handler.return_value = handler
    service = DataStorageService(environment='SYSTEM')
    service._storage_handler = handler
    handler.save_file.return_value = 'path/to/file'
    result = service.save_file('file.txt', b'data')
    handler.save_file.assert_called_once_with('file.txt', b'data', None)
    assert result == 'path/to/file'


def test_load_file_delegates_to_handler(mock_system_handler):
    handler = MagicMock()
    mock_system_handler.return_value = handler
    service = DataStorageService(environment='SYSTEM')
    service._storage_handler = handler
    handler.load_file.return_value = b'data'
    result = service.load_file('file.txt')
    handler.load_file.assert_called_once_with('file.txt')
    assert result == b'data'


def test_file_exists_delegates_to_handler(mock_system_handler):
    handler = MagicMock()
    mock_system_handler.return_value = handler
    service = DataStorageService(environment='SYSTEM')
    service._storage_handler = handler
    handler.file_exists.return_value = True
    result = service.file_exists('file.txt')
    handler.file_exists.assert_called_once_with('file.txt')
    assert result is True


def test_delete_file_delegates_to_handler(mock_system_handler):
    handler = MagicMock()
    mock_system_handler.return_value = handler
    service = DataStorageService(environment='SYSTEM')
    service._storage_handler = handler
    handler.delete_file.return_value = True
    result = service.delete_file('file.txt')
    handler.delete_file.assert_called_once_with('file.txt')
    assert result is True


def test_create_directory_delegates_to_handler(mock_system_handler):
    handler = MagicMock()
    mock_system_handler.return_value = handler
    service = DataStorageService(environment='SYSTEM')
    service._storage_handler = handler
    handler.create_directory.return_value = True
    result = service.create_directory('dir')
    handler.create_directory.assert_called_once_with('dir')
    assert result is True


def test_get_file_url_delegates_to_handler(mock_system_handler):
    handler = MagicMock()
    mock_system_handler.return_value = handler
    service = DataStorageService(environment='SYSTEM')
    service._storage_handler = handler
    handler.get_file_url.return_value = '/tmp/file.txt'
    result = service.get_file_url('file.txt')
    handler.get_file_url.assert_called_once_with('file.txt')
    assert result == '/tmp/file.txt'


def test_is_s3_storage():
    service = DataStorageService(environment='AWS')
    assert service.is_s3_storage() is True
    assert service.is_local_storage() is False


def test_is_local_storage():
    service = DataStorageService(environment='SYSTEM')
    assert service.is_local_storage() is True
    assert service.is_s3_storage() is False


def test_get_storage_handler_caches_instance(mock_system_handler):
    instance = MagicMock()
    mock_system_handler.return_value = instance
    service = DataStorageService(environment='SYSTEM')
    handler1 = service.get_storage_handler()
    handler2 = service.get_storage_handler()
    assert handler1 is handler2
    mock_system_handler.assert_called_once()
