#Module 1

#Challenge 5

'''
dict_practice = {'One': month_1, 'Two': month_2, 'Three': month_3}
'''

import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))
	
#Mock data goes first

month_1 = 'January'
month_2 = 'February'
month_3 = 'March' 

try:
	
    #user submission
    #Type python code here
    dict_practice = {}  
	not 'have both opening and closing brace'  # what is here will be reported to calling code as part of syntax error message
except Exception as e:
	report('Generic error', 'On your own', e)  # won't get to this code for certain types of syntax errors
	sys.exit(1)

try:
	dict_practice		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(dict_practice, dict):
	report('Data type bug', 'dict_practice is not a dictionary', 'No further help available')
	sys.exit(1)

if len(dict_practice) != 3:
	report('Length bug', 'dict_practice should have length of 3 but has length ' + str(len(dict_practice)), 'No further help available')
	sys.exit(1)

try:
	check = (dict_practice['One'] == 'January')
except KeyError as e:
	report('Key bug', 'expecting key of "One" but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for "One"', 'value of "One" is ' + str(dict_practice['One']) + ' which is incorrect')

try:
	check = (dict_practice['Two'] == 'February')
except KeyError as e:
	report('Key bug', 'expecting key of "Two" but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for "Two"', 'value of "Two" is ' + str(dict_practice['Two']) + ' which is incorrect')

try:
	check = (dict_practice['Three'] == 'March')
except KeyError as e:
	report('Key bug', 'expecting key of "Three" but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for "Three"', 'value of "Three" is ' + str(dict_practice['Three']) + ' which is incorrect')
