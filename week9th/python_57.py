import re
txt="Atheer Asmba osama And soso "
#A=re.search("^The. *spain$ ",txt) 
 
#if (A):
  #  print("True")
#else:
  #  print("False")
D=re.search("^Atheer.",txt)

#A=re.search(" *And",txt)
A=re.findall("[a-b]",txt)
# if (A,D):
  #  print("True")
#else:
 #   print("False")
# F=re.findall("\AThe",txt)
print(A) 
#print(F)

str = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\Aosama", txt)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")
