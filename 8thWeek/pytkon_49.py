Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=200
>>> def func():
	num=300
	print(num)

	
>>> func()
300
>>> print(num)
200
>>> def func():
	global num1
	num1=300

	
>>> func():
	
SyntaxError: invalid syntax
>>> func()
>>> print(num1)
300
>>> num1="it was change!"
>>> print(num1)
it was change!
>>> 
