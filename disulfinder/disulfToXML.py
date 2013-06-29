from optparse import OptionParser
from collections import defaultdict
from lxml import etree as et
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
	return data

#for key in ["AA","DB_state","DB_conf","DB_flip"]:
#	print key
#	print "".join(data[key])
#	print len(data[key])

def getContentIds(data):
	res = []
	for i,db in enumerate(data['DB_state']):
		if db != " ":
			res.append(i)
	return res

def writeOcc(node,data,id):
	XSI = "http://www.w3.org/2001/XMLSchema-instance"
	occ = et.subElement(node,bxNode("occurence")) 
	pos = et.subElement(occ,bxNode("position"))
	pos.set(et.QName(XSI,type),"bx:SequencePosition")
	pnt = et.subElement(pos,bxNode("point"))
	pnt.set("pos",str(id))
	pnt.set(et.QName(XSI,type),"bx:SequencePoint")
	for score in ["DB_state","DB_conf","DB_flip"]:
		sNode = et.subElement(occ,bxNode("score")) 
	 	sNode.set("scoreTypeIdRef","S#"+score)
		sNode.set("value",str(data[score][i]))

def bxNode(name):
	return "{%s}%s" % ("http://bioxsd.org/BioXSD-1.1",name)

def writeBioXSD(data,outName):
	#constants
	DI = "http://rostlab.org/disulfinder/output"
	BX = "http://bioxsd.org/BioXSD-1.1"
	XSI = "http://www.w3.org/2001/XMLSchema-instance"
	
	ns_map = { "di" : DI, "bx" : BX, "xsi": XSI }
	#build xml tree

	eStub = "{%s}%s"

	#create root element
	#rootname = et.QName(DI,"disulfideBridgePrediction")
	rootname = eStub % (DI,"disulfideBridgePrediction")
	root = et.Element(rootname, nsmap = ns_map)
	
	#create sequence reference record
	refSeq = et.SubElement(root,eStub % (BX,"referenceSequence"))	
	seqRec = et.SubElement(refSeq,eStub % (BX, "sequenceRecord"))
	seqRec.set(et.QName(XSI,"type"), "bx:GeneralAminoacidSequenceRecord")
	seq = et.SubElement(refSeq,eStub % (BX,"sequence"))
	seq.text = "".join(data['AA'])
	
	#create
	occRef = et.SubElement(root,eStub % (BX, "blockWithOccurrenceReferences"))
	meth = et.SubElement(occRef,eStub % (BX, "method"))
	meth.set("localID","M#di")
	meth.set("name","disulfinder")
	et.SubElement(meth,eStub % (BX,"citation"), date="2013-6-28")
	
	#category = et.SubElement(meth,eStub % (BX,"categoryConcept"))
	#category.set("accession","operation_1850")
	#category.set("conceptURI","http://edamontology.org/operation_1850")
	#category.set("ontologyName","EDAM")
	#category.set("term","Protein cysteine and disulfide bond assignment")
	
	#et.subElement(occRef, eStub % (BX,"scoreType"), localId="S#DB_state")
	#et.subElement(occRef, eStub % (BX,"scoreType"), localId="S#DB_conf")
	#et.subElement(occRef, eStub % (BX,"scoreType"), localId="S#DB_flip")
	
	#ann = et.subElement(occRef, eStub % (BX,"annotation"))
	#feat = et.subElement(ann, eStub % (BX, "feature"))
	#featName = et.subElement(feat, eStub % (BX,"name"))
	#featName.text = "Disulfide bridge and cystein connectivity prediction"
	#evtlInsert equalConcept
	
	#cRef = et.subElement(ann, eStub % ( BX, "condensedReferences"))
	#midRef = et.subElement(cRef, eStub %( BX, "methodIdRef"))
	#midRef.text = "M#di"
	
	disulfIDs = getContentIds(data)
	
	#for did in disulfIDs:
		

	#write XML to file
	tree = et.ElementTree(root)
	tree.write(outName)
	

def main():
	parser = OptionParser()

	parser.add_option("-i","--input",dest="inFile",
        	        help="disulfinder ascii output file")
	parser.add_option("-o","--output",dest="outFile",
        	        help="BioXSD conform XML version of the disulfinder output")

	options,args = parser.parse_args()

	data = parseDisulfinder(options.inFile)
	writeBioXSD(data,options.outFile)


if __name__ == "__main__":
	main()
