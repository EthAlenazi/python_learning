# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:00:14 2019

@author: ETH
"""

try:
    print(A)
except NameError:
    print("Error type :")
    print("not defined !! ")    
except :
    print("Error type :")
    print("it has another Error   ")    
        
print("================================")

try:
    print (A+B)
    print("================================")
    
except NameError: 
    print("Error type :")
    print("not defined !! ")    
except :
    print("Error type :")
    print("it has another Error   ")  

A=4
B=50
try:
    print ('the result =')
    print (A+B)
    print("================================")
    
except NameError: 
    print("Error type :")
    print("not defined !! ")    
else :
    print("thank you :")
    print("your code without Error  ")  
    
print("================================")

try :
    print(A,N)
except:
    print("*****************")
finally:
    print("don't matter if it has Error or not ")
        