from flask import Flask
from flask import send_file
from threading import Thread
from replit import db
from os import walk
import zipfile

path = "servers/"

app = Flask('')

@app.route('/')
def home():
  
  # mystrin = "<h1> hello </h1> <ul> " 
  # filenames = next(walk(path))
  # print(f"File names: {filenames[2]}")
  # for fln in filenames[2]:
  #   #print(fln)
  #   mystrin += f"<li><a href=\"{str(fln)}\">{str(fln)}</a></li>"
  # mystrin += "</ul>"
  # return mystrin

  return "<a href=\"/download\">dw</a>"

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
  filenames = next(walk("servers/"))
  with zipfile.ZipFile("dw/servers.zip", mode="w") as archive:
    for fln in filenames[2]:
      archive.write(f"servers/{fln}")
  path = "dw/servers.zip"
  return send_file(path, as_attachment=True)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()