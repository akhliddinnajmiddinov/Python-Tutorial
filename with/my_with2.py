from contextlib import contextmanager

@contextmanager
def my_with(file_name):
    try:
        file = open(file_name, "w")
        yield file
    finally:
        file.close()


with my_with("salom.txt") as file:
    print(file.write("Hello"))