'''
TUTORIAL / Geir Arne Hjelle / Introduction to Decorators: Power UP Your Python Code
https://www.youtube.com/watch?v=VWZAh1QrqRE&list=PLkSx7-yjGZ3aKxSk_rFQDz-YRAoUw-4EO
PyCon US, 2021
'''


def before_and_after(wrapped):
	def wrapper(*args, **kwargs):
		print("BEFORE") 					# to be executed before wrapped fn
		value = wrapped(*args, **kwargs)
		print("AFTER")						# after
		return value

	return wrapper


@before_and_after
def greet(name):
	print(f"Hello {name}!")


@before_and_after
def adder(num1, num2):
	return num1 + num2

'''
What this is essentially doing is:
	adder = before_and_after(adder)
'''



greet("Aditya")
solution = adder(10, 3)