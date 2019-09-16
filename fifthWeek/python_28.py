Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=0
>>> while A < 10:
	print("yo can do it yourself")
	A+=1

	
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
yo can do it yourself
>>> while A > 10:
	print(A)
	A-=1

	
>>> while A > 10:
	print(A)
	A*=1

	
>>> while A <10:
	print(A)
	A*=1

	
>>> while A < 20:
	print(A)
	A+=1

	
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
>>> while A < 120:
	print(A)
	A+=1
	if A==50:
		break

	
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
>>> I=1
>>> while I<6
SyntaxError: invalid syntax
>>> while I<6:
	print(I)
	if I==3:
		break
	I += 1

	
1
2
3
>>> i=0
>>> while i < 20:
	i++
	
SyntaxError: invalid syntax
>>> while i < 20:
	i+=1
	if i==1 or i==3 or i==5:
		continue
	print(i)

	
2
4
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
>>> while i < 20:
	i+=1
	if i==1 or i==3 or i==5 or i==7 or i==9 or i==11 or i==13 or i==15 or i==17 or i==19:
		continue
	print(i)

	
>>> while i < 20:
	i+=1
	if i==1 or i==3 or i==5 or i==7 or i==9 or i==11 :
		continue
	print(i)

	
>>> while i < 20:
	i+=1
	if i==1 or i==3 or i==5 or i==7  :
		continue
	print(i)

	
>>> i=0
>>> while i < 20:
	i+=1
	if i==1 or i==3 or i==5 or i==7 or i==9 or i==11 or i==13 or i==15 or i==17 or i==19:
		continue
	print(i)

	
2
4
6
8
10
12
14
16
18
20
>>> i=0
>>> while i ==0 or i==2 or i==4 or i==6:
	i+=1
	print('odd number'+i)

	
Traceback (most recent call last):
  File "<pyshell#48>", line 3, in <module>
    print('odd number'+i)
TypeError: can only concatenate str (not "int") to str
>>> while i ==0 or i==2 or i==4 or i==6:
	i+=1
	print('odd number')

	
>>> while i==0 or i==2 or i==4 or i==6:
	i+=1
	print('odd number')

	
>>> print(i)
1
>>> i=0
>>> while i==0 or i==2 or i==4 or i==6:
	i+=1
	print('odd number')

	
odd number
>>> while i<6:
	print(i)
	i +=1
	else:
		
SyntaxError: invalid syntax
>>> while i<6:
	print(i)
	i +=1
else:
	print("i is not longer less than 6")

	
1
2
3
4
5
i is not longer less than 6
>>> 
