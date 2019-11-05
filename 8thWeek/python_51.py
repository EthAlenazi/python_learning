import platform 
import mod as Dex

A = Dex.personl["age"]
print(A)
x = platform.system()
print(x)

print(platform.python_version())
Q =dir(platform)
print(Q)


Q1 =dir(Dex)
print(Q1)
print("----------------------------------")
print("the age is :")
print(Dex.personl["age"])
