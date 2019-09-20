Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def non():
	print('****')

	
>>> non()
****
>>> 
>>> def function(fname):
	print(fname+"Refrance")

	
>>> function("Amal")
AmalRefrance
>>> function("Amal"):
	
SyntaxError: invalid syntax
>>> def function(fname):
	print(fname+"  Refrance")

	
>>> function("Amal")
Amal  Refrance
>>> 
>>> function("Amal")
Amal  Refrance
>>> function("dalal")
dalal  Refrance
>>> function("rawam")
rawam  Refrance
>>> function()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    function()
TypeError: function() missing 1 required positional argument: 'fname'
>>> def function(fname ="Atheer"):
	print(fname+"  Refrance")

	
>>> function("dalal")
dalal  Refrance
>>> function()
Atheer  Refrance
>>> 
