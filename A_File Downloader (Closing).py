import requests
import datetime
import os
import sys
import zipfile

pref = "B_"
ext = "bhav.csv.zip"
Start = input("Start downloading files ? y/n : ")# Safety feature to prevent accidental execution
mdict = {'01':'JAN','02':'FEB','03':'MAR','04':'APR','05':'MAY','06':'JUN','07':'JUL','08':'AUG','09':'SEP','10':'OCT','11':'NOV','12':'DEC'}
zip_fileslist = []
if Start == "y":
    empty_files = []
    a = list(range(32))
    date = a[1:]
    ask_month = input("Enter the number of months : ")
    if int(ask_month) < 13 and int(ask_month) > 0:
        b = list(range(int(ask_month)+1))
    else:
        sys.exit("Month not available")
    month = b[1:]
    ask_year = input("Enter the target year : ")
    year = int(ask_year)
    if year < 2015 or year > 2019:
        sys.exit("Year not available")
    files = 0
    errors = 0
    print ("Downloading...")
    for x in month:
        if x < 10:
            x = "0" + str(x)
        else:
            x = str(x)
        for y in date:
            if y < 10:
                y = "0" + str(y)
            else:
                y = str(y)
            qwe = str(year)
            name = y + mdict[x] + qwe + ext
            try:
                ck = datetime.date(year, int(x), int(y))  # Check for a weekend
                qq = ck.weekday()
                if qq > 4:
                    continue
                else:
                    url = "https://www.nseindia.com/content/historical/EQUITIES/"+qwe+"/"+mdict[x]+"/cm" + name
                    r = requests.get(url, allow_redirects=True)
                    open(pref + name, 'wb').write(r.content)
                    files += 1
                    pathx = "cm" + y + mdict[x] + qwe + "bhav.csv"
                    zip_obj = zipfile.ZipFile(pref+name, 'r')
                    zip_obj.extractall()
                    zip_obj.close()
                    filex = open(pathx, "r+")
                    content = filex.read()
                    empty = content.find("404 Not Found")
                    zip_fileslist.append(pref+name)
                    if empty != -1:
                        empty_files.append(pathx)
                        errors += 1
                    filex.close()
            except:
                continue
    print("Successfully Downloaded " + str(files) + " files ! ")
    ask_del = input("Deleting " + str(errors) + " error files and "+ str(len(zip_fileslist)) +" zip files. Press any key to proceed : ")
    for wrong in empty_files:
        os.remove(wrong)
    for wrongx in zip_fileslist:
        os.remove(wrongx)
    print("Task completed Successfully !")
else:
    print ("Task aborted.")