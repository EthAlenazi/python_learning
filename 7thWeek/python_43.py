Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class AP:
	def __init__(self, Fname ,Lname):
		self.Fname =Fname
		self.Lname =Lname
	def fun(self):
		print(self.Fname ,self.Lname)

		
>>> A1=AP("Dan","Alenazi")
>>> A1.fun()
Dan Alenazi
>>> class Ap(A)
SyntaxError: invalid syntax
>>> 
p
>>> class Ap(AP):
	pass

>>> A101=Ap("Atheer","Alenazi")
>>> A101.fun()
Atheer Alenazi
>>> class Ap(AP):
	def __init__(self,Fname.Lname):
		
SyntaxError: invalid syntax
>>> class Ap(AP):
	def __init__(self,Fname,Lname):
		AP.__init__(self ,Fname,Lname)

		
>>> Q1=Ap("gaddah","Alasmari")
>>> Q1.fun()
gaddah Alasmari
>>> class Ap(AP):
	def __init__(self,Fname,Lname):
		AP.__init__(self ,Fname,Lname)
	def As
	
SyntaxError: invalid syntax
>>> class Ap(AP):
	def __init__(self,Fname,Lname):
		AP.__init__(self ,Fname,Lname)
	def As(self):
		print('your welcome in class children')

		
>>> Q1.As()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Q1.As()
AttributeError: 'Ap' object has no attribute 'As'
>>> class Ap(AP):
	def __init__(self,Fname,Lname):
		AP.__init__(self ,Fname,Lname)
	def X(self):
		print(self.Fname ,self.Lname)
		print('your welcome in class children')

		
>>> Q1=Ap("gaddah","Alasmari")
>>> Q1.X()
gaddah Alasmari
your welcome in class children
>>> 
