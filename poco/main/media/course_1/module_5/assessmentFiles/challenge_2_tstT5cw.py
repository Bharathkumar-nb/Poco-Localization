#Module 2

#Challenge 2

'''
miss_s_age = miss_s['Age']
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

miss_s = row6

try:
	&&&  # paste user code here

except KeyError as e:
	report('Key error', 'Check spelling of your key', e)
except NameError as e:
	report('Name error', 'Keys should be strings and watch for typos', e)
except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	miss_s_age		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(miss_s_age, str):
	report('Data type bug', 'miss_s_age is not a string', 'No further help available')
	sys.exit(1)

try:
	check = (miss_s_age == row6['Age'])
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in miss_s of ' + str(repl(miss_s)), 'No further help available')
