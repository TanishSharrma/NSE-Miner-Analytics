'''

import pandas as pd

date = "02"
month = "01"
year = "2019"
file_path = "C_" + date + month + year + ".CSV"
df = pd.read_csv(file_path)
df.columns = ['A','B','C','D','E','F','G','H']
key = "TCI"
x = df.loc[df['B'] == key]['C']
y = x.iloc[0]
'''


nq = "B_01JAN2019bhav.csv.zip"


import zipfile

path = "B_01JAN2019bhav.csv.zip"
zip_obj = zipfile.ZipFile(path, 'r')
zip_obj.extractall()
zip_obj.close()