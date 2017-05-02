#Module 5

#Challenge 1

'''
coapplicantincome_column = [row['Loan_Amount_Term'] for row in loan_table if row['Loan_Amount_Term'] != '']
n = len(coapplicantincome_column)
total = sum(coapplicantincome_column)
lat_average = total/n
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

loan_table  = xdf_dict.values() # convert to final form
first_row = loan_table[0] 

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	lat_average   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(lat_average, int):
	report('Data type bug', 'int_applicantincome_column is not a list', 'No further help available')
	sys.exit(1)

xcoapplicantincome_column = [row['Loan_Amount_Term'] for row in loan_table if row['Loan_Amount_Term'] != '']
xn = len(xcoapplicantincome_column)
xtotal = sum(xcoapplicantincome_column)
xlat_average = xtotal/xn

try:
	check = (lat_average == xlat_average)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in lat_average: ' + str(lat_average), 'No further help available')
