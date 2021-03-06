#!/usr/bin/python
import sys
from lxml import etree as et

def parseNorsOutput(infile):
	#####################################################################
	# Preprocessing and stuff
	#####################################################################

	# define constants
	NR = "http://rostlab.org/norsnet/output"
	BX = "http://bioxsd.org/BioXSD-1.1"
	XSI = "http://www.w3.org/2001/XMLSchema-instance"

	# namespace map
	NS_MAP = {"nr": NR, "bx": BX, "xsi": XSI}


	#####################################################################
	# Create document parts
	#####################################################################

	# define root element
	# element or attribute names with a namespace are qualified names (QName)
	rootName = et.QName(NR, 'norsOutput')
	root = et.Element(rootName, nsmap=NS_MAP)

	# create attribute xsi:schemaLocation
	root.set(et.QName(XSI, 'schemaLocation'), "http://rostlab.org/norsnet/output http://i12r-tbl.informatik.tu-muenchen.de/~niko/norsnet_output.xsd")

	# now create children elements. We need bx:referenceSequence and bx:blockWithOccurrenceReferences
	rSeq = et.Element(et.QName(BX, 'referenceSequence'), nsmap=NS_MAP)
	seqRec = et.Element(et.QName(BX, 'sequenceRecord'), nsmap=NS_MAP)
	sequence = "" # empty string. We will append the sequence found in every line.
	block = et.Element(et.QName(BX, 'blockWithOccurrenceReferences'), nsmap=NS_MAP)

	#####################################################################
	# Read the actual file and populate block with occurrence references
	#####################################################################

	# populate block. We need method, scoreTypes and annotation.
	# Remember to put them together at the very end.
	# method
	method = et.Element(et.QName(BX, 'method'), nsmap=NS_MAP)
	method.set("localId", "nrs")
	method.set("name", "norsnet")

	catConcept = et.Element(et.QName(BX, 'categoryConcept'), nsmap=NS_MAP)
	catConcept.set("accession", "operation_244")
	catConcept.set("conceptUri", "http://edamontology.org/operation_0244")
	catConcept.set("ontologyName", "EDAM")
	catConcept.set("term", "Protein flexibility and motion analysis")

	citation = et.Element(et.QName(BX, 'citation'), nsmap=NS_MAP)
	citation.set("date", "2007-07-20")
	citation.set("accession", "17658943")
	citation.set("entryUri", "http://www.ncbi.nlm.nih.gov/pubmed/17658943")
	citation.set("dbName", "PubMed")

	method.append(catConcept)
	method.append(citation)

	# scoreTypes
	node1 = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	node1.set("localId", "n1")
	node2 = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	node2.set("localId", "n2")
	pred = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	pred.set("localId", "pred")
	n40 = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	n40.set("localId", "n40")
	n40fil = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	n40fil.set("localId", "n40f")
	n59 = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	n59.set("localId", "n59")
	n59fil = et.Element(et.QName(BX, 'scoreType'), nsmap=NS_MAP)
	n59fil.set("localId", "n59f")

	# annotation. Contains feature, condensedReferences and many occurrences
	annotation = et.Element(et.QName(BX, 'annotation'), nsmap=NS_MAP)

	feature = et.Element(et.QName(BX, 'feature'), nsmap=NS_MAP)
	name = et.Element(et.QName(BX, 'name'), nsmap=NS_MAP)
	name.text = "Protein Disorder Prediction"
	eqConc = et.Element(et.QName(BX, 'equalConcept'), nsmap=NS_MAP)
	eqConc.set("term", "Protein disorder prediction based on a neural network (2 nodes)")

	feature.append(name)
	feature.append(eqConc)

	conRef = et.Element(et.QName(BX, 'condensedReferences'), nsmap=NS_MAP)
	mtIdRef = et.Element(et.QName(BX, 'methodIdRef'), nsmap=NS_MAP)
	mtIdRef.text  = "nrs"
	conRef.append(mtIdRef)

	annotation.append(feature)
	annotation.append(conRef)



	# access norsnet output file
	f = open(infile, 'r') #sys.argv[1]
	# skip first line, since it only contains the column titles
	f.readline()
	# read file line by line
	for line in f:
		posValues = line.split()
		position = et.Element(et.QName(BX, 'position'), nsmap=NS_MAP)
		position.set(et.QName(XSI, 'type'), "bx:SequencePosition")
		point = et.Element(et.QName(BX, 'point'), nsmap=NS_MAP)
		point.set("pos", posValues[0])
		point.set(et.QName(XSI, 'type'), "bx:SequencePoint")
		position.append(point)
		
		score1 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score1.set("scoreTypeIdRef", "n1")
		score1.set("value", posValues[2])
		score2 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score2.set("scoreTypeIdRef", "n2")
		score2.set("value", posValues[3])
		score3 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score3.set("scoreTypeIdRef", "pred")
		score3.set("value", posValues[4])
		score4 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score4.set("scoreTypeIdRef", "n40")
		score4.set("value", posValues[5])
		score5 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score5.set("scoreTypeIdRef", "n40f")
		score5.set("value", posValues[6])
		score6 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score6.set("scoreTypeIdRef", "n59")
		score6.set("value", posValues[7])
		score7 = et.Element(et.QName(BX, 'score'), nsmap=NS_MAP)
		score7.set("scoreTypeIdRef", "n59f")
		score7.set("value", posValues[8])

		occ = et.Element(et.QName(BX, 'occurrence'), nsmap=NS_MAP)
		occ.append(position)
		occ.append(score1)
		occ.append(score2)
		occ.append(score3)
		occ.append(score4)
		occ.append(score5)
		occ.append(score6)
		occ.append(score7)
		annotation.append(occ)
		sequence += posValues[1]


	# now bring everything together
	block.append(method)
	block.append(node1)
	block.append(node2)
	block.append(pred)
	block.append(n40)
	block.append(n40fil)
	block.append(n59)
	block.append(n59fil)
	block.append(annotation)

	#####################################################################
	# Pick up sequence and populate rSeq. Finalize.
	#####################################################################
	seqObj = et.Element(et.QName(BX, 'sequence'), nsmap=NS_MAP)
	seqObj.text = sequence

	seqRec.append(seqObj)
	rSeq.append(seqRec)

	# append elements
	root.append(rSeq)
	root.append(block)

	# create sheet and print it
	sheet = et.ElementTree(root)
	print(et.tostring(sheet, pretty_print=True))


if __name__=="__main__":
	import argparse
	parser = argparse.ArgumentParser(description='parseNorsOutput takes a norsnet output file and converts it to BioXSD.')
	parser.add_argument('-i', metavar='str', type=str, required=True, help='input file')
	args = parser.parse_args()
	arguments = vars(args)
	input_file = arguments['i']
	parseNorsOutput(input_file)