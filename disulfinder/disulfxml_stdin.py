#!/usr/bin/python
import sys
from optparse import OptionParser
from collections import defaultdict
from lxml.builder import ElementMaker
from lxml import etree as et
#doto: read from stdin
def parseDisulfinder(inFile):

	data= defaultdict(list)
	if inFile != None:
		f = open(inFile)
	else:
		f = sys.stdin.read()
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
	if inFile!=None:
		f.close()
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
	
	flipMap =  { " " : "0" , "*" : "1"}
	
	channel = E.annotation(
                        E.feature(
				E.name("Cystein disulfide bonding"),
				E.equalConcept(term="Binary cystein bonding map inside of one chain")
			),
                        E.condensedReferences(
                                E.methodIdRef("M#di")
                        )
                )



	for dsID in getContentIds(data):
		item = E.occurrence(
			E.position(
				E.point({"pos" : str(dsID), XS + "type" : "bx:SequencePoint"}),
				{ XS + "type" : "bx:SequencePosition"}
			),
			E.score(
				scoreTypeIdRef="S#st",value=str(data['DB_state'][dsID])
			),
			E.score(
				scoreTypeIdRef="S#co",value=str(data['DB_conf'][dsID])
			),
			E.score(
				scoreTypeIdRef="S#fl",value=flipMap[data['DB_flip'][dsID]]
			)
		)
		channel.append(item)



	mydoc = DI.disulfideBridgePrediction(
	E.referenceSequence(
		E.sequenceRecord(
			E.sequence("".join(data['AA'])),{XS+"type" : "bx:GeneralAminoacidSequenceRecord"  }
		)
	),
        E.blockWithOccurrenceReferences(
                E.method(
                        E.categoryConcept({
				"accession" : "operation_1850",
				"conceptUri" : "http://edamontology.org/operation_1850",
				"ontologyName" : "EDAM",
				"term" : "Protein cysteine and disulfide bond assignment"
			}),
                        E.citation(date="2013-06-28"),
			localId="M#di",name="disulfinder"
                ),
                E.scoreType(localId="S#st"),
                E.scoreType(localId="S#co"),
                E.scoreType(localId="S#fl"),
                
                channel
                
        ),
	{ XS+"schemaLocation": "http://rostlab.org/disulfinder/output http://i12r-tbl.informatik.tu-muenchen.de/~alex/disulfinder_output.xsd" }

	)
	if outFile != None:
		with open(outFile,"w+") as outF:
			outF.write(et.tostring(mydoc, pretty_print=True))
	else:
		print et.tostring(mydoc, pretty_print=True)


def main():
	parser = OptionParser()

	parser.add_option("-i","--input",dest="inFile",default=None,
        	        help="disulfinder ascii output file")
	parser.add_option("-o","--output",dest="outFile",default=None,
        	        help="BioXSD conform XML version of the disulfinder output")

	options,args = parser.parse_args()
	

	data = parseDisulfinder(options.inFile)
	writeBXD(data,options.outFile)


if __name__ == "__main__":
	main()

