#Module 9

#Challenge 1

'''
def predictor( row ):
    grad = row['Education']
    if grad == 'Graduate':
        return 'Y'
    else:
        return 'N'
    raise ValueError('No leaf reached for row: ' + row)
    
cases = [[predictor(row), row['Loan_Status']] for row in loan_table]

'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

from csv import DictReader # helps with handling csv formatted data
from urllib2 import urlopen # helps with pulling data off the web
url = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
response = urlopen(url)
loan_table = [row for row in DictReader(response)]  # a mapping function using identity

xloan_table = loan_table  # in case user screws with loan_table



try:
	&&&  # paste user code here 

except IndentationError as e:
	report('Indentation error', 'Make sure you are using tabs for indentation, and not spaces.', e)
	sys.exit(1)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	predictor		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not callable(predictor):
	report('Data type bug', 'predictor is not a function - review function syntax', 'No further help available')
	sys.exit(1)

try:
	cases		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not type(cases) is list:
	report('Data error', 'cases is not a list', 'No further help available')
	sys.exit(1)

if len(cases) != len(loan_table):
	report('Length bug', 'cases of wrong length: ' + str(len(cases)), 'No further help available')
	sys.exit(1)

if not all([(type(item) is list and len(item) == 2 and type(item[0]) is str and type(item[1]) is str) for item in cases]):
	report('Data error', 'items in cases are not correct - first several: ' + str(cases[:5]), 'No further help available')
	sys.exit(1)

def xpredictor( row ):
	xgrad = row['Education']
	if xgrad == 'Graduate':
		return 'Y'
	else:
		return 'N'
	raise ValueError('No leaf reached for row: ' + row)
    
xcases = [[xpredictor(row), row['Loan_Status']] for row in loan_table]

if 	xcases != cases:
	report('Value bug', 'cases does not contain correct values.', 'No further help available')
	sys.exit(1)
