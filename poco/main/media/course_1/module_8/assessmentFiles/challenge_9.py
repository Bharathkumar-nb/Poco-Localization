#Module 5

#Challenge 9

'''
float_loan_amount = [float(row['LoanAmount']) for row in loan_table if row['LoanAmount'] != '']

sorted_loan_amount = sorted(float_loan_amount)

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


try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	sorted_loan_amount		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(sorted_loan_amount, list):
	report('Data type bug', 'sorted_loan_amount is not a list', 'No further help available')
	sys.exit(1)

x_float_loan_amount = [float(row['LoanAmount']) for row in loan_table if row['LoanAmount'] != '']

x_sorted_loan_amount = sorted(x_float_loan_amount)

if len(sorted_loan_amount) != len(x_sorted_loan_amount):
	report('List length bug', 'sorted_loan_amount has wrong length of ' + str(len(sorted_loan_amount)), 'No further help available')
	sys.exit(1)

try:
	check = (sorted_loan_amount == x_sorted_loan_amount) 
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in sorted_loan_amount - first 10 values: ' + str(sorted_loan_amount[:10]), 'No further help available')

