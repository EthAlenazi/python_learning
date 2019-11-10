# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:40:43 2019

@author: ETH
"""
print("Enter your name to continue")
name = input()

txt="hello {} welcom dack io our small program !!"

print (txt.format(name))

price = 25

Price="this price is {:.2f} SAR , Dear {} you can bay now  "

print(Price.format(price , name))
