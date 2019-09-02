Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> X = 13
>>> A = 23
>>> print(X > 3 OR X < 20 )
SyntaxError: invalid syntax
>>> print(X > 3 or X < 20 )
True
>>> print(X > 3 and X < 20 )
True
>>> print(X < 3 and X < 20 )
False
>>> print ( X is not A )
True
>>> print ( X != A )
True
>>> print ( X is  A )
False
>>> print ( 23 is  A )
True
>>> print(X > 3 & X < 20 )
True
>>> 
