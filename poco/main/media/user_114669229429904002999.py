#Module 4

#Challenge 4

'''
mean_applicantincome = float(sum_applicantincome_column)/len(int_applicantincome_column)
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

loan_table  = xdf_dict.values() # convert to final form
first_row = loan_table[0] 

int_applicantincome_column = [row['ApplicantIncome'] for row in loan_table]

sum_applicantincome_column = sum(int_applicantincome_column)

try:
	n = len(int_applicantincome_column)
        sum_applicantincome_column = sum(int_applicantincome_column)
        mean_applicantincome = sum_applicantincome_column/n
        
          

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	mean_applicantincome   # does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(mean_applicantincome, int):
	report('Data type bug', 'mean_applicantincome is not an int', 'No further help')
	sys.exit(1)

try:
	check = (mean_applicantincome == sum_applicantincome_column/len(int_applicantincome_column))  
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in mean_applicantincome of ' + str(mean_applicantincome), 'No further help available')
