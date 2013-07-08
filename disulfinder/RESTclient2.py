import requests
from optparse import OptionParser
import sys

def main():
	parser = OptionParser()
	parser.add_option("-i","--input",dest="inFile")
	parser.add_option("-o","--output",dest="outFile")
	options,args = parser.parse_args()
	
	#define Web service URI
	serviceURI = "http://alex.tbl/webservice/disulfinder/RESTdisulfinder.php"

	#read fasta from file or stdin	
	if options.inFile != None:
		with open(options.inFile) as f:
			fasta = f.read()
	else:
		fasta = sys.stdin.read()

	#send fasta file per POST to Webservice
	res = requests.post(serviceURI+"/getDsBonds",fasta)
	#retrieve content
	msg = res.content
	#write to file
	with open(options.outFile,"w+") as f:
		f.write(msg)
	

if __name__ == "__main__":
	main()
