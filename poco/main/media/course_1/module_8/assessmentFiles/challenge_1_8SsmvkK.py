#Module 5

#Challenge 1

'''
from csv import DictReader # helps with handling csv formatted data
​
from urllib2 import urlopen # helps with pulling data off the web
​
url = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
​
response = urlopen(url)
​
loan_table = [row for row in DictReader(response)]  # a mapping function using identity
​
print(loan_table[0])  # print the first row of the table - Mr. Braund
​
len(loan_table) # 641
{'Property_Area': 'Urban', 'Loan_ID': 'LP001002', 'CoapplicantIncome': '0', 'LoanAmount': '',
 'Self_Employed': 'No', 'Married': 'No', 'ApplicantIncome': '5849', 'Loan_Amount_Term': '360',
  'Gender': 'Male', 'Loan_Status': 'Y', 'Dependents': '0', 'Education': 'Graduate', 'Credit_History': '1'}
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first
​
xrow1 = {'Property_Area': 'Urban', 'Loan_ID': 'LP001002', 'CoapplicantIncome': '0', 'LoanAmount': '',
 'Self_Employed': 'No', 'Married': 'No', 'ApplicantIncome': '5849', 'Loan_Amount_Term': '360',
  'Gender': 'Male', 'Loan_Status': 'Y', 'Dependents': '0', 'Education': 'Graduate', 'Credit_History': '1'}

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	DictReader
except NameError as e:
	report('Name error', 'Typically a typo - check import statement', e)
	sys.exit(1)

if type(DictReader) != 'classobj':
	report('Import error', 'DictReader not imported correctly', 'Review import syntax')
	sys.exit(1)

try:
	urlopen
except NameError as e:
	report('Name error', 'Typically a typo - check import statement', e)
	sys.exit(1)

if type(urlopen) != 'function':
	report('Import error', 'urlopen not imported correctly', 'Review import syntax')
	sys.exit(1)

try:
	loan_table   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(loan_table, list):
	report('Data type bug', 'loan_table is not a list', 'No further help available')
	sys.exit(1)

url = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
response = urlopen(url)
answer = [row for row in DictReader(response)]
​answer_len = len(answer)

if len(loan_table) != answer_len:
	report('Length bug', 'loan_table has ' + str(len(loan_table)) + ' rows and shoould have ' + str(answer_len), 'No further help available')
	sys.exit(1)

if not all(type(item) is dict for item in loan_table):
	report('Data type bug', 'loan_table should be a list of dictionaries - first several items: ' + str(loan_table[:10]), 'No further help available')
	sys.exit(1)

try:
	first_row		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(first_row, dict):
	report('Data type bug', 'first_row is not a dict', 'No further help available')
	sys.exit(1)

try:
	check = (first_row == answer[0])
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in first_row of ' + str(first_row), 'No further help available')
