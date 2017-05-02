#Module 1

#Challenge 6

'''
daisy = {'Name': 'Daisy', 'Weight': 23}
rusty = {'Name': 'Rusty', 'Weight': 42}
ramona = {'Name': 'Ramona', 'Weight': 25}
'''

import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))
	
#Mock data goes first

try:
	&&&  # paste user code here
except Exception as e:
	report('Generic error', 'On your own', e)  # won't get to this code for certain types of syntax errors
	sys.exit(1)

### daisy
try:
	daisy		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(daisy, dict):
	report('Data type bug', 'daisy is not a dictionary', 'No further help available')
	sys.exit(1)

if len(daisy) != 2:
	report('Length bug', 'daisy should have length of 2 but has length ' + str(len(daisy)), 'No further help available')
	sys.exit(1)

try:
	check = (daisy['Name'] == 'Daisy')
except KeyError as e:
	report('Key bug', 'expecting key of "Name" in daisy but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for daisy "Name" of ' + str(repr(daisy['Name'])), 'No further help available')

try:
	check = (daisy['Weight'] == 23)
except KeyError as e:
	report('Key bug', 'expecting key of "Weight" for daisy but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for daisy "Weight" of ' + str(repr(daisy['Weight'])), 'No further help available')

### rusty
try:
	rusty		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(rusty, dict):
	report('Data type bug', 'rusty is not a dictionary', 'No further help available')
	sys.exit(1)

if len(rusty) != 2:
	report('Length bug', 'rusty should have length of 2 but has length ' + str(len(rusty)), 'No further help available')
	sys.exit(1)

try:
	check = (rusty['Name'] == 'Rusty')
except KeyError as e:
	report('Key bug', 'expecting key of "Name" for rusty but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for rusty "Name" of ' + str(repr(rusty['Name'])), 'No further help available')

try:
	check = (daisy['Weight'] == 42)
except KeyError as e:
	report('Key bug', 'expecting key of "Weight" for rusty but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for rusty "Weight" of ' + str(repr(rusty['Weight'])), 'No further help available')

### ramona
try:
	ramona		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(ramona, dict):
	report('Data type bug', 'ramona is not a dictionary', 'No further help available')
	sys.exit(1)

if len(ramona) != 2:
	report('Length bug', 'ramona should have length of 2 but has length ' + str(len(ramona)), 'No further help available')
	sys.exit(1)

try:
	check = (ramona['Name'] == 'Ramona')
except KeyError as e:
	report('Key bug', 'expecting key of "Name" for ramona but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for ramona "Name" of ' + str(repr(ramona['Name'])), 'No further help available')

try:
	check = (ramona['Weight'] == 25)
except KeyError as e:
	report('Key bug', 'expecting key of "Weight" for ramona but does not exist', 'Be careful with lower and upper case')
	# keep checking for others
else:
	if not check:
		report('Value bug', 'Wrong value for ramona "Weight" of ' + str(repr(ramona['Weight'])), 'No further help available')


