#Module 1

#Challenge 8

'''
int_x = int(x)
float_y = float(y)
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

x = '42' 
y = '-.06'

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	check = (int_x == int(x))
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if type(int_x) is not int:
		report('Type bug', 'Type of int_x is not an int but instead a ' + str(type(int_x)), 'No further help available.')
	elif not check:
		report('Value bug', 'Wrong value in box int_x of ' + str(int_x), 'No further help available')

try:
	check = (float_y == float(y))
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if type(float_y) is not float:
		report('Type bug', 'Type of float_y is not a float but instead a ' + str(type(float_y)), 'No further help available.')
	elif not check:
		report('Value bug', 'Wrong value in box float_y of ' + str(float_y), 'No further help available')


	