Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt = " Please, I want {} sandwishes and {} donutes "
>>> print(txt)
 Please, I want {} sandwishes and {} donutes 
>>> print(txt.replace('I','We'))
 Please, We want {} sandwishes and {} donutes 
>>> print(txt)
 Please, I want {} sandwishes and {} donutes 
>>> print(txt.replace('I','We'))
 Please, We want {} sandwishes and {} donutes 
>>> txt = " Please, I want {*} sandwishes and {*} donutes "
>>> print(txt.replace('*','5',1))
 Please, I want {5} sandwishes and {*} donutes 
>>> #the number 1 because i want to change the first star
>>> print(txt.replace('*','7',2))
 Please, I want {7} sandwishes and {7} donutes 
>>> txt = " Please, I want {*} sandwishes and {-} donutes "
>>> print(txt.replace('-','7',1))
 Please, I want {*} sandwishes and {7} donutes 
>>> # i cant to do with the same icon so that i was change
>>> print(txt.replace('I','We'))
 Please, We want {*} sandwishes and {-} donutes 
>>> txt='Please, We want {*} sandwishes and {-} donutes'
>>> print(txt.replace('*','5',1))
Please, We want {5} sandwishes and {-} donutes
>>> txt = "Please, We want {5} sandwishes and {-} donutes"
>>> print(txt.replace('-','7',1))
Please, We want {5} sandwishes and {7} donutes
>>> txt ="Please, We want {5} sandwishes and {7} donutes"
>>> print
<built-in function print>
>>> print(txt)
Please, We want {5} sandwishes and {7} donutes
>>> print(txt.replace('a','A',))
PleAse, We wAnt {5} sAndwishes And {7} donutes
>>> txt ="PleAse, We wAnt {5} sAndwishes And {7} donutes"
>>> print (txt)
PleAse, We wAnt {5} sAndwishes And {7} donutes
>>> 
