from nsetools import Nse
nse = Nse()
q = nse.get_quote("infy")
p = q['lastPrice']
print (p)