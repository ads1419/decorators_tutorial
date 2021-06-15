'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021

Ex2: Write a decorator that runs the decorated function twice and returns a 2-tuple
with both return values.
'''


import random

def do_twice(wrapped):
	def wrapper(*args, **kwargs):
		roll_1 = wrapped(*args, **kwargs)
		roll_2 = wrapped(*args, **kwargs)
		return (roll_1, roll_2)

	return wrapper

@do_twice
def roll_dice():
	return random.randint(1, 6)


print(roll_dice())

