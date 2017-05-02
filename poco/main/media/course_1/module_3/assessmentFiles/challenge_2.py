#Module 0

#Challenge 2

'''
x = '23'
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first


try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', 'Look for typos')
	sys.exit(1)

try:
	y		# does var exist?
except NameError as e:
	report('Name error', "Don't see y on left", 'Look for typos')
	sys.exit(1)

if not isinstance(y, str):
	report('Data type bug', "Did you type the '23' correctly?", 'It should have quotes around it')
	sys.exit(1)

try:
	check = (y == '23')
except Exception as e:
	report('Generic error', "On your own", 'Look for typos')
else:
	if not check:
		report('Value bug', "'Did you type '23' with quotes?", 'Look for typos')
