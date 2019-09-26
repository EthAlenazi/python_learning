Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ADF (Name):
	for X in Name:
		print(X)

		
>>> NAME=['ATHEER','BDOOR','AHMAED']
>>> ADF(NAME)
ATHEER
BDOOR
AHMAED
>>> def Amoon(x):
	return 5 * x

>>> print(Amoon(2))
10
>>> print(Amoon(5))
25
>>> print(Amoon(15))
75
>>> def FAMILY (Ch1,Ch2,Ch3):
	print ("the youngest child is "+Ch3 )

	
>>> FAMILY(Ch1='Asrar',Ch2='Abrar',Ch3='Anfal')
the youngest child is Anfal
>>> def FAMILY (*Ch):
	print ("the youngest child is "+ Ch[4] )

	
>>> FAMILY('Asrar','Abrar','Anfal')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    FAMILY('Asrar','Abrar','Anfal')
  File "<pyshell#17>", line 2, in FAMILY
    print ("the youngest child is "+ Ch[4] )
IndexError: tuple index out of range
>>> FAMILY("Asrar","Abrar","Anfal")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    FAMILY("Asrar","Abrar","Anfal")
  File "<pyshell#17>", line 2, in FAMILY
    print ("the youngest child is "+ Ch[4] )
IndexError: tuple index out of range
>>> FAMILY('Asrar','Abrar','Anfal','DALAL')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    FAMILY('Asrar','Abrar','Anfal','DALAL')
  File "<pyshell#17>", line 2, in FAMILY
    print ("the youngest child is "+ Ch[4] )
IndexError: tuple index out of range
>>> 
>>> def FAMILY (*Ch):
	print ("the youngest child is "+ Ch[3])

	
>>> FAMILY("1","2","3")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    FAMILY("1","2","3")
  File "<pyshell#23>", line 2, in FAMILY
    print ("the youngest child is "+ Ch[3])
IndexError: tuple index out of range
>>> def FAMILY (*Ch):
	print ("the youngest child is "+ Ch[2])

	
>>> FAMILY("1","2","3")
the youngest child is 3
>>> def FAMILY (*Ch):
	print ("the youngest child is "+ Ch[3])

	
>>> FAMILY('Asrar','Abrar','Anfal','DALAL')
the youngest child is DALAL
>>> def test(k):
	if k>0:
		result= k+test(k-1)
		print (result)
	else :
		result =0
	return result

>>> test(3)
1
3
6
6
>>> test(6)
1
3
6
10
15
21
21
>>> def test(k):
	if k>0:
		result= k+test(k-1)
		print (result +"this is test")
	else :
		result =0
	return result

>>> test(6)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    test(6)
  File "<pyshell#42>", line 3, in test
    result= k+test(k-1)
  File "<pyshell#42>", line 3, in test
    result= k+test(k-1)
  File "<pyshell#42>", line 3, in test
    result= k+test(k-1)
  [Previous line repeated 2 more times]
  File "<pyshell#42>", line 4, in test
    print (result +"this is test")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def test(k):
	if k>0:
		result= k+test(k-1)
		print (result +"this is test")
	else :
		result =0
	return result

>>> 
>>> 
>>> test(6)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    test(6)
  File "<pyshell#45>", line 3, in test
    result= k+test(k-1)
  File "<pyshell#45>", line 3, in test
    result= k+test(k-1)
  File "<pyshell#45>", line 3, in test
    result= k+test(k-1)
  [Previous line repeated 2 more times]
  File "<pyshell#45>", line 4, in test
    print (result +"this is test")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def test(k):
	if k>0:
		result= k+test(k-1)
		print (result)
	else :
		result =0
	return result

>>> test(6)
1
3
6
10
15
21
21
>>> def test(k):
	if k>0:
		result= k+test(k-1)
		print ("***"+result)
	else :
		result =0
	return result

>>> test(6)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    test(6)
  File "<pyshell#53>", line 3, in test
    result= k+test(k-1)
  File "<pyshell#53>", line 3, in test
    result= k+test(k-1)
  File "<pyshell#53>", line 3, in test
    result= k+test(k-1)
  [Previous line repeated 2 more times]
  File "<pyshell#53>", line 4, in test
    print ("***"+result)
TypeError: can only concatenate str (not "int") to str
>>> def test(k):
	if k>0:
		result= k+test(k-1)
		print (result*0)
	else :
		result =0
	return result

>>> test(5)
0
0
0
0
0
15
>>> #why 15 ?
>>> 
