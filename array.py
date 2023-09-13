# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:58:12 2023

@author: dhanu
"""

def read(lst , n):
    print("enter",n,"values:")
    for i in range(n):
        ele=int(input())
        lst.append(ele)
        
def display(lst):
    for i in lst:
        print(i , end=" ")
        
def findcount(lst):
    ecount=ocount=0
    for i in lst:
        if i%2==0:
            ecount+=1
        else:
            ocount+=1
    return ecount , ocount

lst1=[]
lst2=[]

n1=int(input("enter list 1 size:"))
read(lst1 , n1)
n2=int(input("enter list 2 size:"))
read(lst2 , n2)

print("elements of list 1 are:\n\n")
display(lst1)
print("\n\nelements of list 2 are:\n\n")
display(lst2)

ecount1,ocount1=findcount(lst1)
ecount2,ocount2=findcount(lst2)
if ecount1==ecount2 and ocount1==ocount2:
    print("\n\nsymmetrical\n\n")
else:
    print("not symmetrical\n\n")



        
