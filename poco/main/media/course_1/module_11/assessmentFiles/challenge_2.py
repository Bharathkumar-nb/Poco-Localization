#Module 8

#Challenge 2

'''
amounts = [float(row['LoanAmount']) for row in loan_table if row['LoanAmount'] != '']
loan_account_mean = sum(amounts)/len(amounts)
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
	loan_account_mean		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

xamounts = [float(row['LoanAmount']) for row in loan_table if row['LoanAmount'] != '']

try:
	check = (loan_account_mean == sum(xamounts)/len(xamounts))
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in loan_account_mean of ' + str(repr(loan_account_mean)), 'No further help available')
		sys.exit(1)