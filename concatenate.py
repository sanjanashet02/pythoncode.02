# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:52:58 2023

@author: dhanu
"""
str1=input("enter the string\n")
str2=input("enter the string\n")
str3=" "

for ch in str1+str2:
    if ch.isupper():
        str3=str3+ch
        
print("string 1 is",str1)
print("string 2 is:",str2)
print("concatenated string is:",str3)