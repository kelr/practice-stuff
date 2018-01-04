import sys

def fib(num):
	fib_list = list()
	a, b = 0, 1
	while a < num:
		fib_list.append(a)
		a, b = b, a + b 
	return fib_list