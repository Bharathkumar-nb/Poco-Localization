#Module 4

#Challenge 1

'''
from csv import DictReader # helps with handling csv formatted data

from urllib2 import urlopen # helps with pulling data off the web

url = 'https://www.dropbox.com/s/ki8tr9c0gomfi3e/Iris.csv?raw=1'

response = urlopen(url)

iris_table = [row for row in DictReader(response)] 
from csv import DictReader # helps with handling csv formatted data

from urllib2 import urlopen # helps with pulling data off the web

url = 'https://www.dropbox.com/s/ki8tr9c0gomfi3e/Iris.csv?raw=1'

response = urlopen(url)

iris_table = [row for row in DictReader(response)]  # a mapping function using identity

first_row = iris_table[0]

{'PetalLengthCm': '1.4', 'SepalLengthCm': '5.1', 'Id': '1', 'PetalWidthCm': '0.2', 'SepalWidthCm': '3.5', 'Species': 'Iris-setosa'}
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

xrow1 = {'PetalLengthCm': '1.4', 'SepalLengthCm': '5.1', 'Id': '1', 'PetalWidthCm': '0.2', 'SepalWidthCm': '3.5', 'Species': 'Iris-setosa'}

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
  iris_table   # does var exist?
except NameError as e:
  report('Name error', 'Typically a typo', e)
  sys.exit(1)

if not isinstance(first_row, dict):
  report('Data type bug', 'iris_table is not a list', 'No further help available')
  sys.exit(1)

if len(iris_table) != 150:
  report('Length bug', 'iris_table has incorrect number of rows ' + str(len(iris_table)), 'No further help available')
  sys.exit(1)

try:
	first_row		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(first_row, dict):
	report('Data type bug', 'first_row is not a dict', 'No further help available')
	sys.exit(1)

try:
	check = (first_row == xrow1)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in first_row of ' + str(first_row), 'No further help available')
