Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=['A','B','C','D','E','F','G'0]
SyntaxError: invalid syntax
>>> for A=['A','B','C','D','E','F','G']
SyntaxError: invalid syntax
>>> for A=['A','B','C','D','E','F','G']
SyntaxError: invalid syntax
>>> A=['A','B','C','D','E','F','G']
>>> for B in A:
	print(B)

	
A
B
C
D
E
F
G
>>> for B in A:
	print(A)

	
['A', 'B', 'C', 'D', 'E', 'F', 'G']
['A', 'B', 'C', 'D', 'E', 'F', 'G']
['A', 'B', 'C', 'D', 'E', 'F', 'G']
['A', 'B', 'C', 'D', 'E', 'F', 'G']
['A', 'B', 'C', 'D', 'E', 'F', 'G']
['A', 'B', 'C', 'D', 'E', 'F', 'G']
['A', 'B', 'C', 'D', 'E', 'F', 'G']
>>> for B in A:
	print(B)

	
A
B
C
D
E
F
G
>>> print (B)
G
>>> 
>>> G
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    G
NameError: name 'G' is not defined
>>> print (B)
G
>>> for D in 'Atheer Alenazi':
	print(D)

	
A
t
h
e
e
r
 
A
l
e
n
a
z
i
>>> for D in 'Atheer Alenazi':
	print(D)
	if D==r:
		break

	
A
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    if D==r:
NameError: name 'r' is not defined
>>> for D in 'Atheer Alenazi':
	print(D)
	if D==r:
	break
SyntaxError: expected an indented block
>>> for D in 'Atheer Alenazi':
	print(D)
if D==r:
	break
SyntaxError: invalid syntax
>>> for D in 'Atheer Alenazi':
	print(D)
    if D==r:
	break
SyntaxError: unindent does not match any outer indentation level
>>> for D in 'Atheer Alenazi':
    print(D)
    if D==r:
	break
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> A=['Atheer Alenazi']
>>> 	for D in 'Atheer Alenazi':
    print(D)
    if D=="r":
	break
SyntaxError: unexpected indent
>>> for D in A:
	print(D)
	if D=='r':
	break
SyntaxError: expected an indented block
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for D in A:
     print(D)
     if D=='r':
       break

Atheer Alenazi
>>> for D in 'Atheer Alenazi':
     print(D)
     if D=='r':
       break

A
t
h
e
e
r
>>> for D in 'Athee**r Alenazi':
     if D=='r':
	 break
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for D in 'Athee**r Alenazi':
     if D=='r':
        break
print(D)
SyntaxError: invalid syntax
>>> for D in 'Athee**r Alenazi':
     if D=='r':
        break
         print(D)
         
SyntaxError: unexpected indent
>>> for D in 'Athee**r Alenazi':
     if D=='r':
        break
 print(D)
 
SyntaxError: unindent does not match any outer indentation level
>>> for D in "1,2,3,4":
	if D ==3 :
		break
	print(D)

	
1
,
2
,
3
,
4
>>> for D in "1,2,3,4":
	if D ==3 :
	break
	print(D)
	
SyntaxError: expected an indented block
>>> for D in "1,2,3,4":
	if D ==3 :
	  break
	print(D)

	
1
,
2
,
3
,
4
>>> for D in 'Atheer Alenazi':
     print(D)
     if D=='r':
       continue

A
t
h
e
e
r
 
A
l
e
n
a
z
i
>>> for D in 'Atheer Alenazi':
     print(D)
     continue

A
t
h
e
e
r
 
A
l
e
n
a
z
i
>>> for D in 'Atheer Alenazi':
     continue
     if D=="r":
	     print(0)

	     
>>> for D in 'Atheer Alenazi':
	if D == "r":
		continue
	print(D)

	
A
t
h
e
e
 
A
l
e
n
a
z
i
>>> 
