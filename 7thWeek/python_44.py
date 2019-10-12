Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class people:
	def __init__(self,Age,Fname,gendar):
		self.Age =Age
		self.Fname =Fname
		self.gendar= gendar
	def funSuper(self):
		print(self.Fname +"Welcme this is super class")

		
>>> class person(people):
	def __init__(self,Age,Fname,gendar):
		super().__init__(Age,Fname,gendar)

		
>>> per1=person(12,'shahed','Famel')
>>> per1.funSuper()
shahedWelcme this is super class
>>> class person(people):
	def __init__(self,Age,Fname,gendar):
		super().__init__(Age,Fname,gendar)
		self.year=2020

		
>>> per1=person(12,'shahed','Famel')
>>> print(per1.year)
2020
>>> class person(people):
	def __init__(self,Age,Fname,gendar,year):
		super().__init__(Age,Fname,gendar)
		self.date=year

		
>>> per1=person(12,'shahed','Famel',2019)
>>> print(per1.year)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(per1.year)
AttributeError: 'person' object has no attribute 'year'
>>> print(per1.Age)
12
>>> print(per1.year)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(per1.year)
AttributeError: 'person' object has no attribute 'year'
>>> print(per1.date)
2019
>>> 
