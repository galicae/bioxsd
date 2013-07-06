from pysimplesoap.client import SoapClient
client = SoapClient(wsdl="http://localhost/webservice/disulfinder/disulfinder_soap.wsdl",trace=False)
print "Target Namespace", client.namespace
for service in client.services.values():
    for port in service['ports'].values():
        print port['location']
        for op in port['operations'].values():
            print 'Name:', op['name']
            print 'Docs:', op['documentation'].strip()
            print 'SOAPAction:', op['action']
            print 'Input', op['input'] # args type declaration
            print 'Output', op['output'] # returns type declaration
            print
