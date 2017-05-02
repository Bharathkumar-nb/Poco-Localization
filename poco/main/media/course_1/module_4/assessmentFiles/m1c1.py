#Module 1

#Challenge 1

'''
one = 1
two = 2
three = 3
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

#No mock data for this challenge.

try:
	&&&  # paste user code here

except IndentationError as e:
	report('Indentation error', 'Make sure each line of code starts in column 1', e)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

errors = False

try:
	one
except NameError as e:
	report('Name error',  e, 'Typically a typo')
	errors = True

try:
	two
except NameError as e:
	report('Name error',  e, 'Typically a typo')
	errors = True

try:
	three
except NameError as e:
	report('Name error',  e, 'Typically a typo')
	errors = True

if errors:
	sys.exit(1)

if not one == 1:
	if type(one) is int:
		report('Value bug', 'Wrong value in box', 'Box labeled one has incorrect value ' + str(repr(one)))
	else:
		report('Type bug', 'Wrong type of value in box - should be an integer', 'Box labeled one has incorrect type ' + str(type(one)))
	sys.exit(1)

if not two == 2:
	if type(two) is int:
		report('Value bug', 'Wrong value in box', 'Box labeled one has incorrect value ' + str(repr(two)))
	else:
		report('Type bug', 'Wrong type of value in box - should be an integer', 'Box labeled two has incorrect type ' + str(type(two)))
	sys.exit(1)

if not three == 3:
	if type(three) is int:
		report('Value bug', 'Wrong value in box', 'Box labeled one has incorrect value ' + str(repr(three)))
	else:
		report('Type bug', 'Wrong type of value in box - should be an integer', 'Box labeled two has incorrect type ' + str(type(three)))
	sys.exit(1)