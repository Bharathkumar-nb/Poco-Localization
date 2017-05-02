#Module 4

#Challenge 4

'''
mean_applicantincome = float(sum_applicantincome_column)/len(int_applicantincome_column)
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
loan_table = [row for row in DictReader(response)]
first_row = loan_table[0]

applicantincome_column = [row['ApplicantIncome'] for row in loan_table]
int_applicantincome_column = [int(income) for income in applicantincome_column]
sum_applicantincome_column = sum(int_applicantincome_column)]

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
  mean_applicantincome   # does var exist?
except NameError as e:
  report('Name error', 'Typically a typo', e)
  sys.exit(1)

if not isinstance(mean_applicantincome, float):
  report('Data type bug', 'mean_applicantincome_column is not a float', 'Remember to float numerator or denominator')
  sys.exit(1)

try:
	check = (int(mean_applicantincome) == int(sum_applicantincome_column/len(int_applicantincome_column)))  # doing int compare as crude measure
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in mean_applicantincome of ' + str(mean_applicantincome), 'No further help available')
