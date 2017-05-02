#Module 5

#Challenge 4

'''
# First the average or mean

target_column = [passenger['Loan_Amount_Term'] for passenger in loan_table if passenger['Loan_Amount_Term'] != '']
n = len(target_column)
total = sum (target_column)  # the numerator of the fraction above
column_average = total/n  # the "x bar" above

# Then the standard deviation

squared_diff_list = [(xi - column_average)**2 for xi in target_column]  # **2 will square a number
sqd_total = sum(squared_diff_list)
variance = sqd_total/n  # or 1/N * total if you prefer
sn = variance**.5

# The walls

sigma3 = 3 * sn
low_wall = column_average - sigma3
high_wall = column_average + sigma3

# The outliers

low_outliers = [xi for xi in target_column if xi < low_wall]
high_outliers = [xi for xi in target_column if xi > high_wall]
total_outliers = len(low_outliers) + len(high_outliers)
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
	total_outliers   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(total_outliers, int):
	report('Data type bug', 'total_outliers is not an int', 'No further help available')
	sys.exit(1)

# First the average or mean

xtarget_column = [passenger['Loan_Amount_Term'] for passenger in xloan_table if passenger['Loan_Amount_Term'] != '']
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

try:
	check = (total_outliers == xtotal_outliers)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in total_outliers: ' + str(total_outliers), 'No further help available')
