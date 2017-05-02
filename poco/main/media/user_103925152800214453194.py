#Module 1

#Challenge 2

'''
one = one + 1  # how can we know if they just did one = 2?
two = two + 1
three = three + 1
'''

import sys

#Mock data goes first

one = 1
two = 2
three = 3

def report( name, shortd, longd):
	d = {'Name': name+sys.version, 'Short': shortd, 'Long': longd}
	print(str(d))

try:
	#Type python code here
        one = one+1
          

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	check = (one == 2)
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled one has incorrect value ' + str(one))

try:
	check = (two == 3)
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled two has incorrect value ' + str(two))
		
try:
	check = (three == 4)
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled three has incorrect value ' + str(three))		
