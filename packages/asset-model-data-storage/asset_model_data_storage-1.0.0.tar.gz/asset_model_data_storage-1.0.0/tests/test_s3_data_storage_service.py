from unittest.mock import patch, MagicMock

import pytest
from botocore.exceptions import ClientError, NoCredentialsError

from asset_model_data_storage.s3_data_storage_service import S3DataStorageService


@pytest.fixture
def s3_client_mock():
    with patch('boto3.client') as mock:
        yield mock

@pytest.fixture
def s3_service(s3_client_mock):
    # Patch head_bucket to simulate bucket existence
    instance = MagicMock()
    s3_client_mock.return_value = instance
    instance.head_bucket.return_value = {}
    return S3DataStorageService(bucket_name='test-bucket', region_name='us-east-1')

def test_init_success(s3_service):
    assert s3_service.bucket_name == 'test-bucket'
    assert s3_service.region_name == 'us-east-1'

def test_init_no_credentials(s3_client_mock):
    s3_client_mock.side_effect = NoCredentialsError()
    with pytest.raises(ValueError, match='AWS credentials not found'):
        S3DataStorageService(bucket_name='test-bucket')

def test_init_bucket_not_found(s3_client_mock):
    instance = MagicMock()
    s3_client_mock.return_value = instance
    error = ClientError({'Error': {'Code': '404'}}, 'HeadBucket')
    instance.head_bucket.side_effect = error
    with pytest.raises(ValueError, match="S3 bucket 'test-bucket' not found"):
        S3DataStorageService(bucket_name='test-bucket')

def test_save_file(s3_service):
    s3_service.s3_client.put_object = MagicMock()
    url = s3_service.save_file('file.txt', b'data')
    assert url == 's3://test-bucket/file.txt'
    s3_service.s3_client.put_object.assert_called_once()

def test_save_file_filelike(s3_service):
    from io import BytesIO
    s3_service.s3_client.put_object = MagicMock()
    filelike = BytesIO(b'data')
    url = s3_service.save_file('file.txt', filelike)
    assert url == 's3://test-bucket/file.txt'
    s3_service.s3_client.put_object.assert_called_once()

def test_save_file_client_error(s3_service):
    s3_service.s3_client.put_object.side_effect = ClientError({'Error': {'Code': '500'}}, 'PutObject')
    with pytest.raises(ClientError):
        s3_service.save_file('file.txt', b'data')

def test_load_file(s3_service):
    mock_body = MagicMock()
    mock_body.read.return_value = b'data'
    s3_service.s3_client.get_object.return_value = {'Body': mock_body}
    data = s3_service.load_file('file.txt')
    assert data == b'data'
    s3_service.s3_client.get_object.assert_called_once()

def test_load_file_not_found(s3_service):
    error = ClientError({'Error': {'Code': 'NoSuchKey'}}, 'GetObject')
    s3_service.s3_client.get_object.side_effect = error
    with pytest.raises(FileNotFoundError):
        s3_service.load_file('nofile.txt')

def test_file_exists_true(s3_service):
    s3_service.s3_client.head_object.return_value = {}
    assert s3_service.file_exists('file.txt') is True
    s3_service.s3_client.head_object.assert_called_once()

def test_file_exists_false(s3_service):
    error = ClientError({'Error': {'Code': '404'}}, 'HeadObject')
    s3_service.s3_client.head_object.side_effect = error
    assert s3_service.file_exists('file.txt') is False

def test_delete_file_success(s3_service):
    s3_service.s3_client.delete_object.return_value = {}
    assert s3_service.delete_file('file.txt') is True
    s3_service.s3_client.delete_object.assert_called_once()

def test_delete_file_client_error(s3_service):
    s3_service.s3_client.delete_object.side_effect = ClientError({'Error': {'Code': '500'}}, 'DeleteObject')
    assert s3_service.delete_file('file.txt') is False

def test_create_directory_success(s3_service):
    s3_service.s3_client.put_object.return_value = {}
    assert s3_service.create_directory('dir/') is True
    s3_service.s3_client.put_object.assert_called_once()

def test_create_directory_client_error(s3_service):
    s3_service.s3_client.put_object.side_effect = ClientError({'Error': {'Code': '500'}}, 'PutObject')
    assert s3_service.create_directory('dir/') is False

def test_get_file_url(s3_service):
    url = s3_service.get_file_url('file.txt')
    assert url == 's3://test-bucket/file.txt'

def test_get_content_type(s3_service):
    assert s3_service._get_content_type('file.png') == 'image/png'
    assert s3_service._get_content_type('file.unknown') == 'application/octet-stream'
