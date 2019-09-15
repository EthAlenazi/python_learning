Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt ={'FName':'Atheer' , 'LName':'Alenazi','IdNumber':436005128}
>>> if "FName" in txt:
	print('yes ,FName in the keys in the txt')

	
yes ,FName in the keys in the txt
>>> print(len(txt))
3
>>> txt['age']=23
>>> print(txt)
{'FName': 'Atheer', 'LName': 'Alenazi', 'IdNumber': 436005128, 'age': 23}
>>> txt.pop('LName')
'Alenazi'
>>> print(txt)
{'FName': 'Atheer', 'IdNumber': 436005128, 'age': 23}
>>> txt.pop('LName')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    txt.pop('LName')
KeyError: 'LName'
>>> txt.popitem()
('age', 23)
>>> print(txt)
{'FName': 'Atheer', 'IdNumber': 436005128}
>>> del txt('FName')
SyntaxError: can't delete function call
>>> del txt['FName']
>>> print(txt)
{'IdNumber': 436005128}
>>> txt.clear()
>>> print(txt)
{}
>>> del txt
>>> print(txt)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(txt)
NameError: name 'txt' is not defined
>>> #23 day
