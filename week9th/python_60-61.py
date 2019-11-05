import json
import re 

print("Question (1):")
tuble = ["Monday","Tuesday","wednesday",
         "thursday","Friday","saterday.",
         "sunday"]
Data=json.dumps(tuble)
print("the result with out format:")
print(Data)
print("-----------------------------")
print("after formatted")
print(json.dumps(tuble,indent=4))
print("----------------------------")
print("Question (2):")
txt="data is the new oil"
S=re.search("data",txt)
print(S)
if (S):
    print("yes we found it ")
else:
    print("sorry not found it !")
