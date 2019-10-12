Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person :
	def __init__(self, name,age):
		self.name=name
		self.age =age

		
>>> class per :
	def __init__(self, name,age):
		self.name=name
		self.age =age
	def fun(self):
		print('hello me name is '+self.name)

		
>>> A1=per("hanan" , 36)
>>> A1.fun()
hello me name is hanan
>>> A2=per
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 
>>> 



>>> 
>>> 

>>> A2=per("asma",40)
>>> A2.fun()
hello me name is asma
>>> A1.fun()
hello me name is hanan
>>> A1.name="Atheer"
>>> A1.fun()
hello me name is Atheer
>>> prent(A1.age)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    prent(A1.age)
NameError: name 'prent' is not defined
>>> print(A1.age)
36
>>> A1.age =40
>>> print(A1.age)
40
>>> del A1.name
>>> print(A1)
<__main__.per object at 0x030111F0>
>>> print(A1.name)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(A1.name)
AttributeError: 'per' object has no attribute 'name'
>>> del A1
>>> print(A1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(A1)
NameError: name 'A1' is not defined
>>> 
