from optparse import OptionParser
import re

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="source log file", metavar="FILE")
parser.add_option("-s", "--string", dest="string",
                  help="regex to match", metavar="STRING")

(options, args) = parser.parse_args()

filename = options.filename
f = open(filename, 'r')

p = re.compile(options.string)

matchcounter = 1
ipaddresses = []
statuscodes = []
status_stats = {}

for line in f:
	line_buffer = line

	match = p.match(line)
	if match != []:
		matchcounter = matchcounter + 1

	ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
	if ip not in ipaddresses:
		ipaddresses.append(ip)

	line_parts = line_buffer.split(' ')
	statuscodes.append(line_parts[8])

for code in statuscodes:
	if code not in status_stats:
		status_stats[code] = 0
	status_stats[code] = status_stats[code] + 1

print options.string, "was found:", matchcounter, "times"

print len(ipaddresses), "Ipaddresses that have accessed this website"

print 'Number of times webserver responded with each status code'

for k, v in status_stats.iteritems():
	print k , v




