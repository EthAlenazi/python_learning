Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> strong = "eat an apple with freands "
>>> print(len(strong));
26
>>> print(strip(strong));
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(strip(strong));
NameError: name 'strip' is not defined
>>> print(strong,strip());
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(strong,strip());
NameError: name 'strip' is not defined
>>> print(strong.rstrip());
eat an apple with freands
>>> print(strong.lower());
eat an apple with freands 
>>> 
KeyboardInterrupt
>>> print(strong.upper());
EAT AN APPLE WITH FREANDS 
>>> print(strong.replace(E,*));
SyntaxError: invalid syntax
>>> print(strong.replace("E","*"));
eat an apple with freands 
>>> print(strong.replace("e","*"));
*at an appl* with fr*ands 
>>> print(strong.split("w"));
['eat an apple ', 'ith freands ']
>>> 
['eat an apple ', 'ith freands ']
['eat an apple ', 'ith freands ']
>>> #this is code of 8days
>>> 
