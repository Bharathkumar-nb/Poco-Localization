#Module 0

#Challenge 3

'''
z = {'x': x, 'y': y, 'Foo': 'Bar'}
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

x = 23
y = '23'

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'Lots of fussy syntax to get right', 'Look for typos')
	sys.exit(1)

try:
	z		# does var exist?
except NameError as e:
	report('Name error', "Did you put quotes in all the right places?", 'Look for typos')
	sys.exit(1)

if not isinstance(z, dict):
	report('Data type bug', "Did you type the {...} correctly?", 'Lots of fussy syntax to get right')
	sys.exit(1)

try:
	check = (z['x'] == x)
except KeyError as e:
  report('Key error', "Did you type 'x': x correctly?", 'Look for typos - watch those quotes')
except Exception as e:
	report('Generic error', "On your own", 'Look for typos')
else:
	if not check:
		report('Value bug', "Did you type 'x': x correctly?", 'Look for typos - watch those quotes')

try:
  check = (z['y'] == y)
except KeyError as e:
  report('Key error', "Did you type 'y': y correctly?", 'Look for typos - watch those quotes')
except Exception as e:
  report('Generic error', "On your own", 'Look for typos')
else:
  if not check:
    report('Value bug', "Did you type 'y': y correctly?", 'Look for typos - watch those quotes')

try:
  check = (z['Foo'] == 'Bar')
except KeyError as e:
  report('Key error', "Did you type 'Foo': 'Bar' correctly?", 'Look for typos - case matters')
except Exception as e:
  report('Generic error', "On your own", 'Look for typos')
else:
  if not check:
    report('Value bug', "Did you type 'Foo': 'Bar' correctly?", 'Look for typos - case matters')

try:
  check = (len(z) == 3)
except Exception as e:
  report('Generic error', "On your own", 'Look for typos')
else:
  if not check:
    report('Length bug', "Not an exact match of what is needed. Too little or too much.", 'Missing something?')
