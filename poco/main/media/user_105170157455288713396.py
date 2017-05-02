#Module 4

#Challenge 7

'''
lat = [row['Loan_Amount_Term'] for row in loan_table if row['Loan_Amount_Term'] != '']
plt.hist(lat, 5)  # same as before
plt.xlabel("Loan Term (in months)")
plt.ylabel("Number of applicants")
plt.title("Loan Term of Applicants")

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

import random
random.seed()

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

import pandas as pd # helps with handling csv formatted data
xurl = 'https://docs.google.com/spreadsheets/d/1_artlzgoj6pDBCBfdt9-Jmc9RT9yLsZ0vTnk3zJmt_E/pub?gid=1291197392&single=true&output=csv'
xdf = pd.read_csv(xurl)  # reads in the data from web
xdf_fill = xdf.fillna('') # replace empty values with empty string 
xdf_dict = xdf_fill.T.to_dict() # create dictionary

loan_table  = xdf_dict.values() # convert to final form

xloan_table = loan_table  # in case user screws with loan_table

# image dirs

target_url1 = '/home/poco/waggle-classroom/main/media/course_1/module_7/image_7/challenge7.png'
target_url2 = '/home/poco/waggle-classroom/main/media/tmp/attempt_4_7_{}_{}.png'.format(datetime.now(), random.random())

target_url1_dir = os.path.dirname(target_url1)

if not os.path.exists(target_url1_dir):
		os.makedirs(target_url1_dir)

import matplotlib.pyplot as plt

plt.close()
plt.cla()
plt.clf()

try:
	Loan_Amount_Term = [row['Loan_Amount_Term'] for row in loan_table if row['Loan_Amount_Term'] != '']
        plt.hist(Loan_Amount_Term, 5)
        plt.xlabel('Loan Term (in months)')
        plt.ylabel('Number of applicants')
        plt.title('Loan Term of Applicants')   
	# have to comment out the plt.show() function.
except TypeError as e:
	report('Type Error', 'This means did not skip over empties: TypeError: cannot perform reduce with flexible type', e)
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
except Exception as e:
	report('Generic error', 'Hist plot not set up correctly', e)
	sys.exit(1)

#plt.xlabel("Loan Term (in months)")
#plt.ylabel("Number of applicants")
#plt.title("Loan Term of Applicants")

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
	check = (xlab == "Loan Term (in months)")
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in xlabel of ' + str(xlab), 'No further help available')
		all_good = False

try:
	check = (title == "Loan Term of Applicants")
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in title of ' + str(title), 'No further help available')
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

	xlat = [row['Loan_Amount_Term'] for row in xloan_table if row['Loan_Amount_Term'] != '']
	plt.hist(xlat, 5)  # same as before
	plt.xlabel("Loan Term (in months)")
	plt.ylabel("Number of applicants")
	plt.title("Loan Term of Applicants")

	plt.savefig(target_url1)



	img1 = mpimg.imread(target_url1)  # answer
	img2 = mpimg.imread(target_url2)  #student submission

	img1 = img1.flatten()
	img2 = img2.flatten()

	if not np.array_equal(img1,img2): #True if two arrays have the same shape and elements, False otherwise.
		report('Value bug', 'Image does not match target', 'No further help available')
