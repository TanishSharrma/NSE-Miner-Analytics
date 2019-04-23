import numpy
import pandas as pd
import datetime
import xlrd
import os


start_row = 772             # Set first value row (0,1,2....)  4 & 334
group_size = 5
last_row = 1485           # Second Latest Day's Available Data's last row 447
sheet_name = 0            # 0 for Gainers and 1 for Losers
year = "2017"
path = "A_Experiment_"+year+".xlsx"

data = pd.read_excel(path, sheet_name,None)
mdict = {'01':'JAN','02':'FEB','03':'MAR','04':'APR','05':'MAY','06':'JUN','07':'JUL','08':'AUG','09':'SEP','10':'OCT','11':'NOV','12':'DEC'}

filex = open("A_Temp.txt","r+")
for loop in range(start_row,last_row+1,group_size+1):
    iter = data.iloc[loop + 6]
    y = iter[1]
    date = str(y)[8:10]
    month = str(y)[5:7]
    file_path = "cm" + date + mdict[month] + year + "bhav.csv"
    df = pd.read_csv(file_path)
    df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', "M", 'O']
    for iterx in range(5):
        keyx = data.iloc[loop+iterx]
        key = keyx[2]
        if str(key) == "x":
            y = "0\t0\t0\t0"
        else:
            y = ""
            check = df.loc[df['A'] == str(key)]['B']
            x1 = df.loc[df['A'] == str(key)]['C']
            x2 = df.loc[df['A'] == str(key)]['D']
            x3 = df.loc[df['A'] == str(key)]['E']
            x4 = df.loc[df['A'] == str(key)]['F']
            if str(check.iloc[0]).find("EQ")!=-1:
                y = str(x1.iloc[0]) + "\t" + str(x2.iloc[0]) + "\t" + str(x3.iloc[0]) + "\t" + str(x4.iloc[0])
            else :
                y = str(x1.iloc[1]) + "\t" + str(x2.iloc[1]) + "\t" + str(x3.iloc[1]) + "\t" + str(x4.iloc[1])
        filex.write(y+"\n")
    filex.write("\n")
filex.close()