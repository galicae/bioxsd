import requests
from optparse import OptionParser
from lxml.builder import ElementMaker
from lxml import etree as et


def wrapFasta(fasta):
	DI = "http://rostlab.org/disulfinder/input"
        XSI = "http://www.w3.org/2001/XMLSchema-instance"
	WSDL_MSG = "http://alex.tbl/webservice/disulfinder"	
	NS_MAP = {"di": DI, "xsi": XSI , "msg" : WSDL_MSG}
	DI = ElementMaker(namespace = DI, nsmap = NS_MAP)
	MSG = ElementMaker(namespace= WSDL_MSG, nsmap = NS_MAP)
	with open(fasta) as f:
		seq = f.read()
	mydoc = MSG.getDisulfinderRequest(DI.sequence(seq))
	return mydoc

def main():
	parser = OptionParser()

	parser.add_option("-i","--input",dest="inFile")
	parser.add_option("-o","--output",dest="outFile")

	options,args = parser.parse_args()
	seqWrap = wrapFasta(options.inFile)
	res = requests.post("http://alex.tbl/webservice/disulfinder/RESTdisulfinder.php/getDsBonds",et.tostring(seqWrap))
	msg = et.fromstring(res.content)
	xmlDoc = list(msg.iter())[1]
	with open(options.outFile,"w+") as f:
		
		f.write(et.tostring(xmlDoc,pretty_print=True))
	


if __name__ == "__main__":
	main()
