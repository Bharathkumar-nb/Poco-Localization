#Module 5

#Challenge 7

'''

'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

import pandas as pd
xurl = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
xdf = pd.read_csv(xurl)  # reads in the data from web
xdf_fill = xdf.fillna('') # replace empty values with empty string 
xdf_dict = xdf_fill.T.to_dict() # create dictionary

xloan_table  = xdf_dict.values() # convert to final form

loan_table = xloan_table 

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	beyond_the_walls   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(beyond_the_walls, float):
	report('Data type bug', 'beyond_the_walls is not a float', 'No further help available')
	sys.exit(1)

# First the average or mean

xtarget_column = [passenger['LoanAmount'] for passenger in loan_table if passenger['LoanAmount'] != '']
xn = len(xtarget_column)
xtotal = sum (xtarget_column)  # the numerator of the fraction above
xcolumn_average = xtotal/xn  # the "x bar" above

# Then the standard deviation

xsquared_diff_list = [(xi - xcolumn_average)**2 for xi in xtarget_column]  # **2 will square a number
xsqd_total = sum(xsquared_diff_list)
xvariance = xsqd_total/xn  # or 1/N * total if you prefer
xsn = xvariance**.5

# The walls

xsigma3 = 3 * xsn
xlow_wall = xcolumn_average - xsigma3
xhigh_wall = xcolumn_average + xsigma3

# The outliers

xlow_outliers = [xi for xi in xtarget_column if xi < xlow_wall]
xhigh_outliers = [xi for xi in xtarget_column if xi > xhigh_wall]
xtotal_outliers = len(xlow_outliers) + len(xhigh_outliers)

xbeyond_the_walls = (1.0*xtotal_outliers/n)/(1.0/370)

try:
	check = (beyond_the_walls == xbeyond_the_walls)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in beyond_the_walls: ' + str(beyond_the_walls), 'No further help available')
