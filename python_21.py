Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> test = {'Atheer ' , 'Ahmeed','Abrar','mariam'}
>>> print(test)
{'Ahmeed', 'Atheer ', 'mariam', 'Abrar'}
>>> print(len(test))
4
>>> test.remove('Atheer')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    test.remove('Atheer')
KeyError: 'Atheer'
>>> test.remove('Atheer')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    test.remove('Atheer')
KeyError: 'Atheer'
>>> 
>>> print(test)
{'Ahmeed', 'Atheer ', 'mariam', 'Abrar'}
>>> test.remove('Atheer ')
>>> # must be the same
>>> test.discard('Ahmeed')
>>> print(test)
{'mariam', 'Abrar'}
>>> test.pop()
'mariam'
>>> print(test)
{'Abrar'}
>>> test.clear()
>>> print(test)
set()
>>> del test
>>> print (test)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (test)
NameError: name 'test' is not defined
>>> print (test)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print (test)
NameError: name 'test' is not defined
>>> 
>>> 
>>> 
>>> 
>>> this =set(('n','j','o','t'))
>>> print(this)
{'n', 'j', 'o', 't'}
>>> this.add('5')
>>> print(this)
{'n', 'o', 't', '5', 'j'}
>>> test = ('n','j','o')
>>> print("this U test : ", this.union(test))
this U test :  {'n', 'o', 'j', 't', '5'}
>>> this.update(test)
>>> print(this)
{'n', 'o', 't', '5', 'j'}
>>> # 21day
