Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> key = ('apple' , 'orange' , 'banana' , 'corn')
>>> if 'apple' in key :
	print("yes ther is apple ")

	
yes ther is apple 
>>> key = ('apple' , 'orange' , 'banana' , 'corn')*2
>>> 
>>> print(key)
('apple', 'orange', 'banana', 'corn', 'apple', 'orange', 'banana', 'corn')
>>> txtA =(1,2,3,4)
>>> txtB = (5,6,7,8,9)
>>> txt = txtA+txtB
>>> print(txt)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> txtA =(4,5,8,8,7,8)
>>> txtA =(4,5,8,8,7,8)
>>> txtA[1]=*
SyntaxError: invalid syntax
>>> #we can't change
>>> for A in txt:
	print(txt)

	
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> txt =(7,8,9)
>>> for A in txt:
	print (A);

	
7
8
9
>>> print(txt)
(7, 8, 9)
>>> printtxt = txtA+txtB
>>> print(len(txt))
3
>>> txt = txtA+txtB
>>> print(len(txt))
11
>>> table = tuple(('l','k','p','i'))
>>> print(teble)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(teble)
NameError: name 'teble' is not defined
>>> print(table)
('l', 'k', 'p', 'i')
>>> code = [4,5,6,7,8,'L','M','O']
>>> tcode =tuple(code)
>>> print(tcode)
(4, 5, 6, 7, 8, 'L', 'M', 'O')
>>> tuple.index(table)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tuple.index(table)
TypeError: index() takes at least 1 argument (0 given)
>>> V =('a','e' ,'i', 'o')
>>> index =V.index('i'):
	
SyntaxError: invalid syntax
>>> index =V.index('i'):
	
SyntaxError: invalid syntax
>>> index =V.index('i')
>>> print(index)
2
>>> i =V.index('i')
>>> print(i)
2
>>> #it doesn't matter the name the last exemple like was 'index' then 'i'
>>> number =V.count('O')
>>> print (number)
0
>>> number =V.count('o')
>>> print (number)
1
>>> number =V.count()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    number =V.count()
TypeError: count() takes exactly one argument (0 given)
>>> #we must to put parameter
>>> 
