# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:31:06 2023

@author: dhanu
"""

ipstr=input("enter the string\n")
count=0
for i in range(len(ipstr)):
    if ipstr[i].isupper():
        count+=1
        print("character",ipstr[i],"is present in the position",i+1)
print("number of capital letters is:",count)