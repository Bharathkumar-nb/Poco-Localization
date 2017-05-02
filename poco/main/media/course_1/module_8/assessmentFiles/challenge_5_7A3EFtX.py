#Module 5

#Challenge 5

'''
float_loan_amount = [float(row['LoanAmount']) for row in loan_table if row['LoanAmount'] != '']

loan_amount_default = sum(float_loan_amount)/len(float_loan_amount)

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

try:
	&&&  # paste user code here

except ValueError as e:
	report('Value error', 'Remember cannot use int function on empty value', e)
	sys.exit(1)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	loan_amount_default		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(loan_amount_default, float):
	report('Data type bug', 'loan_amount_default is not a float', 'No further help available')
	sys.exit(1)

try:
	_x = [float(row['LoanAmount']) for row in xloan_table if row['LoanAmount'] != '']
	check = (int(loan_amount_default) == int(sum(_x)/len(_x)))  # taking int to avoid precision mismatch - 146.412162162
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	report('Debugging1', str(int(loan_amount_default)), str(int(sum(_x)/len(_x))))
	if not check:
		report('Value bug', 'Wrong value in loan_amount_default of ' + str(loan_amount_default), 'No further help available')

