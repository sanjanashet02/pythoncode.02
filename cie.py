# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:13:19 2023

@author: dhanu
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('semcie.csv')
avgsrs=pd.Series()
for i in range(1,len(df.columns),2):
    code=df.columns[i][:5]
    value=(df.iloc[::,1].mean()+df.iloc[::,i+1].mean())/2
    avgsrs[code]=value
print("highest average value is:",avgsrs.max())
print("subject code with highest average is:",avgsrs.idxmax())

avgcie=df.iloc[::,1::2].mean(axis=1)
avgsee=df.iloc[::,2::2].mean(axis=1)

#plotting graph
x1=[]
x2=[]
ticks=[]
w=0.2 
for i in range(len(df.index)):
    x1.append(i)
    x2.append(i+w)
    ticks.append(i+w/2)
plt.figure(figsize=(10,8))
plt.bar(x1,avgcie,width=w,color='r',label="CIE")
plt.bar(x2,avgsee,width=w,color='g',label="SEE")
plt.xticks(ticks,df['USN'])
plt.legend()
plt.xlabel("STUDENTS USN")   
plt.ylabel("CIE AND SEE SCORE")
plt.title("STUDENTS PERFORMANCE ON CIE AND SEE")
plt.show()     

