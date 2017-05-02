#Module 6

#Challenge 4

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

try:
	'''
	&&& 
	'''
	'done'

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)
