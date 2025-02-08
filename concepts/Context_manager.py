# this is a context manager, handles things like close file connection even when we get an error somewhere
with open('notes.txt', 'w') as file:
    pass
    # print(file.read())

import time
import threading

# custom context manager class, has entry exit method in which we can do operations that we want.

class FileReadManager:
    lock = threading.Lock()

    def __init__(self, name):
        self.counter = 1
        self.name = name

    def __enter__(self):
        self.lock.acquire()
        print('lock acquired')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(2)
        self.counter = 1
        self.lock.release()
        print('lock released.')

    def perform_read(self):
        print(f'read performed by {self.name}')


with FileReadManager('name1') as file1:
    file1.perform_read()

with FileReadManager('name2') as file2:
    file2.perform_read()

# we can also do this with the help of inbuilt class decorator.

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
with open_managed_file('notes.txt') as f:
    f.write('adasd')
