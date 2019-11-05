# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:55:40 2019

@author: ETH
"""

import json
#some Json :
X = '{"name ":"Atheer",   "age":"24",  "id":"436005128", "marks":"20"}'
#dicitionary object in python 
A = {"name ":"Atheer",  
     "age":"24", 
     "id":"436005128",
     "marks":"20"}
#convert 
Z = json.loads(X)
 #print as python dictionary:
print (Z["age"])
#convert to json :
Q= json.dumps(A)
#print rssult as json string :
print("the result of conver is /")
print("---------------  ")
print(Q)
#som of example:
print("------------------------------------------")
print("some of expretion")
print(json.dumps({"name":"Ali","Age":"23"}))
print(json.dumps(["Nada","Ali","Abeer","Anhar"]))
print(json.dumps(("Nada","Ali","Abeer","Anhar")))
print(json.dumps("Hello"))
print(json.dumps(24))
print(json.dumps(24.32))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#Convert a Python object containing all the legal data types:
AllDataType={
        "name":"john",
        "age":30,
        "married":True,
        "divorced":False,
        "children":("Ann","Billy"),
        "pest":"None",
        "Cars":[{"Model":"BMW230","mpg":27.5},
                {"Model":"Ford Edge","mpg":21.1}
                ]}

print("-------------------------------------")      
print("this is all data after coner " )
print("-------------------------------------")        
converAll=json.dumps(AllDataType)   
print(converAll)     
    
  


