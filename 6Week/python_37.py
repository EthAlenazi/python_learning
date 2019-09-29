Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Array=['A'.'B','C','D','E','F']
SyntaxError: invalid syntax
>>> Array=['A','B','C','D','E','F']
>>> print(Array)
['A', 'B', 'C', 'D', 'E', 'F']
>>> print(Array[1],Array[2])
B C
>>> Array[0]=0
>>> print(Array)
[0, 'B', 'C', 'D', 'E', 'F']
>>> print(len(Array))
6
>>> 
