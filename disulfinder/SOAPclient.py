from pysimplesoap.client import SoapClient, SoapFault
import sys

client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://alex.tbl/webservice/disulfinder/disulfinder_soap.wsdl", 
    soap_ns='soap',
    trace = True,
    ns = False)


fasta = sys.stdin.read()

response = client.GetDsBonds(getDisulfinderRequest = fasta)

# extract and convert the returned value
result = response.getDisulfinderResponse
print result
