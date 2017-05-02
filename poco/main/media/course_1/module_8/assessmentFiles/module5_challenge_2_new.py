#Module 5

#Challenge 2

'''
lam_column = [row['CoapplicantIncome'] for row in loan_table if row['CoapplicantIncome'] != '']  # has empties
n = len(lam_column)
lam_column = sorted(lam_column)
x = lam_column[n/2]
y = lam_column[(n/2)-1]
coapplicantincome_median = (x+y)/2
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
	coapplicantincome_median   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(coapplicantincome_median, float):
	report('Data type bug', 'coapplicantincome_median is not a float', 'No further help available')
	sys.exit(1)

xlam_column = [row['CoapplicantIncome'] for row in loan_table if row['CoapplicantIncome'] != '']  # has empties
xn = len(xlam_column)
xlam_column = sorted(xlam_column)
xx = xlam_column[xn/2]
xy = xlam_column[(xn/2)-1]
xcoapplicantincome_median = (xx+xy)/2

try:
	check = (coapplicantincome_median == xcoapplicantincome_median)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in coapplicantincome_median: ' + str(coapplicantincome_median), 'No further help available')
