Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mylist=('apple','orenig','banana','cherry')
>>> list=iter(mylist)
>>> print(next(list))
apple
>>> print(next(list))
orenig
>>> print(next(list))
banana
>>> A="Atheer"
>>> a=iter(A)
>>> print(next(a))
A
>>> print(next(a))
t
>>> print(next(a))
h
>>> for X in mylist:
	print(X)

	
apple
orenig
banana
cherry
>>> for X in A:
	print(X)

	
A
t
h
e
e
r
>>> class myNumber:
	def __iter__(self):
		self.a+=1
		return a
	def __next__(self):
		x=self.a
		self.a +=1

		
>>> Q_1=myNumber()
>>> list=iter(Q_1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list=iter(Q_1)
  File "<pyshell#22>", line 3, in __iter__
    self.a+=1
AttributeError: 'myNumber' object has no attribute 'a'
>>> myiter=iter(Q_1)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    myiter=iter(Q_1)
  File "<pyshell#22>", line 3, in __iter__
    self.a+=1
AttributeError: 'myNumber' object has no attribute 'a'
>>> class myNumber:
	def __iter__(self):
		self.a+=1
		return a
	def __next__(self):
		X=self.a
		self.a +=1
		return X

	
>>> Q_1=myNumber()
>>> list=iter(Q_1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list=iter(Q_1)
  File "<pyshell#28>", line 3, in __iter__
    self.a+=1
AttributeError: 'myNumber' object has no attribute 'a'
>>> A1=myNumber()
>>> myiter + iter(myiteer)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    myiter + iter(myiteer)
NameError: name 'myiter' is not defined
>>> myiter + iter(A1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    myiter + iter(A1)
NameError: name 'myiter' is not defined
>>> myiter = iter(A1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    myiter = iter(A1)
  File "<pyshell#28>", line 3, in __iter__
    self.a+=1
AttributeError: 'myNumber' object has no attribute 'a'
>>> class myNumber:
	def __iter__(self):
		self.a +=1
		return self
	def __next__(self):
		X=self.a
		self.a +=1
		return X

	
>>> A1=myNumber()
>>> myiter = iter(A1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    myiter = iter(A1)
  File "<pyshell#36>", line 3, in __iter__
    self.a +=1
AttributeError: 'myNumber' object has no attribute 'a'
>>> class myNumber:
	def __iter__(self , a):
		self.a +=1
		return self
	def __next__(self):
		X=self.a
		self.a +=1
		return X

	
>>> A1=myNumber()
>>> myiter = iter(A1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    myiter = iter(A1)
TypeError: __iter__() missing 1 required positional argument: 'a'
>>> A1=myNumber(2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    A1=myNumber(2)
TypeError: myNumber() takes no arguments
>>> class ETH:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		D =self.a
		self.a +=1
		return D

	
>>> Q1 = ETH()
>>> Q2 = iter (Q1)
>>> 
>>> print(next(Q2))
1
>>> print(next(Q2))
2
>>> print(next(Q2))
3
>>> print(next(Q2))
4
>>> print(next(Q2))
5
>>> class Num:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.s <= 50:
			X =self.a
			self.a += 1
			return X
		else:
			raise stopIteration

		
>>> myclass = Num()
>>> myiter = iter(myclass)
>>> for V in myiter:
	print (V)

	
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    for V in myiter:
  File "<pyshell#72>", line 6, in __next__
    if self.s <= 50:
AttributeError: 'Num' object has no attribute 's'
>>> for V in myiter:
	print (V)

	
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    for V in myiter:
  File "<pyshell#72>", line 6, in __next__
    if self.s <= 50:
AttributeError: 'Num' object has no attribute 's'
>>> class Num:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a <= 50:
			X =self.a
			self.a += 1
			return X
		else:
			raise stopIteration

		
>>> myclass = Num()
>>> myiter = iter(myclass)
>>> for V in myiter:
	print (V)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    for V in myiter:
  File "<pyshell#81>", line 11, in __next__
    raise stopIteration
NameError: name 'stopIteration' is not defined
>>> 
