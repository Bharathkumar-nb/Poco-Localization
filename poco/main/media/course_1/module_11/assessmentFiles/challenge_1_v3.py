#Module 8

#Challenge 1

'''
def predictor(row):
    if row['Self_Employed'] == 'No':
        return 'Y'
    else:
        return 'N'

reward = 1
no_reward = 0
correct_list = [reward if predictor(row) == row['Loan_Status'] else no_reward for row in loan_table]
correct_counter = sum(correct_list)
accuracy = float(correct_counter)/len(loan_table)
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
	predictor		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not callable(predictor):
	report('Data type bug', 'predictor is not a function - review function syntax', 'No further help available')
	sys.exit(1)

try:
	predictions = [predictor(row) for row in loan_table]
	y_count = predictions.count('Y')
	n_count = predictions.count('N')
except Exception as e:
	report('Generic error', 'Problem calling predictor function', e)
else:
	if y_count+n_count != len(predictions):
		report('Value bug', 'Wrong value returned by predictor ', 'No further help available')
		sys.exit(1)

def x_predictor(row):
    if row['Self_Employed'] == 'No':
        return 'Y'
    else:
        return 'N'

def y_predictor(row):
    if row['Self_Employed'] == 'Yes':
        return 'N'
    else:
        return 'Y'

xreward = 1
xno_reward = 0
xcorrect_list = [xreward if x_predictor(row) == row['Loan_Status'] else xno_reward for row in loan_table]
xcorrect_counter = sum(xcorrect_list)
xaccuracy = float(xcorrect_counter)/len(loan_table)

zreward = 1
zno_reward = 0
zcorrect_list = [zreward if y_predictor(row) == row['Loan_Status'] else zno_reward for row in loan_table]
zcorrect_counter = sum(zcorrect_list)
zaccuracy = float(zcorrect_counter)/len(loan_table)

try:
	ycorrect_list = [xreward if predictor(row) == row['Loan_Status'] else xno_reward for row in loan_table]
	ycorrect_counter = sum(ycorrect_list)
	yaccuracy = float(ycorrect_counter)/len(loan_table)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if yaccuracy != xaccuracy and yaccuracy != zaccuracy:
		report('Value bug', 'Wrong value in accuracy of ' + str(yaccuracy), 'No further help available')
		sys.exit(1)
