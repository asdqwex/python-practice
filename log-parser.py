from optparse import OptionParser
import re

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="source log file", metavar="FILE")
parser.add_option("-c", "--count", dest="count",
                  help="count instances of -s in file", metavar="COUNT")


(options, args) = parser.parse_args()

filename = options.filename
f = open(filename, 'r')

p = re.compile("/assets/flagship.otf")

flagmatchcounter = 1
ipaddresses = []

for line in f:

	flagmatch = p.match(line)
	if flagmatch != []:
		flagmatchcounter = flagmatchcounter + 1

	ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
	if ip not in ipaddresses:
		ipaddresses.append(ip)

print "flagship.otf was accessed:", flagmatchcounter, "times"

print " Ipaddresses that have accessed this website:"

print len(ipaddresses)
