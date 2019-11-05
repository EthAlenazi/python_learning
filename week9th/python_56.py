import json
#som of example:

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
#converAll=json.dumps(AllDataType,indent =4)   
print(json.dumps(AllDataType,indent =4,separators=("**","//"),sort_keys=True))     
    
  


