import time
import urllib.request
import json

# jObj = json.loads(urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read())

with urllib.request.urlopen("https://www.bitstamp.net/api/ticker/") as response: 
    btcbit = response.read()
    print (str(btcbit))

jObj = json.loads(btcbit)
lastNum =int(float(jObj["last"]))
print("last BTC/USD price:")
print(lastNum)





