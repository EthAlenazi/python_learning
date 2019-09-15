Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> python =[1,2,3,4,5,6,8,8,7,9,7,5,0]
>>> returnValue = python.pop(2)
>>> print(returnValue)
3
>>> print(python)
[1, 2, 4, 5, 6, 8, 8, 7, 9, 7, 5, 0]
>>> returnValue = python.pop(2)
>>> print(returnValue)
4
>>> print(python)
[1, 2, 5, 6, 8, 8, 7, 9, 7, 5, 0]
>>> python.insert(0,'K')
>>> print(python)
['K', 1, 2, 5, 6, 8, 8, 7, 9, 7, 5, 0]
>>> A=python.index(8)
>>> print(A)
5
>>> python.sort()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    python.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> python.sort();
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    python.sort();
TypeError: '<' not supported between instances of 'int' and 'str'
>>> value = {1,1,2,5,4,43,2,2,2,5,6.9.9}
SyntaxError: invalid syntax
>>> value = [1,1,2,5,4,43,2,2,2,5,6.9.9]
SyntaxError: invalid syntax
>>> value =[1,1,2,5,4,43,2,2,2,5,6,9]
>>> value.sort()
>>> print()

>>> print(value)
[1, 1, 2, 2, 2, 2, 4, 5, 5, 6, 9, 43]
>>> python.sort()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    python.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> #we have problem because inside the python int and str
>>> value.remove(2)
>>> #remove first element found it
>>> print(value)
[1, 1, 2, 2, 2, 4, 5, 5, 6, 9, 43]
>>> value.extend(python)
>>> print(value)
[1, 1, 2, 2, 2, 4, 5, 5, 6, 9, 43, 'K', 1, 2, 5, 6, 8, 8, 7, 9, 7, 5, 0]
>>> python =('java','python','swifi')
>>> if 'pytho' in python:
	print('yss insid')

	
>>> 
>>> 

;


print (Hi)









	python =['java','python','swifi']value.extend(python)
	
SyntaxError: invalid syntax
>>> python =['java','python','swifi']
>>> if 'pytho' in python:
	print('yss insid')

	
>>> 
>>> if 'python' in python :
	print ("true it has ");

	
true it has 
>>> 
