import timeit
import subprocess
from collections import defaultdict

def getTime(shellCmd):
	start = timeit.default_timer()
	subprocess.call(shellCmd,shell=True)
	stop = timeit.default_timer()
	return stop - start

restCMD = "python RESTclient.py -i Q30201.fasta -o test.xml"
soapCMD = "python SOAPclient.py < Q30201.fasta"

times = defaultdict(list)


for i in range(100):
	t = getTime(restCMD)
	times["rest"].append(t)

for i in range(100):
	t = getTime(soapCMD)
	times["soap"].append(t)

with open("timeOut.txt","w") as f:
	for key in times.iterkeys():
		f.write(",".join(times[key]))
	
