import time,os

#os.system("clear") 

print("pokus 123")
for i in range(9):
  for j in range(9):	
	  os.system("clear")
	  print("+---+---+---+") 
	  print("! "+str(i)+" !   ! "+str(j)+" !")
	  print("+---+---+---+")
	  if (i+j==10):
		  k="*"
	  else:
		  k=" "	 
	  print("!   ! "+str(k)+" !   !") 
	  print("+---+---+---+") 
	
	  time.sleep(0.1)

def getIp():
   try:
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1]
   except:
     ipaddr ="ip.Err"
   #print "ip: " ip
   return ipaddr

#====== get procesor temp ============================
def getProcTemp():  
   try:
     pytemp = subprocess.check_output(['vcgencmd', 'measure_temp'], universal_newlines=True)
     #ipoutput = subprocess.check_output(['vcgencmd measure_temp'], universal_newlines=True, 'w'))
     #print pytemp 
     eq_index = pytemp.find('=')+1 
     #if eq_index>0:
     var_name = pytemp[:eq_index].strip()
     value = pytemp[eq_index:eq_index+4]
     numvalue=float(value)
   except:
     numvalue = -1
   return numvalue 


print (getProcTemp())
print (getIp())
