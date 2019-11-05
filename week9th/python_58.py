import re 

data="hello this is my txt just i have to say myself keep going "

A=re.findall('is',data)

print(A)
print("-------------------------") 
a=re.findall('its',data)
print(a)
if (a):
    print("yes, there is match! ")
else:
    print("sorry, not found!")

print("-------------------------") 
Q=re.search('\s',data)
print("this is first white space the program found =", Q.start()) #why the resuit is 5?   
print("-------------------------") 
Z=re.search("program",data)
print(Z)

W=re.split('\s',data)
print(W)
