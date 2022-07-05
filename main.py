from mcstatus import JavaServer
#from replit import db
import socket

#import thread
import threading
import time

import json

#from web import keep_alive
#from web import setThredsValue
import time
import sys, getopt

rmthred = 0

def check(host,port,timeout=2):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #presumably 
    sock.settimeout(timeout)
    try:
       sock.connect((host,port))
    except:
       return False
    else:
       sock.close()
       return True

#print(check('google.com',443,timeout=1))


class McServer:
  def __init__(self, host, software, plugins, motd, players, playercount, maxplayers, version):
    self.host = host
    self.software = software
    self.plugins = plugins
    self.motd = motd
    self.players = players
    self.playercount = playercount
    self.maxplayers = maxplayers
    self.version = version
    


import subprocess
#import uuid

def ChackServerInfo(ip,port,nextone):
  if check(ip,port,timeout):
    #mcstatus 217.144.53.54:25565 json
    myip = f"{ip}:{port}"
    result = subprocess.run(['mcstatus', myip ,'json'], stdout=subprocess.PIPE)
    json_string = json.dumps(result.stdout.decode('utf-8'))
    
    print(json_string)
    
    json_string = json_string[1:len(json_string)-3]

    json_string = json_string.replace('\\"','"')
    
    print(f"Json sting: \n {json_string} \n\n")
    
    print("The type of object is: ", type(json_string))
    ###
    stud_obj = json.loads(json_string)

    print(type(stud_obj))

    #name = f"servers/{str(uuid.uuid4())}_{ip}.json"
    name = f"servers/_{ip}:{port}.json"
    #db['saved_scane'] = name

    with open(name, "w") as outfile:
      json.dump(stud_obj, outfile)
    
    
    
  else:
    print(f"can not connect to {ip} on port {port}! ")

  if not nextone == None:
    nextone()


    
def nextIp():
  ipparts = ip.split('.')
  dig = []
  for x in ipparts:
    dig.append(int(x))
  
  if dig[3] + 1 < 256:
    dig[3] += 1
  else:
    dig[3] = 0
    if dig[2] + 1 < 256:
      dig[2] += 1
    else:
      dig[2] = 0
      if dig[1] + 1 < 256:
        dig[1] += 1
      else:
        dig[1] = 0
        if dig[0] +1 < 256:
          dig[0] += 1
        else:
          return "error"
  outstring = ""
  for x in dig:
    outstring += str(x) + "."
  outstring = outstring[0:len(outstring)-1]

  return outstring


def startnewThred():
  global ip
  global rmthred
  if rmthred > 0:
    try:
      time.sleep(0.1)
      t1 = threading.Thread(target=ChackServerInfo, args=(ip,port,startnewThred,))
      t1.start()
      threds.append(t1)
      ip = nextIp()
      rmthred -= 1
      return True
    except:
      print (f"Error: unable to start thread in loop index: {str(i)}")
      return False
  

def Main(ip,port,runtime):
  print("Start running code...")
  if runtime <= maxthred:
    for i in range(runtime):
      try:
         t1 = threading.Thread(target=ChackServerInfo, args=(ip,port,None,))
         t1.start()
          
         threds.append(t1)
      except:
        print (f"Error: unable to start thread in loop index: {str(i)}") 
        ip = nextIp()
      print(f"Run index: {str(i)}.")
  else:
    for i in range(maxthred):
      if startnewThred():
        print(f"Run index: {str(i)}.")
      
def logger():
  while 1 == 1:
    time.sleep(3)
    #setThredsValue(threds)
    print("rm threds: ")
    print(rmthred)
    if rmthred <= 0:
      for t in threds:
        if t.is_alive:
          print("stop thred" + str(t))
          #t._stop()
          
      break

#--------- config -----------

startIp = "93.63.33.168"#"51.222.93.22" #25606
port = 25565
timeout = 30
maxthred = 255
runtime = 3000000

#-------- end config ---------

ip = startIp


threds = []

#---------- start ----------

if __name__ == "__main__":
  startArgs = sys.argv[1:]
  try:
    opts, args = getopt.getopt(startArgs,"hip:p:t:th:rt",["ip=","port=","timeout=","thred=","runtime="])
  except getopt.GetoptError:
    print ('test.py -i <ip> -p <port> -t <timeout> -th <thred> -rt <runtime>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('test.py -i <ip> -p <port> -t <timeout> -th <thred> -rt <runtime>')
  
      sys.exit()
    elif opt in ("-i", "--ip"):
      ip = str(arg)
    elif opt in ("-p", "--port"):
      port = int(arg)
    elif opt in ("-t", "--timeout"):
      timeout = int(arg)
    elif opt in ("-th", "--thred"):
      maxthred = int(arg)
    elif opt in ("-rt", "--runtime"):
      runtime = int(arg)
  #keep_alive()

  rmthred = runtime

  Main(ip,port,runtime)
  logger()

# for i in range(100):
#   print(ip)
#   ip = nextIp()
  
#ChackServerInfo(startIp,port)  



print("Finised")

