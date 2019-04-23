import numpy as np
import pandas as pd
import datetime
import xlrd
import os
import math

top = 5
stop_loss = -0.01
upper_limit = 8
lev = 50
bank = 28000
investx = 25000

data = pd.read_excel("A_Experiment_2017.xlsx", 0,None)
datax = pd.read_excel("A_Experiment_2017.xlsx", 2,None)

start_row = 4          # Set first value row (0,1,2....)  4 & 334
group_size = 5
last_row = 1485         # 2017 : 1485 , 2018 : 1473 , 2019 : 447


arr = []
for loop in range(start_row,last_row+1,group_size+1):
    for rn in range(top):
        iter = data.iloc[loop+rn]
        y = iter[14]
        j = iter[6]
        q = iter[16]
        if not math.isnan(float(y)):
            if float(j) <= upper_limit:
                if float(q) < stop_loss:
                    y = stop_loss
            else:
                y = 0
        else:
            y = 0
        arr.append(float(y))
xw = np.array(arr)
#Practical
daily = []
rx = []
day = 0
for val in range(0,len(xw),top):
    invest = bank
    cap = invest * lev
    gl = 0
    for xp in range(top):
        gl += xw[val+xp]
    res = (cap*(gl/top))/100
    bank += res
    day += 1
    daily.append(str(day) + " : "+ str(bank))
    rx.append(str(res))
dp = np.array(daily)

#print (xw)
print (sum(xw)*(lev/top))
print (dp)