#Module 0

#Challenge 1

import sys
from csv import DictReader # helps with handling csv formatted data
from urllib2 import urlopen # helps with pulling data off the web

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))


try:
        url = "&&&"
        url.rstrip()
        response = urlopen(url)
        first_table = [row for row in DictReader(response)]
        report('No error', "first couple rows", str(first_table[0]).replace("\'", "`"))
except Exception as e:
	report('Generic error', "shortd", e)
	sys.exit(1)

