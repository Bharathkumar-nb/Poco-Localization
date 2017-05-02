#Module 7

#Challenge 7

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
	pa_converter		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not callable(pa_converter):
	report('Function error', 'pa_converter not a function', 'No further help available')
	sys.exit(1)

try:
	val = pa_converter({'Property_Area': 'Urban'})
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if val != 0:
		report('Function error', 'pa_converter returned wrong value for Urban: ' + str(val), 'No further help available')

try:
	val = pa_converter({'Property_Area': 'Rural'})
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if val != 1:
		report('Function error', 'pa_converter returned wrong value for Rural: ' + str(val), 'No further help available')

try:
	val = pa_converter({'Property_Area': 'Semiurban'})
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
else:
	if val != 2:
		report('Function error', 'pa_converter returned wrong value for Semiurban: ' + str(val), 'No further help available')

try:
	val = pa_converter({'Property_Area': 'Desert'})
except ValueError as e:
	if str(e) != 'Unknown property area type: ' + str(val):
		report('Function error', 'pa_converter did not do proper raise: ' + str(e), 'No further help available')
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
