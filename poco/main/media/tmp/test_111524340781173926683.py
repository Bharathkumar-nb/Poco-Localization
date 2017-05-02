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
	one = 'kjeshkjfhs'
        two = 2
        three=3
        
        
        
        
          

except IndentationError as e:
	report('Indentation error', 'Make sure each line of code starts in column 1', e)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	check = (one == 1)
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		if type(one) is int:
			report('Value bug', 'Wrong value in box', 'Box labeled one has incorrect value ' + str(repr(one)))
		else:
			report('Type bug', 'Wrong type of value in box', 'Box labeled one has incorrect type ' + str(type(one)))

try:
	check = (two == 2)
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled two has incorrect value ' + str(repr(two)))

try:
	check = (three == 3)
except NameError as e:
	report('Name error', 'Typically a typo', e)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in box', 'Box labeled three has incorrect value ' + str(repr(three)))
	