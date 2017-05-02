#Module 7

#Challenge 2

'''
yes_by_gender = [row['Gender'] for row in loan_table if row['Loan_Status'] == 'Y']

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
	yes_by_gender		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(yes_by_gender, list):
	report('Data type bug', 'yes_by_gender is not a list', 'No further help available')
	sys.exit(1)

yanswer = [row['Gender'] for row in loan_table if row['Loan_Status'] == 'Y']
yanswer_len = len(yanswer)
ypeek = min(10, yanswer_len)

if len(yes_by_gender) != yanswer_len:
	report('Length bug', 'yes_by_gender has ' + str(len(yes_by_gender)) + ' items and should have ' + str(yanswer_len), 'Reminder: should include empty values')
	sys.exit(1)

if not all(type(item) is str for item in yes_by_gender):
	report('Data type bug', 'yes_by_gender should be a list of strings - first several items: ' + str(yes_by_gender[:ypeek]), 'No further help available')
	sys.exit(1)

try:
	check = (yes_by_gender == yanswer)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in yes_by_gender - first several items: ' + str(yes_by_gender[:ypeek]), 'No further help available')
