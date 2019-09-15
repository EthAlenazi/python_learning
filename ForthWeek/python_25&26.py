Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set = {1,3,5,7,8}
>>> set.add(4)
>>> set.add(12)
>>> set.add(8)
>>> print(set)
{1, 3, 4, 5, 7, 8, 12}
>>> print(set)
{1, 3, 4, 5, 7, 8, 12}
>>> set.pop(8)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set.pop(8)
TypeError: pop() takes no arguments (1 given)
>>> set.discard(8)
>>> print(set)
{1, 3, 4, 5, 7, 12}
>>> del set
>>> print(set)
<class 'set'>
>>> animal = {'name':'pigeon','type':'bird','skin cover':'feathers'}
>>> typeOFAnimal=animal.get('type')
>>> print(typeOFAnimal)
bird
>>> seet={2,5,8,9}
>>> print(seet)
{8, 9, 2, 5}
>>> seet.update([1,2,3,5,])
>>> print(seet)
{1, 2, 3, 5, 8, 9}
>>> #add mulitple element
>>> del seet
>>> print(seet)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(seet)
NameError: name 'seet' is not defined
>>> 
>>> 
>>> 
>>> 
>>> prinr(animal)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    prinr(animal)
NameError: name 'prinr' is not defined
>>> print(animal)
{'name': 'pigeon', 'type': 'bird', 'skin cover': 'feathers'}
>>> animal['skin cover'] = '****'
>>> print(animal)
{'name': 'pigeon', 'type': 'bird', 'skin cover': '****'}
>>> 
