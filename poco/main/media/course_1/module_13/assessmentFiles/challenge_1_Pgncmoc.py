#Module 9

#Challenge 2

'''
def predictor( row ):


'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

from csv import DictReader # helps with handling csv formatted data
from urllib2 import urlopen # helps with pulling data off the web

# TRAIN DATA
url = 'https://docs.google.com/spreadsheets/d/1z1ycUZjJpmMWB4gXbhwRQ9B_qa42CwzAQkf82mLibxI/pub?output=csv'
response = urlopen(url)
train_table = [row for row in DictReader(response)]  # a mapping function using identity

# TEST DATA
url = 'https://docs.google.com/spreadsheets/d/1HhuBRTf3FyHY7zgyR3YJFen2IPwVsn0UHoqJqa6_teM/pub?output=csv'
response = urlopen(url)
test_table = [row for row in DictReader(response)]  # a mapping function using identity

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
	train_cases = [[predictor(row), row['Survived']] for row in train_table]
	test_cases = [[predictor(row), row['Survived']] for row in test_table]
except Exception as e:
	report('Generic error', 'Problem calling predictor function', e)
	sys.exit(1)
else:
	if len(train_cases) != len(train_table) or len(test_cases) != len(test_table):
		report('Length bug', 'Not predicting a value for every row', 'No further help available')
		sys.exit(1)

pp_count_train = train_cases.count(['1','1'])
nn_count_train = train_cases.count(['0','0'])

train_accuracy = (pp_count_train + nn_count_train)/float(len(train_table))

pp_count_test = test_cases.count(['1','1'])
nn_count_test = test_cases.count(['0','0'])

test_accuracy = (pp_count_test + nn_count_test)/float(len(test_table))

if 	train_accuracy > test_accuracy:
	report('Testing bug', 'Training accuracy ({0}) greater than test accuracy ({1}).'.format(train_accuracy, test_accuracy), 'No further help available')
	sys.exit(1)
