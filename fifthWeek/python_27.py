Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=(9,5,2,4,1,)
>>> B=(1,4,8,9,3)
>>> A=450
>>> B=500
>>> if A<=B:
	print("A less then B")

	
A less then B
>>> if A!=B:
	print("A not equal B")

	
A not equal B
>>> if A==B:
	print("A  equal B")

	
>>> if A==B:
 print("A  equal B")

 
>>> if A==B:
print("A  equal B")
SyntaxError: expected an indented block
>>> if A==B:
 print("A  equal B")
 elif A!=B:
	 
SyntaxError: invalid syntax
>>> if A==B:
    print("A  equal B")
     elif A!=B :
	     
SyntaxError: unexpected indent
>>> if A==B :
	print('A equal B')
	elif A != B:
		
SyntaxError: invalid syntax
>>> if A==B :
	print('A equal B')
	elif A != B: print ("A not equal B")
	
SyntaxError: invalid syntax
>>> num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
SyntaxError: multiple statements found while compiling a single statement
>>> num = 3
>>> if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
SyntaxError: invalid syntax
>>> if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")

    
Positive number
>>> if A==B :
	print('A equal B')
elif A != B:
	print('A not B')

	
A not B
>>> if A==B :
	print('A equal B')
elif A<B:
	print('A less than B')
elif A != B:
	print('A not B')

	
A less than B
>>> if A==B :
	print('A equal B')
else A != B:
	print('A not B')
	
SyntaxError: invalid syntax
>>> if A==B :
	print('A equal B')
else A!= B:
	print('A not B')
	
SyntaxError: invalid syntax
>>> if A==B :
	print('A equal B')
elif A != B:
	print('A not B')

	
A not B
>>> if A==B :
	print('A equal B')
else :
	print('A not B')

	
A not B
>>> if A<B:A=B

>>> print(A)
500
>>> print(B)
500
>>> A=10
>>> print(A) if A>B else print(B)
500
>>> print(A) if A<B else print(B)
10
>>> print(A) if A<B else print(B) if A==B else print(B-A)
10
>>> print(A) if A>B else print(B) if A==B else print(B-A)
490
>>> if A<B and A!=B print ('A less then B and not equal')
SyntaxError: invalid syntax
>>> if A<B and A!=B print('A less then B and not equal')
SyntaxError: invalid syntax
>>> if A<B and A!=B: print('A less then B and not equal')

A less then B and not equal
>>> if A<B and A==B: print('A less then B and not equal')

>>> if A<B or A==B: print('A less then B and not equal')

A less then B and not equal
>>> if A<B or A==B: print('A less then B Or not equal')

A less then B Or not equal
>>> if A <=10:
	print('A less Or equal 10')
if B>100:
	
SyntaxError: invalid syntax
>>> if A <=10:
	print('A less Or equal 10')
 if B>100:
	 
SyntaxError: unindent does not match any outer indentation level
>>> if A <=10:
	print('A less Or equal 10')
  if B>100:
	  
SyntaxError: unindent does not match any outer indentation level
>>> if A <=10:
	print('A less Or equal 10')
      if B>100:
	      
SyntaxError: unindent does not match any outer indentation level
>>> if A <=10:
	print('A less Or equal 10')
	if B>90:
		print('B more then 90')
		else : print('error!')
		
SyntaxError: invalid syntax
>>> if A <=10:
	print('A less Or equal 10')
	if B>90:
		print('B more then 90')
		else :
			
SyntaxError: invalid syntax
>>> if A <=10:
	print('A less Or equal 10')
	if B>90:
		print('B more then 90')
		else:
			
SyntaxError: invalid syntax
>>> if A <=10:
	print('A less Or equal 10')
	if B>90:
		print('B more then 90')
	else:
		print('error!')

		
A less Or equal 10
B more then 90
>>> 
