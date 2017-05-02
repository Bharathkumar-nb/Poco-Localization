#Module 1

#Challenge 4

'''
quarter1 = [month_1, month_2, month_3]
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
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	quarter1		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(quarter1, list):
	report('Data type bug', 'quarter1 is not a list', 'No further help available')
	sys.exit(1)

if len(quarter1) != 3:
	report('Length bug', 'quarter1 should have length of 3 but has length ' + str(len(quarter1)), 'No further help available')
	sys.exit(1)

try:
	check = (quarter1[0] == 'January')
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled quarter1 has incorrect value for first item ' + str(quarter[0]))
	#continue

try:
	check = (quarter1[1] == 'February')
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled quarter1 has incorrect value for second item ' + str(quarter[1]))
	#continue

try:
	check = (quarter1[2] == 'March')
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled quarter1 has incorrect value for third item ' + str(quarter[2]))
	#continue

