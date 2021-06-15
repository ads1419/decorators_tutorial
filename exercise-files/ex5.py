'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021

Ex5: Rewrite @retry so that it only retries on specific, user-defined exceptions.

'''

import random
import functools

def retry(exception):
	'''
	A decorator factory that returns a decorator according to an input parameter. 
	'''

	def decorator(wrapped):
		@functools.wraps(wrapped)
		def wrapper(*args, **kwargs):
			while(True):
				try:
					return wrapped(*args, **kwargs)
				except exception as e:
					print(f"Retrying ({e})")
		return wrapper

	return decorator


@retry(ValueError)
def calculation():
	number = random.randint(-5, 5)
	if abs(1 / number) > 0.2:
		raise ValueError(number)
	return number


print(calculation())