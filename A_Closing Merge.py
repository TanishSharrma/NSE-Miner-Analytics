import numpy
import pandas as pd
import datetime
import xlrd
import os


start_row = 4             # Set first value row (0,1,2....)  4 & 334
group_size = 5
last_row = 1473           # Second Latest Day's Available Data's last row 447
sheet_name = 0            # 0 for Gainers and 1 for Losers
year = "2018"
path = "A_Experiment_"+year+".xlsx"

data = pd.read_excel(path, sheet_name,None)

filex = open("A_Temp.txt","r+")
for loop in range(start_row,last_row+1,group_size+1):
    iter = data.iloc[loop + 6]
    y = iter[1]
    date = str(y)[8:10]
    month = str(y)[5:7]
    file_path = "C_" + date + month + year + ".CSV"
    df = pd.read_csv(file_path)
    df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for iterx in range(5):
        keyx = data.iloc[loop+iterx]
        key = keyx[2]
        if str(key) == "x":
            y = "0"
        else:
            x = df.loc[df['B'] == str(key)]['C']
            y = x.iloc[0]
        filex.write(str(y)+"\n")
    filex.write("\n")
filex.close()