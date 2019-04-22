# NSE-Miner-Analytics
Data miner and stocks analysis for NIFTY 50 companies listed on the NSE (National Stock Exchange - India)

# AIM
Trying to develop a profit making strategy/model using previous data.

# Current Strategy Attempted
Calculating if the strategy "Going long on Previous Day's Top 5 Gainers" works.

# Steps :
1) Download Old Gainers, Losers and Nifty from NSE website using data miner (A_File Downloader.py)
2) Sort out the data using (A_Raw Data.py). The extracted Data is saved in txt files for ease of Excel formatting. (To be done manually from txt to Excel, simple copy and paste)
3) Download Bhav files from NSE website using data miner (A_File Downloader (Closing).py)
4) Fetch company names and dates from Step 1 and return their next day's : 1) Opening 2) High 3) Low 4)Closing prices from files downloaded in Step 3 using
   (A_Closing Merge.py)

Any errors arising are from the inconsistent data format provided by NSE.
Used : Python, Pandas, Numpy, Excel


Intial Tests' Resultant Model (alpha) :

1) Long Top 5 Gainers with a Y leverage. 
2) Set Stop loss ~ Z (with respect to Y leverage)
3) Investment Intervals with provided margain ~ 30-33% <> 50-55% for large n
4) Exclude Stocks >8% gain in the previous day from data set
5) BUY : Execute Market order (within limits) during After Hours
6) SELL : Either sell 15 mins before closing or find max median (TBD)

To Check for:

1) Continuous Day patterns (2-3 days continuous of ups and downs have effect)
2) Company rucurssive habits (If specific companies have a pattern)
3) After hour trades effect (Open Price Calculate)
4) Calculate Stop Loss by taking Significant Mean for the lowest a "Gaining" stock dips in a day.
5) Correlation with the movement of NIFTY
6) Effects on specific days (Mondays, Before major holidays, Before and After dividents are paid out etc)
7) Test correlation between After Hour trend and daily trend