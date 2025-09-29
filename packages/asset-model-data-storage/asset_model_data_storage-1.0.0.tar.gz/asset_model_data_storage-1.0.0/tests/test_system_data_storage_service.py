import os
import shutil
import tempfile

import pytest

from asset_model_data_storage.system_data_storage_service import SystemDataStorageService


@pytest.fixture(scope="function")
def temp_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    shutil.rmtree(dirpath)


@pytest.fixture(scope="function")
def storage(temp_dir):
    return SystemDataStorageService(base_path=temp_dir)


def test_save_and_load_file(storage):
    file_path = "test_dir/test_file.txt"
    data = b"Hello, world!"
    saved_path = storage.save_file(file_path, data)
    assert os.path.exists(saved_path)
    loaded = storage.load_file(file_path)
    assert loaded == data


def test_save_file_with_filelike(storage):
    file_path = "filelike.bin"
    data = b"filelike data"
    from io import BytesIO
    filelike = BytesIO(data)
    storage.save_file(file_path, filelike)
    assert storage.load_file(file_path) == data


def test_file_exists(storage):
    file_path = "exists.txt"
    assert not storage.file_exists(file_path)
    storage.save_file(file_path, b"exists")
    assert storage.file_exists(file_path)


def test_delete_file(storage):
    file_path = "delete_me.txt"
    storage.save_file(file_path, b"bye")
    assert storage.file_exists(file_path)
    assert storage.delete_file(file_path)
    assert not storage.file_exists(file_path)
    # Deleting non-existent file returns False
    assert not storage.delete_file(file_path)


def test_create_directory(storage):
    dir_path = "new_dir/subdir"
    assert storage.create_directory(dir_path)
    full_path = os.path.join(storage.base_path, dir_path)
    assert os.path.isdir(full_path)


def test_get_file_url(storage):
    file_path = "somefile.txt"
    expected = os.path.join(storage.base_path, file_path)
    assert storage.get_file_url(file_path) == expected


def test_load_file_not_found(storage):
    with pytest.raises(FileNotFoundError):
        storage.load_file("notfound.txt")


def test_save_file_permission_error(storage, monkeypatch):
    file_path = "no_permission.txt"

    def raise_permission(*a, **kw):
        raise PermissionError("No permission")

    monkeypatch.setattr("builtins.open", raise_permission)
    with pytest.raises(PermissionError):
        storage.save_file(file_path, b"data")


def test_delete_file_permission_error(storage, monkeypatch):
    file_path = "perm_delete.txt"
    storage.save_file(file_path, b"data")

    def raise_permission(path):
        raise PermissionError("No permission")

    monkeypatch.setattr(os, "remove", raise_permission)
    assert not storage.delete_file(file_path)
