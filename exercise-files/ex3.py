'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021

Ex3: Write a decorator that stores references to decorated functions in a dictionary.

'''

import random
FUNCTIONS = {}

def register(wrapped):
	'''
	Does some processing when the decorated function is defined, and on every subsequent
	call not changes are made, as the function is not changed at all.

	'''
	
	FUNCTIONS[wrapped.__name__] = wrapped
	return wrapped

@register
def roll_dice():
	return random.randint(1, 6)


print(FUNCTIONS["roll_dice"]())

