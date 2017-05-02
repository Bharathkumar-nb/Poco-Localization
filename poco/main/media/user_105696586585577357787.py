#Module 4

#Challenge 1

'''
#This code can also be used to check DictReader and urlopen

import inspect

if not inspect.isclass(DictReader):
	report('Import error', 'DictReader not imported correctly', 'Review import syntax')
	sys.exit(1)

.....

if not inspect.isfunction(urlopen):
	report('Import error', 'urlopen not imported correctly', 'Review import syntax')
	sys.exit(1)
'''

import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

import pandas as pd # helps with handling csv formatted data

try:
	import pandas as pd
        url = https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv
        loan_table = pd.read_csv(url)
        loan_table_fill = loan_table_fill.fillna('')
        loan_table_dict = loan_table_fill.T.to_dict()
        first_row = loan_table_dict.values()
        first_row[0]
          

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

if not pd:
	report('Import error', 'pd not imported correctly', 'Review import syntax')
	sys.exit(1)

try:
	loan_table   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(loan_table, list):
	report('Data type bug', 'loan_table is not a list', 'No further help available')
	sys.exit(1)

xurl = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
xdf = pd.read_csv(url)  # reads in the data from web
xdf_fill = xdf.fillna('') # replace empty values with empty string 
xdf_dict = xdf_fill.T.to_dict() # create dictionary

xloan_table  = xdf_dict.values() # convert to final form

if len(loan_table) != len(xloan_table):
	report('Length bug', 'loan_table has ' + str(len(loan_table)) + ' rows and should have ' + str(len(xloan_table)), 'No further help available')
	sys.exit(1)

peek = min(3, len(loan_table))

if not all(type(item) is dict for item in loan_table):
	report('Data type bug', 'loan_table should be a list of dictionaries - first several items: ' + str(loan_table[:peek]), 'No further help available')
	sys.exit(1)

try:
	first_row		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(first_row, dict):
	report('Data type bug', 'first_row is not a dict', 'No further help available')
	sys.exit(1)

try:
	check = (first_row == xloan_table[0])
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in first_row of ' + str(first_row), 'No further help available')
