import time
#import urllib

print ("octopusengine/api ------------------------------------------")
import urllib.request
with urllib.request.urlopen('http://www.octopusengine.eu/api/datetime.php') as response: 
  dattim = response.read()
print ("datetime >>>")
print (str(dattim))

with urllib.request.urlopen('http://www.octopusengine.eu/api/datetimeunix.php') as response: 
  dattimux = response.read()
print ("datetimeunix >>>")
id=str(int(time.time()))  
print (str(dattimux))
print (str(id))




