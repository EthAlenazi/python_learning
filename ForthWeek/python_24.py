Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt={'Name':'Atheer','Age':23}
>>> print(txt)
{'Name': 'Atheer', 'Age': 23}
>>> Information=txt.copy()
>>> print(Information)
{'Name': 'Atheer', 'Age': 23}
>>> myData=dict(txt)
>>> print(myData)
{'Name': 'Atheer', 'Age': 23}
>>> mycode = { 'classA' :{'A':202,'B':205},'classB':{'B':205,'C':207}, 'classC':{'C':207,'D':206}}
>>> print (mycode)
{'classA': {'A': 202, 'B': 205}, 'classB': {'B': 205, 'C': 207}, 'classC': {'C': 207, 'D': 206}}
>>> -IT381 = {'MID1':00,'MID2':00}
SyntaxError: can't assign to operator
>>> IT381 = {'MID1':00,'MID2':00}
>>> #the error was ( - ) in the beginning
>>> IT341 = {'MID1':'**','MID2':'**'}
>>> subject = {'IT381':IT381,'IT341':IT341}
>>> PRINT(subject)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    PRINT(subject)
NameError: name 'PRINT' is not defined
>>> print(subject)
{'IT381': {'MID1': 0, 'MID2': 0}, 'IT341': {'MID1': '**', 'MID2': '**'}}
>>> Doc!=dict(brand='ford',model='000',year=1997)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Doc!=dict(brand='ford',model='000',year=1997)
NameError: name 'Doc' is not defined
>>> Doc1=dict(brand='ford',model='000',year=1997)
>>> print(Doc1)
{'brand': 'ford', 'model': '000', 'year': 1997}
>>> Doc1.clear()
>>> print
<built-in function print>
>>> print(Doc1)
{}
>>> 
