#Module 1

#Challenge 3

'''
month_1 = 'January'
month_2 = 'February'
month_3 = 'March' 
'''

import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

#none

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	check = (month_1 == 'January')
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled month_1 has incorrect value ' + str(month_1))
try:
	check = (month_2 == 'February')
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled month_2 has incorrect value ' + str(month_2))
try:
	check = (month_3 == 'March')
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled month_3 has incorrect value ' + str(month_3))		
