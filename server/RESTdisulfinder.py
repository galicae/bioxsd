from flask import Flask,request
import time
import subprocess
import os

app = Flask(__name__)

#creates a folder with th current time in ms and returns its name
def timeFolder(prefix):
	millis = str(int(round(time.time() * 1000)))
	folName = "/".join([prefix.rstrip("/"),millis])
	if not os.path.exists(folName):
		os.makedirs(folName)
	return folName

@app.route('/')
def hello():
	return "Hello World"

@app.route('/getDsBonds',methods=['POST'])
#handle getDsBonds request
def getDsBonds():
	#create tmp folders
	folder = timeFolder("tmp")
	os.makedirs(folder+"/out")
	
	#write fasta to file because disulfinder requires a file as input
	with open(folder+"/sequence.fasta","w+") as f:
		f.write(request.data)
	
	#call disulfinder
	shellCmd = " ".join(["disulfinder","-f",folder+"/sequence.fasta","-o",folder+"/out","-r",folder,"-d /data/uniprot_sprot","-c"])
	subprocess.call(shellCmd,shell=True)
	
	#retrieve output file 
	outFile = folder+"/out/" + list(os.listdir(folder+"/out"))[0]
	shellCmd = " ".join(["./disulfxml","-i",outFile,"-o",folder+"/sequence.xml"])
	subprocess.call(shellCmd,shell=True)
	
	#open xml output File and return contents
	with open(folder+"/sequence.xml") as f:
		out = f.read()
	return out

@app.route('/getVersion')	
def getVersion():
	p = subprocess.Popen("disulfinder --version",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	out,err = p.communicate()
	return err
	



if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
