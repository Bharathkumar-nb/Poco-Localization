#Module 4

#Challenge 2

'''
applicantincome_column = [row['ApplicantIncome'] for row in loan_table]
int_applicantincome_column = [int(income) for income in applicantincome_column]
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
	int_applicantincome_column   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(int_applicantincome_column, list):
	report('Data type bug', 'int_applicantincome_column is not a list', 'No further help available')
	sys.exit(1)

answer = [row['ApplicantIncome'] for row in loan_table]
answer_len = len(answer)

if len(int_applicantincome_column) != answer_len:
	report('Length bug', 'int_applicantincome_column should have length of ' + str(answer_len) + ' but has length ' + str(len(int_applicantincome_column)), 'No further help available')
	sys.exit(1)

try:
	check = (int_applicantincome_column == answer)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in int_applicantincome_column: first several rows are ' + str(int_applicantincome_column[:10]), 'Make sure to convert string to int')
