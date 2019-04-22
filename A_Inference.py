import numpy as np
import pandas as pd
import datetime
import xlrd
import os

data = pd.read_excel("A_Experiment_2018.xlsx", 0,None)
datax = pd.read_excel("A_Experiment_2018.xlsx", 2,None)

start_row = 4          # Set first value row (0,1,2....)  4 & 334
group_size = 5
last_row = 1473         # 2018 : 1473 , 2019 : 447
top = 5


arr = []
pl = 5
for loop in range(start_row,last_row+1,group_size+1):
    for rn in range(top):
        iter = data.iloc[loop+rn]
        y = iter[10]
        j = iter[6]
        if float(j) <= 8:
            if float(y) < -0.7:
                y = -0.7
            arr.append(float(y))
    pl += 1

xw = np.array(arr)

print (len(xw))
print (sum(xw))

'''
#Practical

bank = 15000
investx = 10000
t = 0
daily = []
rx = []
day = 0
for val in range(0,len(xw),5):
    if bank > investx:
        invest = investx
    else:
        invest = bank
    lev = 10
    cap = invest * lev
    gl = xw[val]+xw[val+1]+xw[val+2]+xw[val+3]+xw[val+4]
    res = (cap*gl)/100
    bank += res
    day += 1
    daily.append(str(day) + " : "+ str(bank))
    rx.append(str(res))
    if t==0:
        if bank > 30000:
            investx = 20000
            t += 1
    elif t==1:
        if bank > 50000:
            investx = 35000
            t += 1
    elif t==2:
        if bank > 100000:
            investx = 60000
            t += 1
    elif t==3:
        if bank > 150000:
            investx = 90000
            t += 1
    elif t==4:
        if bank > 230000:
            investx = 150000
            t += 1
    elif t==5:
        if bank > 310000:
            investx = 210000
            t += 1
    elif t==6:
        if bank > 400000:
            investx = 250000
            t += 1
    elif t==7:
        if bank > 550000:
            investx = 300000
            t += 1

dp = pd.array(daily)

print (dp)



'''