"""
The 'with' statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is
executed. Used in thread locks, database connections, file objects...any context manager.
Sources: https://docs.python.org/2.5/whatsnew/pep-343.html
         https://www.youtube.com/watch?v=C-gEQdGVXbk&index=11&t=697s
         https://book.pythontips.com/en/latest/context_managers.html
         https://docs.python.org/3/reference/datamodel.html#context-managers
"""
from contextlib import contextmanager


class File(object):
    """
    Implementing a context manager as a class
    """

    def __init__(self, file_name: str, mode: str = 'r'):
        self.file_object = open(file_name, mode)

    def __enter__(self):
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If an exception occurs, Python passes the type, value and traceback of the exception as parameters.
        :returns whether or not the exception should be suppressed. Not returning True will cause an exception to be
        raised by the 'with' statement
        """
        self.file_object.close()


@contextmanager
def open_file(name: str, mode: str = 'r'):
    """
    Implementing a context manager as a generator.
    The @contextmanager decorator will call contextmanager with open_file as an argument, which will return the
    generator wrapped by the GeneratorContextManager object.
    """
    f = open(name, mode)
    try:
        yield f
    except:
        # Handle exceptions
        pass
    finally:
        f.close()


if __name__ == '__main__':
    filename: str = 'file.txt'

    # Common usage of the 'with' statement for file objects
    with open(filename, 'r') as file:
        file_content = file.read()

    # Now using our context manager class
    with File(filename) as file:
        file_content = file.read()

    # And now with the generator context manager
    with open_file(filename) as file:
        file_content = file.read()
