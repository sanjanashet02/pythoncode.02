# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:05:49 2023

@author: dhanu
"""

def binsearch(lst, key):
    low=0
    high=len(lst)-1
    while low <high:
        mid = (low+high)//2
        if key==lst[mid]:
            return mid+1
        elif key < lst[mid]:
            high=mid-1
        else:
            low = mid-1
    return -1

n=int(input("enter the number of elements\n"))
lst=[]

print("enter",n,"values\n")
for i in range(n):
    ele=int(input())
    lst.append(ele)
    
lst.sort(reverse=False)
print("the sorted list is:\n")
for i in lst:
    print(i,end=" ")
    
key=int(input("\n enter the key element:\n"))
pos=binsearch(lst,key)
if pos==-1:
    print("key not found")
else:
    print("key is found in the position:",pos)
      
            