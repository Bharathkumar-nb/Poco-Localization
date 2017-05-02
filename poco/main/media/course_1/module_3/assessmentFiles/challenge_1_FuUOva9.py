#Module 0

#Challenge 1

'''
url to Sheets csv file
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

from csv import DictReader # helps with handling csv formatted data
from urllib2 import urlopen # helps with pulling data off the web

try:
	url = '''
	&&&
	'''
	url = url.strip()
	response = urlopen(url)
	first_table = [row for row in DictReader(response)]

except Exception as e:
	report('Generic error', 'Some problem with url submitted', e)
	sys.exit(1)

if not isinstance(first_table, list):
	report('Data type bug', 'Spreadsheet data does not look correct', 'No further help available')
	sys.exit(1)

if len(first_table) < 3:
	report('Length bug', 'Expecting 3 or more rows of data', 'No further help available')
	sys.exit(1)

if not isinstance(first_table[0], dict):
	report('Data type bug', 'Spreadsheet data does not look correct', 'No further help available')
	sys.exit(1)

if len(first_table[0].keys()) != 5:
	report('Length bug', 'Expecting  5 columns in spreadsheet', 'No further help available')
	sys.exit(1)


check = all([type(row) == dict for row in first_table])
if not check:
	report('Data type bug', 'Spreadsheet data does not look correct', 'No further help available')
	sys.exit(1)

# Name,Nickname,Hometown,HS Mascot,Scary

try:
	first_table[0]['Name']
except KeyError as e:
	report('Key error', "Don't see a column Name - remember case matters", e)
	sys.exit(1)

try:
	first_table[0]['Nickname']
except KeyError as e:
	report('Key error', "Don't see a column Nickname - remember case matters", e)
	sys.exit(1)

try:
	first_table[0]['Hometown']
except KeyError as e:
	report('Key error', "Don't see a column Hometown - remember case matters", e)
	sys.exit(1)

try:
	first_table[0]['HS Mascot']
except KeyError as e:
	report('Key error', "Don't see a column HS Mascot - remember case and spaces matters", e)
	sys.exit(1)

try:
	first_table[0]['Scary']
except KeyError as e:
	report('Key error', "Don't see a column Scary - remember case matters", e)
	sys.exit(1)


