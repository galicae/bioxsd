from optparse import OptionParser
from collections import defaultdict
from lxml import etree as et

parser = OptionParser()

parser.add_option("-i","--input",dest="inFile",
                help="disulfinder ascii output file")
parser.add_option("-o","--output",dest="outFile",
                help="BioXSD conform XML version of the disulfinder output")

options,args = parser.parse_args()

#doto: read from stdin
def parseDisulfinder(inFile):

	data= defaultdict(list)
	with open(inFile) as f:
        	for line in f:
			if line.startswith("Abbreviations"):
				break
                	if line.startswith("AA"):
                        	data['AA'].extend(list(line.split()[1].strip()))
                	if line.startswith("DB_state") or line.startswith("DB_conf") or line.startswith("DB_flip"):
                        	content = line.strip("\n")
                        	lIdent = content[:9].strip()
                        	lData = content[9:]
                        	data[lIdent].extend(list(lData))
                        	#print lIdent
                        	#print lData

#for key in ["AA","DB_state","DB_conf","DB_flip"]:
#	print key
#	print "".join(data[key])
#	print len(data[key])

def writeBioXSD(data):
	#constants
		DI = "http://rostlab.org/disulfinder/output"
		BX = "http://bioxsd.org/BioXSD-1.1"
		XSI = "http://www.w3.org/2001/XMLSchema-instance"

	#build xml tree
	rootname = et.QName(DI,"disulfOutput")
