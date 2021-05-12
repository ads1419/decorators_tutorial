import functools


def wrapper(func):
    """Template for decorators"""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        """The wrapper function replacing the original"""
        # Do something before calling the function
        value = func(*args, **kwargs)
        # Do something after calling the function
        return value

    return _wrapper
