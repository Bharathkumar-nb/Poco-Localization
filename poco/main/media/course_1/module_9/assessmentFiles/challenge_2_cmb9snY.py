#Module 6

#Challenge 2

'''
int_scores

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

try:
	&&&  # paste user code here

except ValueError as e:
	report('Conversion error', 'Make sure you skip empty values', e)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	int_scores		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(int_scores, list):
	report('Data type bug', 'int_scores is not a list', 'No further help available')
	sys.exit(1)

answer = [int(row['Credit_History']) for row in xloan_table if row['Credit_History'] != '']
answer_len = len(answer)
peek = min(10, len(int_scores))

if len(int_scores) != answer_len:
	report('Length bug', 'int_scores has ' + str(len(int_scores)) + ' items and should have ' + str(answer_len), 'No further help available')
	sys.exit(1)

if not all(type(item) is int for item in int_scores):
	report('Data type bug', 'int_scores should be a list of ints - first several items: ' + str(int_scores[:peek]), 'No further help available')
	sys.exit(1)

try:
	check = (int_scores == answer)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in int_scores - first several items: ' + str(int_scores[:peek]), 'No further help available')
