#Module 6

#Challenge 5

'''
ch_table = [row for row in loan_table if row['Credit_History'] == '0']
outcomes = [1 if row['Loan_Status'] == 'Y' else 0 for row in ch_table]
plt.hist(outcomes, 2)  # same as before
plt.xlabel("0 = rejected, 1 = accepted")
plt.ylabel("Number of applicants")
plt.title("Outcome with Credit History 0")
plt.xticks([0,1])  # a list of ticks

ax = plt.gca() 
print(ax.get_ylabel())
print(ax.get_xlabel())
print(ax.get_title())
print(ax.get_xticks())

plt.show()
'''
import sys
import os
import matplotlib.image as mpimg
from datetime import datetime

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

# image dirs

target_url1 = '/home/smccumsey/waggle-classroom/main/media/course_1/module_9/image_5/challenge5.png'
target_url2 = '/home/smccumsey/waggle-classroom/main/media/tmp/attempt_6_5_{}.png'.format(datetime.now())

target_url1_dir = os.path.dirname(target_url1)

if not os.path.exists(target_url1_dir):
        os.makedirs(target_url1_dir)

import matplotlib.pyplot as plt

plt.close()
plt.cla()
plt.clf()

try:
	&&&  # paste user code here 
	# have to comment out the plt.show() function.
except TypeError as e:
	report('Type Error', 'Make sure ticks is a list', e)
	sys.exit(1)
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

# 'Credit History' for title
# 'Number of applicants' for ylabel
# 'Credit score' for xlabel

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
	check = (xlab == "0 = rejected, 1 = accepted")
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in xlabel of ' + str(xlab), 'No further help available')
		all_good = False

try:
	check = (title == "Outcome with Credit History 0")
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in title of ' + str(title), 'No further help available')
		all_good = False

try:
	check = (ticks.tolist() == [0,1])
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:	
		report('Value bug', 'Wrong value in xticks of ' + str(ticks), 'No further help available')
		all_good = False

if all_good:
    import matplotlib.image as mpimg
    import numpy as np
    from scipy.misc import imresize, toimage, imsave

    plt.savefig(target_url2)

    # plot solution
    plt.close()
    plt.cla()
    plt.clf()
    ch_table = [row for row in loan_table if row['Credit_History'] == '0']
    outcomes = [1 if row['Loan_Status'] == 'Y' else 0 for row in ch_table]
    plt.hist(outcomes, 2)  # same as before
    plt.xlabel("0 = rejected, 1 = accepted")
    plt.ylabel("Number of applicants")
    plt.title("Outcome with Credit History 0")
    plt.xticks([0,1])  # a list of ticks

    plt.savefig(target_url1)



    img1 = mpimg.imread(target_url1)  # answer
    img2 = mpimg.imread(target_url2)  #student submission

    img1 = img1.flatten()
    img2 = img2.flatten()

    if not np.array_equal(img1,img2): #True if two arrays have the same shape and elements, False otherwise.
        report('Value bug', 'Image does not match target', 'No further help available')
