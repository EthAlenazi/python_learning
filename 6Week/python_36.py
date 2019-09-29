Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfunc(n):
	return lambda a : a*n

>>> deep = myfunc(9)
>>> print(deep(1))
9
>>> deep = myfunc(2)
>>> print(deep(10))
20
>>> 
>>> deep = myfunc(9):
	
SyntaxError: invalid syntax
>>> deep = myfunc(9) deep = myfunc(3)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
