Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> moon=[1,2,5,8,7,9,6,3,5,5]
>>> print(moon)
[1, 2, 5, 8, 7, 9, 6, 3, 5, 5]
>>> #this is set
>>> dictionary=['name':"Atheer','age':23,'Id':436005128]
	    
SyntaxError: invalid syntax
>>> dictionary={'name':"Atheer','age' : 23,'Id':436005128}
	    
SyntaxError: EOL while scanning string literal
>>> dictionary={'name':"Atheer','age' : 23,'Id':436005128}
	    
SyntaxError: EOL while scanning string literal
>>> dictionary={'name':'Atheer' , 'model':436 , 'age':23}
>>> dictionary={'name':"Atheer",'age':23,'Id':436005128}
>>> #the mistake was i was start with single cotationthen close Double Cotation
>>> print(dictionary)
{'name': 'Atheer', 'age': 23, 'Id': 436005128}
>>> S =["name"]
>>> S =dictionary["name"]
>>> print(S)
Atheer
>>> print(dictionary.get("name"))
Atheer
>>> dictionary ["age"]= 10
>>> print(dictionary)
{'name': 'Atheer', 'age': 10, 'Id': 436005128}
>>> for X indictionary:
	
SyntaxError: invalid syntax
>>> for X in dictionary:
	print(X);

	
name
age
Id
>>> for X in dictionary:
	print(dictionary[X]);

	
Atheer
10
436005128
>>> for X in dictionary.values():
	print(X);

	
Atheer
10
436005128
>>> print(dictionary.values())
dict_values(['Atheer', 10, 436005128])
>>> print(dictionary.items())
dict_items([('name', 'Atheer'), ('age', 10), ('Id', 436005128)])
>>> #22 day
>>> 
