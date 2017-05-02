#Module 5

#Challenge 7

'''
full_loan_column = [row if row['LoanAmount'] != '' else loan_amount_default for row in loan_table]

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

float_loan_amount = [float(row['LoanAmount']) for row in xloan_table if row['LoanAmount'] != '']

loan_amount_default = sum(float_loan_amount)/len(float_loan_amount)

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	full_loan_column		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(full_loan_column, list):
	report('Data type bug', 'full_loan_column is not a list', 'No further help available')
	sys.exit(1)

x_full_loan_column = [row['LoanAmount'] if row['LoanAmount'] != '' else loan_amount_default for row in xloan_table]
answer_len = len(x_full_loan_column)

if len(full_loan_column) != answer_len:
	report('Length bug', 'full_loan_column should have length of ' + str(answer_len) + ' but has length ' + str(len(full_loan_column)), 'No further help available')
	sys.exit(1)

'''
#approx
x_ints = [int(item) for item in x_full_loan_column]
user_ints = [int(item) for item in full_loan_column]
x_ints == user_ints
'''

try:
	check = (full_loan_column == x_full_loan_column)  # 
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in full_loan_column. Here are first 10 items: ' + str(full_loan_column[:10]), 'No further help available')

