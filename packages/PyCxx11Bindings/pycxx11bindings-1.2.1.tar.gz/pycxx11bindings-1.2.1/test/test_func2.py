import ctypes
import os

from cxx11bindings import C11Stream, ErrorCodes, PyC11Stream

# Load the DLL (use the full path if not in the current directory)
if os.name == "nt":
    dll = ctypes.CDLL("./Cxx11BindingsTests.dll")
elif os.name == "posix":
    dll = ctypes.CDLL("./Cxx11BindingsTests.so")
else:
    assert False, "Unsupported OS"

dll.test_c11_stream_write.argtypes = [
    ctypes.POINTER(C11Stream),
    ctypes.c_void_p,
    ctypes.c_int32,
]
dll.test_c11_stream_write.restype = ctypes.c_int32
dll.test_c11_stream_flush.argtypes = [ctypes.POINTER(C11Stream)]
dll.test_c11_stream_flush.restype = ctypes.c_int


def test_default1():
    filename = "default1.bin"
    try:
        with open(filename, "wb") as f:
            with PyC11Stream(f) as stream:
                data = b"abcdefghijklmnopqrstuvwxyz"
                ret = dll.test_c11_stream_write(stream.ptr, data, len(data))
                assert ret == 26
                # can we assume no flush yet ?
                assert os.path.getsize(filename) == 0
                ret = dll.test_c11_stream_flush(stream.ptr)
                assert ret == 0
                assert os.path.getsize(filename) == 26
    except Exception as e:
        print("Error occurred: ", e)
        assert False, "No exception should occur in test"
    finally:
        os.remove(filename)


def test_exception():
    filename = "exception.bin"
    try:
        with open(filename, "w"):
            pass
        assert os.path.getsize(filename) == 0
        # open read-only it should trigger an exception:
        with open(filename, "rb") as f:
            with PyC11Stream(f) as stream:
                data = b"abcdefghijklmnopqrstuvwxyz"
                ret = dll.test_c11_stream_write(stream.ptr, data, len(data))
                assert ret == ErrorCodes.C11_E_NOTSUPPORTED.value
                ret = dll.test_c11_stream_flush(stream.ptr)
                assert ret == 0
    except Exception as e:
        print("Error occurred: ", e)
        assert False, "No exception should occur in test"
    finally:
        os.remove(filename)
