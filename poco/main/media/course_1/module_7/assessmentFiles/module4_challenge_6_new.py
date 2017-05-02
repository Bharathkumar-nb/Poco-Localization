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
xdf = pd.read_csv(xurl)  # reads in the data from web
xdf_fill = xdf.fillna('') # replace empty values with empty string 
xdf_dict = xdf_fill.T.to_dict() # create dictionary

loan_table  = xdf_dict.values() # convert to final form
rural_table = [row for row in loan_table if row['Property_Area'] == 'Rural']

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	bad_rural_table   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(bad_rural_table, list):
	report('Data type bug', 'bad_rural_table is not a list', 'No further help available')
	sys.exit(1)

xbad_rural_table = [row for row in rural_table if row['Credit_History'] == 0]

if len(bad_rural_table) != len(xbad_rural_table):
	report('Length bug', 'bad_rural_table has ' + str(len(bad_rural_table)) + ' rows and should have ' + str(len(xbad_rural_table)), 'Check correct value for credit history')
	sys.exit(1)

peek = min(3, len(bad_rural_table))

if not all(type(item) is dict for item in bad_rural_table):
	report('Data type bug', 'bad_rural_table should be a list of dictionaries - first several items: ' + str(bad_rural_table[:peek]), 'No further help available')
	sys.exit(1)

try:
	check = (bad_rural_table == xbad_rural_table)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in bad_rural_table - first several items: ' + str(bad_rural_table[:peek]), 'No further help available')
