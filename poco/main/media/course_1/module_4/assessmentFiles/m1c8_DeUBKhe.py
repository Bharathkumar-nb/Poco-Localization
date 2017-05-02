#Module 1

#Challenge 8

'''
cdatetime			address			district	beat	grid	crimedescr						latitude	longitude
1/1/2006 0:00:00	3108 OCCIDENTAL DR	3		3C		1115	TAKE VEH W/O OWNER	38.55042047	-121.3914158
1/1/2006 0:00:00	2082 EXPEDITION WAY	5		5A		1512	BURGLARY RESIDENCE		38.47350069	-121.4901858
1/1/2006 0:00:00	4 PALEN CT			2		2A		212		10851(A)VC TAKE VEH W/O OWNER	38.65784584	-121.4621009
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

xrow0 = {'cdatetime':'1/1/2006 0:00:00'	,'address':'3108 OCCIDENTAL DR'	,'district':3	,
			'beat':'3C'	,'grid':1115	,'crimedescr':'TAKE VEH W/O OWNER'	,'latitude':38.55042047	,'longitude':-121.3914158}

xrow1 = {'cdatetime':'1/1/2006 0:00:00'	,'address':'2082 EXPEDITION WAY'	,'district':5	,
			'beat':'5A'	,'grid':1512	,'crimedescr':'BURGLARY RESIDENCE'	,'latitude':38.47350069	,'longitude':-121.4901858}

xrow2 = {'cdatetime':'1/1/2006 0:00:00'	,'address':'4 PALEN CT'	,'district':2	,
			'beat':'2A'	,'grid':212	,'crimedescr':'TAKE VEH W/O OWNER'	,'latitude':38.65784584	,'longitude':-121.4621009}

xcrime = [xrow0, xrow1, xrow2]

xkeys = sorted(xrow1.keys())

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	row0
except NameError as e:
	report('Name error', e, 'Typically a typo')
	sys.exit(1)

if type(row0) is not dict:
	report('Type bug', 'Type of row0 is not a dictionary but instead a ' + str(type(row0)), 'No further help available.')
	sys.exit(1)

if len(row0) < len(xrow0):
	report('Length bug', 'row0 is missing one or more key-values ', 'No further help available')
	sys.exit(1)

if len(row0) > len(xrow0):
	report('Length bug', 'row0 has extra key-values ', 'No further help available')
	sys.exit(1)

if sorted(row0.keys()) != xkeys:
	report('Value bug', 'row0 keys do not match ' + str(xkeys), 'No further help available')
	sys.exit(1)

if sorted(row0.values()) != sorted(xrow0.values()):
	report('Value bug', 'Incorrect values in row0: ' + str(row0), 'No further help available')
	sys.exit(1)

try:
	row1
except NameError as e:
	report('Name error', e, 'Typically a typo')
	sys.exit(1)

if type(row1) is not dict:
	report('Type bug', 'Type of row1 is not a dictionary but instead a ' + str(type(row1)), 'No further help available.')
	sys.exit(1)

if len(row1) < len(xrow1):
	report('Length bug', 'row1 is missing one or more key-values ', 'No further help available')
	sys.exit(1)

if len(row1) > len(xrow1):
	report('Length bug', 'row1 has extra key-values ', 'No further help available')
	sys.exit(1)

if sorted(row1.keys()) != xkeys:
	report('Value bug', 'row1 keys do not match ' + str(xkeys), 'No further help available')
	sys.exit(1)

if sorted(row1.values()) != sorted(xrow1.values()):
	report('Value bug', 'Incorrect values in row1: ' + str(row1), 'No further help available')
	sys.exit(1)

try:
	row2
except NameError as e:
	report('Name error', e, 'Typically a typo')
	sys.exit(1)

if type(row2) is not dict:
	report('Type bug', 'Type of row2 is not a dictionary but instead a ' + str(type(row2)), 'No further help available.')
	sys.exit(1)

if len(row2) < len(xrow2):
	report('Length bug', 'row2 is missing one or more key-values ', 'No further help available')
	sys.exit(1)

if len(row2) > len(xrow2):
	report('Length bug', 'row2 has extra key-values ', 'No further help available')
	sys.exit(1)

if sorted(row2.keys()) != xkeys:
	report('Value bug', 'row2 keys do not match ' + str(xkeys), 'No further help available')
	sys.exit(1)

if sorted(row2.values()) != sorted(xrow2.values()):
	report('Value bug', 'Incorrect values in row2: ' + str(row2), 'No further help available')
	sys.exit(1)	

try:
	crime_table
except NameError as e:
	report('Name error', e, 'Typically a typo')
	sys.exit(1)

if type(crime_table) is not list:
	report('Type bug', 'Type of crime_table is not a list but instead a ' + str(type(crime_table)), 'No further help available.')
	sys.exit(1)

if len(crime_table) > len(xcrime):
	report('Length bug', 'crime_table has more than 3 rows ', 'No further help available')
	sys.exit(1)

if len(crime_table) < len(xcrime):
	report('Length bug', 'crime_table is missing rows ', 'No further help available')
	sys.exit(1)

if crime_table[0] != xcrime[0]:
	report('Value bug', 'First value in crime_table is not correct: ' + str(crime_table[0]), 'No further help available')
	sys.exit(1)

if crime_table[1] != xcrime[1]:
	report('Value bug', 'Second value in crime_table is not correct: ' + str(crime_table[1]), 'No further help available')
	sys.exit(1)

if crime_table[2] != xcrime[2]:
	report('Value bug', 'Third value in crime_table is not correct: ' + str(crime_table[2]), 'No further help available')
	sys.exit(1)	
