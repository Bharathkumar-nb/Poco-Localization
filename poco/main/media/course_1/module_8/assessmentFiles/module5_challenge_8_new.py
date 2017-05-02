#Module 5

#Challenge 7

'''

'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

import pandas as pd
xurl = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
xdf = pd.read_csv(xurl)  # reads in the data from web
xdf_fill = xdf.fillna('') # replace empty values with empty string 
xdf_dict = xdf_fill.T.to_dict() # create dictionary

xloan_table  = xdf_dict.values() # convert to final form

loan_table = xloan_table 

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	parea_mode   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(parea_mode, str):
	report('Data type bug', 'parea_mode is not a string', 'No further help available')
	sys.exit(1)

try:
	check = (parea_mode == 'Semiurban')
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in parea_mode: ' + str(parea_mode), 'No further help available')
