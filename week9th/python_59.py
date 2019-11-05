# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:54:10 2019

@author: ETH
"""
import re 

S="hi today i have many work but i can handle , I am strong girl"
replace_S=re.sub("i","I",S)
print(S)
print("the txt after First alter ...")
print("-------------------------------")
print(replace_S)

print("-------------------------------")
replace_S=re.sub("\s","//",S,4)
print("the txt after seconde alter ...")
print(replace_S)

print("-------------------------------")

print("return results...")
Z=re.search("have",S)

print(Z)#$why the results is (11 ,15????  He found it in order number 11.
#The word we're looking for is over in 15th order,
# which is how it's made up of four characters.
print("-------------------------------")
st="The rain in Spain"
str=re.search(r"\bt\w+",S)#i need somr explain 
print(str)
print(str.string)
print(str.group())
#Why didn't he print the first word?