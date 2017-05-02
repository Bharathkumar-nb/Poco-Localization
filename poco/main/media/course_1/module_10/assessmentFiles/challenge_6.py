#Module 7

#Challenge 6

'''
Write a few sentences.
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

try:
	'''
	&&&  # paste user code here - have to comment out the plt.show() function.
	'''
	'Got it'

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
