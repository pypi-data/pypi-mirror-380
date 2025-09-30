import os

from cxx11bindings import PyC11Stream


def test_default():
    filename = "default.bin"
    try:
        with open(filename, "wb") as f:
            with PyC11Stream(f) as stream:
                assert stream is not None
    except Exception as e:
        print("Error occurred: ", e)
        assert False, "Failed to create PyC11Stream"


def test_truncate_file_to_10_bytes():
    file_path = "truncate_test.bin"
    # Write more than 10 bytes
    with open(file_path, "wb") as f:
        stream = PyC11Stream(f)
        stream.write(b"abcdefghijklmnopqrstuvwxyz")
    # Truncate to 10 bytes
    with open(file_path, "r+b") as f:
        stream = PyC11Stream(f)
        stream.truncate(10)
    # Verify length
    assert os.path.getsize(file_path) == 10
    # Optionally, check content
    with open(file_path, "rb") as f:
        stream = PyC11Stream(f)
        data = stream.read()
        assert data == b"abcdefghij"
