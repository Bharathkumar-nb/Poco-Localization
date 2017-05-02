#Module 5

#Challenge 4

'''
self_employed_default = 'Yes' if se_yes_count>se_no_count else 'No'

{'Property_Area': 'Urban', 'Loan_ID': 'LP001002', 'CoapplicantIncome': '0', 'LoanAmount': '',
 'Self_Employed': 'No', 'Married': 'No', 'ApplicantIncome': '5849', 'Loan_Amount_Term': '360',
  'Gender': 'Male', 'Loan_Status': 'Y', 'Dependents': '0', 'Education': 'Graduate', 'Credit_History': '1'}
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

first_row = loan_table[0]

se_yes_count = len([row for row in xloan_table if row['Self_Employed'] == 'Yes'])
se_no_count = len([row for row in xloan_table if row['Self_Employed'] == 'No'])

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	self_employed_default		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(self_employed_default, str):
	report('Data type bug', 'self_employed_default is not a string', 'No further help available')
	sys.exit(1)

try:
	check = (self_employed_default == 'No')
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in self_employed_default of ' + str(repl(self_employed_default)), 'No further help available')

