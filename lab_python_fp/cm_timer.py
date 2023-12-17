import time

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self 
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")

from contextlib import contextmanager
@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield 
    finally:
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time} seconds")