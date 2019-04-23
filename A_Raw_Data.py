import numpy
import pandas as pd
import os

skip = 91
date = [[],[],[],[],[],[],[],[],[],[],[],[]]
a = list(range(13))
month = a[1:]
year = 17
file_name = []

for root, dirs, files in os.walk("."):
    for filename in files:
        name = str(filename)
        if name[-4:]==".csv":
            file_name.append(filename)
for nx in file_name:
    d_m = nx[4:6]
    d_mw = nx[2:4]
    ddjy = nx[6:8]
    ddjx = nx[:2]
    if str (ddjx) == "MA" and str(ddjy)== str(year):
        date[int(d_m)-1].append(int(d_mw))

#NIFTY
filex = open("A_Nifty.txt","r+")
mct = 0
for y in month:
    datex = date[y-1]
    if len(datex) == 0:
        continue
    if int(y) < 10:
        y = "0" + str(y)
    for x in datex:
        if int(x) < 10:
            x = "0" + str(x)
        path = "MA" + str(x) + str(y) + str(year) + ".csv"
        data = pd.read_csv(path, skiprows=8)
        xr = data.iloc[0]
        j = xr.to_string(index=False)
        j = j.replace("\n", "\t")
        new = "\n" + str(y) + "/" + str(x) + "\t" + j.strip()
        filex.write(new)
filex.close()

#GAINERS
filex = open("A_Gainers.txt","r+")
for y in month:
    datex = date[y-1]
    if len(datex) == 0:
        continue
    if int(y) < 10:
        y = "0" + str(y)
    for x in datex:
        if int(x) < 10:
            x = "0" + str(x)
        path = "MA" + str(x) + str(y) + str(year) + ".csv"
        data = pd.read_csv(path, skiprows=skip)
        for i in range(5):
            xr = data.iloc[i]
            j = xr.to_string(index=False)
            j = j.replace("\n", "\t")
            j = j[15:]
            new = "\n" + str(y) + "/" + str(x) + "\t" + j.strip()
            filex.write(new)
        filex.write("\n")
filex.close()

#Losers
filex = open("A_Losers.txt","r+")
for y in month:
    datex = date[y - 1]
    if len(datex) == 0:
        continue
    if int(y) < 10:
        y = "0" + str(y)
    for x in datex:
        if int(x) < 10:
            x = "0" + str(x)
        path = "MA" + str(x) + str(y) + str(year) + ".csv"
        data = pd.read_csv(path, skiprows=skip+8)
        for i in range(5):
            xr = data.iloc[i]
            j = xr.to_string(index=False)
            j = j.replace("\n", "\t")
            j = j[15:]
            new = "\n" + str(y) + "/" + str(x) + "\t" + j.strip()
            filex.write(new)
        filex.write("\n")
    mct+=1
filex.close()