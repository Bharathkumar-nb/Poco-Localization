#Module 1

#Challenge 7

'''
dogs = [daisy, rusty, ramona]  # but did not specify order
'''

import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))
	
#Mock data goes first
daisy = {'Name': 'Daisy', 'Weight': 23}
rusty = {'Name': 'Rusty', 'Weight': 42}
ramona = {'Name': 'Ramona', 'Weight': 25}

try:
	&&&  # paste user code here
except Exception as e:
	report('Generic error', 'On your own', e)  # won't get to this code for certain types of syntax errors
	sys.exit(1)

### daisy
try:
	dogs		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(dogs, list):
	report('Data type bug', 'dogs is not a list', 'No further help available')
	sys.exit(1)

if len(dogs) != 3:
	report('Length bug', 'dogs should have length of 3 but has length ' + str(len(dogs)), 'No further help available')

try:
	check = (daisy in dogs)
except Exception as e:
	report('Generic error', 'On your own', e)  # won't get to this code for certain types of syntax errors
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'daisy not found in dogs', 'No further help available')

try:
	check = (rusty in dogs)
except Exception as e:
	report('Generic error', 'On your own', e)  # won't get to this code for certain types of syntax errors
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'rusty not found in dogs', 'No further help available')

try:
	check = (ramona in dogs)
except Exception as e:
	report('Generic error', 'On your own', e)  # won't get to this code for certain types of syntax errors
	sys.exit(1)
else:
	if not check:
		report('Value bug', 'ramona not found in dogs', 'No further help available')


