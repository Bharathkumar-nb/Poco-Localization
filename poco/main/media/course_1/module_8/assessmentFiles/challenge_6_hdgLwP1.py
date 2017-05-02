#Module 5

#Challenge 6

'''
int_loan_status = [1 if row['Loan_Status'] == 'Yes' else 0 for row in loan_table]

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
​
url = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
​
response = urlopen(url)
​
loan_table = [row for row in DictReader(response)]  # a mapping function using identity

xloan_table = loan_table  # in case user screws with loan_table

first_row = loan_table[0]

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	int_loan_status		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(int_loan_status, list):
	report('Data type bug', 'int_loan_status is not a float', 'No further help available')
	sys.exit(1)

answer = [1 if row['Loan_Status'] == 'Yes' else 0 for row in loan_table]
answer_len = len(answer)

if len(int_loan_status) != answer_len:
	report('Length bug', 'int_loan_status should have length of ' + str(answer_len) + ' but has length ' + str(len(int_loan_status)), 'No further help available')
	sys.exit(1)

try:
	check = (int_loan_status == answer)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in int_loan_status: first several rows are ' + str(int_loan_status[:10]), 'No further help available')

