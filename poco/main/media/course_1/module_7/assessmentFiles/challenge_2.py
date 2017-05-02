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

from csv import DictReader # helps with handling csv formatted data
from urllib2 import urlopen # helps with pulling data off the web
​
url = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
​
response = urlopen(url)
loan_table = [row for row in DictReader(response)]
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

try:
	check = (int_applicantincome_column == [int(row['ApplicantIncome']) for row in loan_table]
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in int_applicantincome_column of ' + str(int_applicantincome_column), 'Make sure to convert string to int')
