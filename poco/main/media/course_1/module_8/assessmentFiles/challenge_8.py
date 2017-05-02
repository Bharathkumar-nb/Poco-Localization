#Module 5

#Challenge 8

'''
wrangled_loan_status_column = [1 if row['Loan_Status'] == 'Y' else 0 for row in loan_table]

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
	wrangled_loan_status_column		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(wrangled_loan_status_column, list):
	report('Data type bug', 'wrangled_loan_status_column is not a list', 'No further help available')
	sys.exit(1)

x_wrangled_loan_status_column = [1 if row['Loan_Status'] == 'Y' else 0 for row in xloan_table]
answer_len = len(x_wrangled_loan_status_column)

if len(wrangled_loan_status_column) != answer_len:
	report('Length bug', 'wrangled_loan_status_column should have length of ' + str(answer_len) + ' but has length ' + str(len(wrangled_loan_status_column)), 'No further help available')
	sys.exit(1)

'''
#approx
x_ints = [int(item) for item in x_wrangled_loan_column]
user_ints = [int(item) for item in wrangled_loan_column]
x_ints == user_ints
'''

try:
	check = (wrangled_loan_status_column == x_wrangled_loan_status_column)  # 
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in wrangled_loan_status_column. Here are first 10 items: ' + str(wrangled_loan_status_column[:10]), 'Expecting list of ints')

