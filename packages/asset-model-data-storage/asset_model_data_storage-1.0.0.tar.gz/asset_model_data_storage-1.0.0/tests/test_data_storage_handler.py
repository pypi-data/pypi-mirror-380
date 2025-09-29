import pytest

from asset_model_data_storage.data_storage_handler import DataStorageHandler


class DummyHandler(DataStorageHandler):
    def save_file(self, file_path, data, content_type=None):
        return 'saved'

    def load_file(self, file_path):
        return b'data'

    def file_exists(self, file_path):
        return True

    def delete_file(self, file_path):
        return True

    def create_directory(self, dir_path):
        return True

    def get_file_url(self, file_path):
        return 'url/' + file_path


def test_normalize_path_removes_leading_slash():
    handler = DummyHandler()
    assert handler._normalize_path('/foo/bar') == 'foo/bar'
    assert handler._normalize_path('foo/bar') == 'foo/bar'
    assert handler._normalize_path('/foo\\bar') == 'foo/bar'


def test_cannot_instantiate_abstract_base():
    with pytest.raises(TypeError):
        DataStorageHandler()


def test_abstract_methods_raise_if_not_implemented():
    class IncompleteHandler(DataStorageHandler):
        pass

    # All abstract methods must be implemented, so instantiation should fail
    with pytest.raises(TypeError):
        IncompleteHandler()
