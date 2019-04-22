import requests
import datetime
import os
import sys

Start = input("Start downloading files ? y/n : ")
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
            name = "MA" + y + x + qwe[2:] + ".csv"
            try:
                ck = datetime.date(year, int(x), int(y))  # Check for a weekend
                qq = ck.weekday()
                if qq > 4:
                    continue
                else:
                    url = "https://www.nseindia.com/archives/equities/mkt/" + name
                    r = requests.get(url, allow_redirects=True)
                    open(name, 'wb').write(r.content)
                    files += 1
                    filex = open(name, "r+")
                    content = filex.read()
                    empty = content.find("404 Not Found")
                    if empty != -1:
                        empty_files.append(name)
                        errors += 1
                    filex.close()
            except:
                continue

    print("Successfully Downloaded " + str(files) + " files ! ")
    ask_del = input("Deleting " + str(errors) + " error files. Press any key to proceed : ")
    for wrong in empty_files:
        os.remove(wrong)
    print("Task completed Successfully !")
else:
    print ("Task aborted.")