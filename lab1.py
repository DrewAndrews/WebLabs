def is_pallindrome(number):
	return str(number) == str(number)[::-1]

def three_lists(numbers):
	is_divided_by_two = [x for x in numbers if x % 2 == 0]
	is_divided_by_three = [x for x in numbers if x % 3 == 0]
	is_divided_by_five = [x for x in numbers if x % 5 == 0]
	return is_divided_by_two, is_divided_by_three, is_divided_by_five

def get_reversed(number):
	if number > 0:
		return str(number)[::-1].strip("0")
	return f"-{str(abs(number))[::-1].strip("0")}"

def root_by_n_pow(x, n):
	x0 = 1
	while True:
		xk = 1 / n * ((n - 1) * x0 + x / x0**(n - 1))
	if xk == x0:
		return xk
	else:
		x0 = xk

def is_prime(number):
	for i in range(2, int(number**0.5)):
		if number % i == 0:
			return False
	return True

def get_cache_simple(func):
	cache = func()
	def wrapper():
		return cache
	return wrapper

def get_cache_hard(count_of_returns):
	def decorator(func):
		cache = {}
		func.invocations = count_of_returns
		cache[func.__name__] = func()
		def wrapper():
			if func.invocations > 0:
				func.invocations -= 1
			if func.invocations == 0:
				cache[func.__name__] = func()
				return cache[func.__name__]
			return cache[func.__name__]
		return wrapper
	return decorator

@get_cache_simple
def some_func():
	return "String"

count_of_returns = 3
@get_cache_hard(count_of_returns)
def another_func():
	return "String"

another_func()
another_func()
another_func()
another_func()
another_func()
another_func()