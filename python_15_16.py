Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt =[1,1,2,3,5,4,7,7,8,6,9]
>>> print(len(txt))
11
>>> print(txt)
[1, 1, 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> txt.insert(2 , 'A')
>>> print(txt)
[1, 1, 'A', 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> txt.remove{1}
SyntaxError: invalid syntax
>>> txt.remove(1)
>>> print(txt)
[1, 'A', 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> txt.pop()
9
>>> print(txt)
[1, 'A', 2, 3, 5, 4, 7, 7, 8, 6]
>>> txt.pop[]
SyntaxError: invalid syntax
>>> txt.pop(9)
6
>>> txt.clear();
>>> print(txt)
[]
>>> txt =[1,1,2,3,5,4,7,7,8,6,9]
>>> txt,1=['A','P','O','M','L','N']
SyntaxError: can't assign to literal
>>> txt.1=['A','P','O','M','L','N']
SyntaxError: invalid syntax
>>> ']
SyntaxError: EOL while scanning string literal
>>> Btxt=['A','P','O','M','L','N']
>>> Atxt=[]
>>> print(txt)
[1, 1, 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> print(Btxt)
['A', 'P', 'O', 'M', 'L', 'N']
>>> print(Atxt)
[]
>>> Atxt=txt.copy()
>>> print(Atxt)
[1, 1, 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> txt=Btxt
>>> print(txt)
['A', 'P', 'O', 'M', 'L', 'N']
>>> txt=list(Atxt)
>>> print(txt)
[1, 1, 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> pull=[list(7.2.6)]
SyntaxError: invalid syntax
>>> pull=[list(7,2,6)]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    pull=[list(7,2,6)]
TypeError: list expected at most 1 arguments, got 3
>>> pull=list((7,2,6))
>>> list.sort()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list.sort()
TypeError: descriptor 'sort' of 'list' object needs an argument
>>> print(txt)
[1, 1, 2, 3, 5, 4, 7, 7, 8, 6, 9]
>>> txt.sort();
>>> print(txt)
[1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
>>> txt.reverse()
>>> print(txt)
[9, 8, 7, 7, 6, 5, 4, 3, 2, 1, 1]
>>> txt.extend(Btxt)
>>> print(txt)
[9, 8, 7, 7, 6, 5, 4, 3, 2, 1, 1, 'A', 'P', 'O', 'M', 'L', 'N']
>>> tuble=('moon','flower')
>>> print(tuble)
('moon', 'flower')
>>> #we cannot remove , add or change value in type tuple.
>>> for X in tuble:
	print(X)

	
moon
flower
>>> 

	
>>> print(X[0])
f
>>> print(X[0:5])
flowe
>>> print(X[0:15])
flower
>>> print(X[5:10])
r
>>> print(X)
flower
>>> print(tuble)
('moon', 'flower')
>>> print(tuble[1])
flower
>>> print(tuble[0])
moon
>>> 
