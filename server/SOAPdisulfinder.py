from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
import time
import subprocess
import os

def timeFolder(prefix):
	millis = str(int(round(time.time() * 1000)))
	folName = "/".join([prefix.rstrip("/"),millis])
	if not os.path.exists(folName):
		os.makedirs(folName)
	return folName


def getDsBonds(getDisulfinderRequest):
	folder = timeFolder("tmp")
	os.makedirs(folder+"/out")
	with open(folder+"/sequence.fasta","w+") as f:
		f.write(getDisulfinderRequest)
	shellCmd = " ".join(["disulfinder","-f",folder+"/sequence.fasta","-o",folder+"/out","-r",folder,"-d /data/uniprot_sprot","-c"])
	subprocess.call(shellCmd,shell=True)
	outFile = folder+"/out/" + list(os.listdir(folder+"/out"))[0]
	shellCmd = " ".join(["./disulfxml","-i",outFile,"-o",folder+"/sequence.xml"])
	subprocess.call(shellCmd,shell=True)
	with open(folder+"/sequence.xml") as f:
		out = f.read()
	return out	
	

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://alex.tbl/webservice/disulfinder/disulfinder_soap.wsdl", prefix="di",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('GetDsBonds', getDsBonds,
    returns={'getDisulfinderResponse': str}, 
    args={'getDisulfinderRequest' : str})

print "Starting server..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
