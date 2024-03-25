class store_results:
    _FILE_PATH = "files/log.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self._FILE_PATH, "a") as log_file:
            log_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n")

# with param not defined by task
class store_result_in_file_name():
    _DIR = "files"

    def __init__(self, file_name: str):  # here goes the param
        self.file_name = file_name

    def __call__(self, func):  # this is out decorator
        def wrapper(*args, **kwargs):
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(
                    f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n"
                )

        return wrapper

# with functions:

def store_results(func):
    _FILE_PATH = "files/log.txt"
    def wrapper(*args, **kwargs):
        with open(_FILE_PATH, "a") as log_file:
            log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")
    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
