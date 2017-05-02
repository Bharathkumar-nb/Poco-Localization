#Module 4

#Challenge 5

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
xurl = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
xdf = pd.read_csv(url)  # reads in the data from web
xdf_fill = xdf.fillna('') # replace empty values with empty string 
xdf_dict = xdf_fill.T.to_dict() # create dictionary

loan_table  = xdf_dict.values() # convert to final form

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	rural_table   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(rural_table, list):
	report('Data type bug', 'rural_table is not a list', 'No further help available')
	sys.exit(1)

xrural_table = [row for row in loan_table if row['Property_area'] == 'Rural']

if len(rural_table) != len(xrural_table):
	report('Length bug', 'rural_table has ' + str(len(rural_table)) + ' rows and should have ' + str(len(xrural_table)), 'No further help available')
	sys.exit(1)

peek = min(3, len(rural_table))

if not all(type(item) is dict for item in rural_table):
	report('Data type bug', 'rural_table should be a list of dictionaries - first several items: ' + str(rural_table[:peek]), 'No further help available')
	sys.exit(1)

try:
	check = (rural_table == xrural_table)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in rural_table - first several items: ' + str(rural_table[:peek]), 'No further help available')
