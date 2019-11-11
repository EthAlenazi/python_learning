# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:40:43 2019

@author: ETH
"""
print("Enter your name to continue")
name = "waleed"#input()

txt="hello {0} welcom dack io our small program !!"

print (txt.format(name))
star="***"
price = 25

Price="this price is {0:.2f} SAR ,Dear {1}{2}{1} you can bay now  "

print(Price.format(price ,star, name))
#Named Indexes
our_proudect="i have {Pr1},also i have a litile of {Pr2}"
print ("hello Ahmed today i want to show our prodect /", our_proudect.format(Pr1="***",Pr2="###"))