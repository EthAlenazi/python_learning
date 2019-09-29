Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x lambda = a : a + 10
SyntaxError: invalid syntax
>>> x = lambda a : a+ 10
>>> print(x(5))
15
>>> x = lambda a : a+ 1
>>> print(x(5))
6
>>> x = lambda a,s,d: a*s+d
>>> print(x(5,2,1))
11
>>> 
