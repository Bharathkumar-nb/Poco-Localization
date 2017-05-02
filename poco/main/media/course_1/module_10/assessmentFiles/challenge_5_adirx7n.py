#Module 7

#Challenge 5

'''
import matplotlib.pyplot as plt

amount = [int(row['Credit_History']) for row in loan_table if row['Credit_History'] != '']
plt.hist(amount, 2)  # same as before
plt.xlabel("Credit score")
plt.ylabel("Number of applicants")
plt.title("Credit History")
plt.xticks([0,1])  # a list of ticks

plt.show()  # This needs to be commented out of user code
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

from csv import DictReader # helps with handling csv formatted data
from urllib2 import urlopen # helps with pulling data off the web
url = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
response = urlopen(url)
loan_table = [row for row in DictReader(response)]  # a mapping function using identity

xloan_table = loan_table  # in case user screws with loan_table

no_by_gender = [row['Gender'] for row in loan_table if row['Loan_Status'] == 'N']
yes_by_gender = [row['Gender'] for row in loan_table if row['Loan_Status'] == 'Y']

yes_by_int = [0 if item == 'Male' else 1 for item in yes_by_gender if item != '']
no_by_int = [0 if item == 'Male' else 1 for item in no_by_gender if item != '']

from datetime import datetime

target_url1 = '/home/smccumsey/waggle-classroom/main/media/course_1/module_10/image_5/challenge5.png'
target_url2 = '/home/smccumsey/waggle-classroom/main/media/tmp/attempt_7_5_{}.png'.format(datetime.now())

import matplotlib.pyplot as plt

plt.close()
plt.cla()
plt.clf()

try:
        &&&  # paste user code here 
        plt.savefig(target_url2)

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	ax = plt.gca()
	fig = plt.gcf()
	ylab= ax.get_ylabel()
	xlab = ax.get_xlabel()
	title = ax.get_title()
	ticks = ax.get_xticks()
except Exception as e:
	report('Generic error', 'Hist plot not set up correctly', e)
	sys.exit(1)
	
'''
* 'Success by gender' for title
* 'Number of applicants' for ylabel
* 'Gender - 0 is male' for xlabel
* <code>['Successful','Unsuccessful']</code> for legend.
* <code>[0,1]</code> for xticks.
'''

all_good = True  # set False if anything does not match

try:
	check = (ylab == 'Number of applicants')
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in ylabel of ' + str(ylab), 'No further help available')
		all_good = False

try:
	check = (xlab == 'Gender - 0 is male')
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in xlabel of ' + str(xlab), 'No further help available')
		all_good = False

try:
	check = (title == 'Success by gender')
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in title of ' + str(title), 'No further help available')
		all_good = False

try:
	check = (ticks == [0,1])
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:	
		report('Value bug', 'Wrong value in xticks of ' + str(ticks), 'No further help available')
		all_good = False

if not all_good:
	sys.exit(1)

plt.close()
plt.cla()
plt.clf()

plt.hist([yes_by_int,no_by_int], 2, stacked=True, label=['Successful','Unsuccessful'])

plt.xlabel("Gender - 0 is male")
plt.ylabel("Number of applicants")
plt.title("Success by gender")
plt.xticks([0,1])

plt.legend()  # this is new - it uses the label values from the list above

plt.savefig(target_url1)

import matplotlib.image as mpimg
import numpy as np

img1 = mpimg.imread(target_url1)  # answer
img2 = mpimg.imread(target_url2)  #student submission

img1 = img1.flatten()
img2 = img2.flatten()

if not np.array_equal(img1,img2): #True if two arrays have the same shape and elements, False otherwise.
    report('Value bug', 'Image does not match target', 'No further help available')
