from optparse import OptionParser
from collections import defaultdict
from lxml.builder import ElementMaker
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

def writeBXD(data,outFile):
	DI = "http://rostlab.org/disulfinder/output"
	BX = "http://bioxsd.org/BioXSD-1.1"
	XSI = "http://www.w3.org/2001/XMLSchema-instance"
	XS = "{%s}" % XSI
	NS_MAP = {"di": DI, "bx": BX, "xsi": XSI}
	
	E = ElementMaker(namespace=BX, nsmap = NS_MAP)
	DI = ElementMaker(namespace = DI, nsmap = NS_MAP)
	
	channel = E.annotation(
                        E.feature(),
                        E.condensedReferences(
                                E.methodIDRef("M#di")
                        )
                )



	for dsID in getContentIds(data):
		item = E.occurence(
			E.position(
				E.point({"pos" : str(dsID), XS + "type" : "bxSequencePoint"}),
				{ XS + "type" : "bxSequencePosition"}
			),
			E.score(
				scoreTypeIdRef="S#DB_state",value=str(data['DB_state'][dsID])
			),
			E.score(
				scoreTypeIdRef="S#DB_conf",value=str(data['DB_conf'][dsID])
			),
			E.score(
				scoreTypeIdRef="S#DB_flip",value=str(data['DB_flip'][dsID])
			)
		)
		channel.append(item)



	mydoc = DI.disulfideBridgePrediction(
	E.referenceSequence(
		E.sequenceRecord(
			E.sequence("".join(data['AA'])),{XS+"type" : "bx:GeneralAminoacidSequenceRecord"  }
		)
	),
        E.blockWithOccurenceReferences(
                E.method(
                        E.categoryConcept({
				"accession" : "operation_1850",
				"conceptURI" : "http://edamontology.org/operation_1850",
				"ontologyName" : "EDAM",
				"term" : "Protein cysteine and disulfide bond assignment"
			}),
                        E.citation(date="2013-06-28"),
			localId="M#di",name="disulfinder"
                ),
                E.scoreType(localId="S#DB_stat"),
                E.scoreType(localId="S#DB_conf"),
                E.scoreType(localId="S#DB_flip"),
                
                channel
                
        )

	)
	
	with open(outFile,"w+") as outF:
		outF.write(et.tostring(mydoc, pretty_print=True))



def main():
	parser = OptionParser()

	parser.add_option("-i","--input",dest="inFile",
        	        help="disulfinder ascii output file")
	parser.add_option("-o","--output",dest="outFile",
        	        help="BioXSD conform XML version of the disulfinder output")

	options,args = parser.parse_args()

	data = parseDisulfinder(options.inFile)
	writeBXD(data,options.outFile)


if __name__ == "__main__":
	main()

