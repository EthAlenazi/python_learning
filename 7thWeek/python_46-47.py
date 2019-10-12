Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Labrary :
	def __init__(self , book ,shelf):
		self.book = book
		self.shelf = shelf
	def func:
		
SyntaxError: invalid syntax
>>> class Labrary :
	def __init__(self , book ,shelf):
		self.book = book
		self.shelf = shelf

	
>>> B1 = Labrary(300,45)
>>> class  section_science(Labrary):
	def __init__(self , book ,shelf ):
		super().__init__(book ,shelf)
		self.Name ="Pysics Book "
	def printer(self):
		print (self.book , self.shelf , self.Name)

		
>>> Book1 =section_science(50 ,14,"Math")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Book1 =section_science(50 ,14,"Math")
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> Book1 =section_science(50 ,14,)
>>> Book1.printer()
50 14 Pysics Book 
>>> Book1.book = 20
>>> Book1.shelf = 14
>>> Book1.printer()
20 14 Pysics Book 
>>> 
KeyboardInterrupt
>>> 
