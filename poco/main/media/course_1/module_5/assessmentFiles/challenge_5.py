#Module 2

#Challenge 5

'''
sum_all_ages = sum(int_all_ages)
'''

import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

row1 = {'Age': '22',
  'Embarked': 'S',
  'Fare': '7.25',
  'Name': 'Braund, Mr. Owen Harris',
  'Pclass': '3',
  'Sex': 'male',
  'Survived': '0'
}

row2 = {'Age': '38',
  'Embarked': 'C',
  'Fare': '71.2833',
  'Name': 'Cuming, Mrs. John Bradley (Florence Briggs Thayer)',
  'Pclass': '1',
  'Sex': 'female',
  'Survived': '1'
}

row3 = {'Age': '26',
  'Embarked': 'S',
  'Fare': '7.925',
  'Name': 'Heikkinen, Miss. Laina',
  'Pclass': '3',
  'Sex': 'female',
  'Survived': '1'
}

row4 = {'Age': '2',
  'Embarked': 'S',
  'Fare': '21.075',
  'Name': 'Palsson, Master. Gosta Leonard',
  'Pclass': '3',
  'Sex': 'male',
  'Survived': '0'
}

row5 = {'Age': '14',
  'Embarked': 'C',
  'Fare': '30.0708',
  'Name': 'Nasser, Mrs. Nicholas (Adele Achem)',
  'Pclass': '2',
  'Sex': 'female',
  'Survived': '1'
}

row6 = {'Age': '4',
  'Embarked': 'S',
  'Fare': '16.7',
  'Name': 'Sandstrom, Miss. Marguerite Rut',
  'Pclass': '3',
  'Sex': 'female',
  'Survived': '1'
}

row7 = {'Age': '58',
  'Embarked': 'S',
  'Fare': '26.55',
  'Name': 'Bonnell, Miss. Elizabeth',
  'Pclass': '1',
  'Sex': 'female',
  'Survived': '1'
}

titanic_starter_table = [row1, row2, row3, row4, row5, row6, row7]

raw_age_column = [person['Age'] for person in titanic_starter_table]

int_all_ages = [int(age) for age in raw_age_column]

try:
	&&&  # paste user code here

except TypeError as e:
	report('Key error', 'Check for correct argument to sum function', e)
except NameError as e:
	report('Name error', 'Look for typos in variable names', e)
except Exception as e:
	report('Generic error', 'On your own - review reducing a list with sum', e)
	sys.exit(1)

try:
	sum_all_ages		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(sum_all_ages, int):
	report('Data type bug', 'int_all_ages is not an int', 'No further help available')
	sys.exit(1)

try:
	check = (sum_all_ages == sum(int_all_ages)
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in int_all_ages of ' + str(sum_all_ages), 'No further help available')
