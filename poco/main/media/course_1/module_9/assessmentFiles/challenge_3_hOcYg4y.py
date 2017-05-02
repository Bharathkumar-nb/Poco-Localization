#Module 6

#Challenge 3

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

int_scores = [int(row['Credit_History']) for row in xloan_table if row['Credit_History'] != '']

# image dirs

target_url1 = '/home/smccumsey/waggle-classroom/waggle/media/course_1/module_9/image_3/challenge3.png'
target_url2 = '/home/smccumsey/waggle-classroom/waggle/media/tmp/attempt_6_3.png'

import matplotlib.pyplot as plt

plt.close()
plt.cla()
plt.clf()

try:
	&&&  # paste user code here 
        # have to comment out the plt.show() function.
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
	check = (xlab == 'Credit score')
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in xlabel of ' + str(xlab), 'No further help available')
		all_good = False

try:
	check = (title == 'Credit History')
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
	if not check.all():	
		report('Value bug', 'Wrong value in xticks of ' + str(ticks), 'No further help available')
		all_good = False

if all_good:
	import matplotlib.image as mpimg
	import numpy as np


	img1 = mpimg.imread(target_url1)  # answer
	img2 = mpimg.imread(target_url2)  #student submission
        
        img1 = img1.resize((100,100))
        img2 = img2.resize((100,100))
        

	if not np.array_equal(img1,img2): #True if two arrays have the same shape and elements, False otherwise.
		report('Value bug', 'Image does not match target', 'No further help available')
