#Module 0

#Challenge 1

'''
x = 23
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
    x		# does var exist?
except NameError as e:
    report('Name error', "Don't see x on left - typo?", 'Look for typos')
    sys.exit(1)

if not isinstance(x, int):
    report('Data type bug', 'Did you type the 23 correctly?', 'No further help available')
    sys.exit(1)

try:
    check = (x == 23)
except Exception as e:
    report('Generic error', 'On your own', 'Look for typos')
else:
    if not check:
        report('Value bug', 'Did you type the 23 correctly?', 'Look for typos')
