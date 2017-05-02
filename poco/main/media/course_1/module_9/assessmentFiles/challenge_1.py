#Module 6

#Challenge 2

'''
import matplotlib.pyplot as plt
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	plt		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(plt, object):
	report('Data type bug', 'plt is not an imported package - review import syntax', 'No further help available')
	sys.exit(1)
