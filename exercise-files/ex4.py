'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021

Ex4: Write a decorator that repeatedly calls the decorated function as long as it raises
and exception.

'''

import random
import functools


def retry(wrapped):
	'''
	Sample usage: to continuously poll a resource until it becomes available.
	'''

	@functools.wraps(wrapped)
	def wrapper(*args, **kwargs):
		while(True):
			try:
				return wrapped(*args, **kwargs)
			except Exception as e:
				print(f"Retrying ({e})")

	return wrapper


@retry
def only_roll_sixes():
	number = random.randint(1, 6)
	if number != 6:
		raise ValueError(number)
	return number

print(only_roll_sixes())