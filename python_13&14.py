Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> S =[];
>>> S =[ ];
>>> print(S)
[]
>>> name =['Atheer' ,'Abeer' ,'Ahad' ,'Wafa' , 'mariam']
>>> print(name)
['Atheer', 'Abeer', 'Ahad', 'Wafa', 'mariam']
>>> print(name.__len__)
<method-wrapper '__len__' of list object at 0x043793F0>
>>> txt=['apple','pnana' ,'orange',4,7,8,9]
>>> print(txt)
['apple', 'pnana', 'orange', 4, 7, 8, 9]
>>> palance = [1.3,2.1,5.2,2.0,5.5]
>>> print(palance)
[1.3, 2.1, 5.2, 2.0, 5.5]
>>> print(palance[0])
1.3
>>> for W in td
SyntaxError: invalid syntax
>>> for W in td:
	print (W);

	
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for W in td:
NameError: name 'td' is not defined
>>> 0for W in txt:
	print (W);
	
SyntaxError: invalid syntax
>>> for W in txt:
	print (W);

	
apple
pnana
orange
4
7
8
9
>>> for write in palance:
	print(write)

	
1.3
2.1
5.2
2.0
5.5
>>> txt[2]='***';
>>> print(txt)
['apple', 'pnana', '***', 4, 7, 8, 9]
>>> del txt[2];
>>> print(txt)
['apple', 'pnana', 4, 7, 8, 9]
>>> 
print(txt[0:2])
['apple', 'pnana']
>>> print(txt)
['apple', 'pnana', 4, 7, 8, 9]
>>> print(txt[2:5])
[4, 7, 8]
>>> print(txt[2:6])
[4, 7, 8, 9]
>>> if 5 in txt:
	print('saccess');

	
>>> 
>>> if '7' in txt:
	print("saccess");

	
>>> 
>>> print(txt)
['apple', 'pnana', 4, 7, 8, 9]
>>> if 'apple' in txt:
	print{'true'}
	
SyntaxError: invalid syntax
>>> if 4 in txt :
	print('saccess');

	
saccess
>>> if 'apple' in txt:
	print('it has')

	
it has
>>> list=['Atheer']*10
>>> print(list)
['Atheer', 'Atheer', 'Atheer', 'Atheer', 'Atheer', 'Atheer', 'Atheer', 'Atheer', 'Atheer', 'Atheer']
>>> 
