'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021

Ex6: Rewrite @retry so that it only retries max_retries times.

'''

import random
import functools

def retry(max_retries):
	'''
	A decorator factory that returns a decorator according to an input parameter. 
	'''

	def decorator(wrapped):
		
		@functools.wraps(wrapped)
		def wrapper(*args, **kwargs):
			nonlocal max_retries
			while(max_retries):
				try:
					return wrapped(*args, **kwargs)
				except Exception as e:
					if max_retries <= 0:
						raise e
					max_retries -= 1
					

					print(f"Retrying ({e}). Retries left: {max_retries}")
		return wrapper

	return decorator


@retry(max_retries=3)
def only_roll_sixes():
	number = random.randint(1, 6)
	if number != 6:
		raise ValueError(number)
	return number


print(only_roll_sixes())