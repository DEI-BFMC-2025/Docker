from multiprocessing import Value, Lock
import ctypes

class SharedFrame:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = Value(ctypes.c_char * max_size)  # shared memory array
        self.lock = Lock()
        self.frame_size = Value('i', 0)

    def write(self, data: bytes):
        with self.lock:
            size = min(len(data), self.max_size)
            ctypes.memmove(self.buffer.get_obj(), data, size)
            self.frame_size.value = size

    def read(self) -> bytes:
        with self.lock:
            return bytes(self.buffer.get_obj()[:self.frame_size.value])
