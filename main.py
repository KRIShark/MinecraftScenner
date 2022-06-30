from mcstatus import JavaServer
from replit import db
import socket

#import thread
import threading
import time

import json

from web import keep_alive

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
import uuid

def ChackServerInfo(ip,port):
  if check(ip,port,timeout):
    
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

    name = f"servers/{str(uuid.uuid4())}_{ip}.json"
    db['saved_scane'] = name

    with open(name, "w") as outfile:
      json.dump(stud_obj, outfile)
    
    
    
  else:
    print(f"can not connect to {ip} on port {port}! ")


    
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


startIp = "8.8.8.8"
port = 25565
timeout = 10

ip = startIp

runtime = 0

threds = []


keep_alive()


  
for i in range(runtime):
  try:
     t1 = threading.Thread(target=ChackServerInfo, args=(ip,port,))
     t1.start()
     threds.append(t1)
  except:
    print (f"Error: unable to start thread in loop index: {str(i)}") 
  ip = nextIp()
  print(f"Run index: {str(i)}.")


# for i in range(100):
#   print(ip)
#   ip = nextIp()
  
#ChackServerInfo(startIp,port)  

print("Finised")