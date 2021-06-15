'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021

Ex7: Rewrite the retry decorator as a callable class.

'''

import random
import functools

'''
A decorator is just a callable. Writing as classes can help us store state easily.
'''


# Exercise 7
class Retry:
    def __init__(self, func):
        # equivalent to define-time operation in a function decorator. 
        functools.update_wrapper(self, func)        # does the same thing as @functools.wrap
        self.func = func
        self.num_retries = 0

    def __call__(self, *args, **kwargs):
        # equivalent to call-time operations in a function decorator.
        while True:
            try:
                return self.func(*args, **kwargs)
            except Exception:
                self.num_retries += 1
                print(f"Retry attempt {self.num_retries}")