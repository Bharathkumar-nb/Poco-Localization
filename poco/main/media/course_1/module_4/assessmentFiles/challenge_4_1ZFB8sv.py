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
	#not "have matching brackets"  # this will be shown to user if he omits closing bracket on list

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

try:
	check = ('January' in quarter1)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'Missing month_1 in quarter1', 'No further help available')
	#continue

try:
	check = ('February' in quarter1)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'Missing month_2 in quarter1', 'No further help available')
	#continue

try:
	check = ('March' in quarter1)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'Missing month_3 in quarter1', 'No further help available')
	#continue

