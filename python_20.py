Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = {4,7,6,3,9,5}
>>> print(A)
{3, 4, 5, 6, 7, 9}
>>> A = {4,7,6,3,9,5,5}
>>> print(A)
{3, 4, 5, 6, 7, 9}
>>> A = {4,7,6,3,9,5,5,5,7,5,5}
>>> print(A)
{3, 4, 5, 6, 7, 9}
>>> #it is sort and unique.
>>> DT={'A','t','h','e','e','r',1,9,9,7}
>>> print(DT)
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
>>> print(DT)
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
>>> for D in DT:
	print(DT)

	
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
>>> print("A" in DT)
True
>>> for D in A:
	print(DT)

	
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
{1, 'r', 't', 7, 9, 'A', 'h', 'e'}
>>> for D in A:
	print(A)

	
{3, 4, 5, 6, 7, 9}
{3, 4, 5, 6, 7, 9}
{3, 4, 5, 6, 7, 9}
{3, 4, 5, 6, 7, 9}
{3, 4, 5, 6, 7, 9}
{3, 4, 5, 6, 7, 9}
>>> W = {'ahmad','yasser','adeel'}
>>> for X in W:
	print(X)

	
yasser
ahmad
adeel
>>> for D in A:
	print(D)

	
3
4
5
6
7
9
>>> for D in DT:
	print(D)

	
1
r
t
7
9
A
h
e
>>> DT.add('orange')
>>> print(DT)
{1, 'r', 't', 7, 9, 'A', 'h', 'orange', 'e'}
>>> DT.update(['sara','fish','faris'])
>>> print(DT)
{1, 'r', 't', 7, 9, 'faris', 'A', 'h', 'orange', 'sara', 'fish', 'e'}
>>> 
