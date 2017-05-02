#Module 3

#Challenge 6

'''
xfemale_ages = [row['Age'] for row in titanic_starter_table if row['Sex'] == 'female']
check = (average_female_age == sum(xfemale_ages)/len(xfemale_ages))
'''
import sys

def report( name, shortd, longd):
	d = {'Name': name, 'Short': shortd, 'Long': longd}
	print(str(d))

#Mock data goes first

row1 = {'Age': 22,
	'Embarked': 'S',
	'Fare': 7.25,
	'Name': 'Braund, Mr. Owen Harris',
	'Pclass': 3,
	'Sex': 'male',
	'Survived': 0
}

row2 = {'Age': 38,
	'Embarked': 'C',
	'Fare': 71.2833,
	'Name': 'Cuming, Mrs. John Bradley (Florence Briggs Thayer)',
	'Pclass': 1,
	'Sex': 'female',
	'Survived': 1
}

row3 = {'Age': 26,
	'Embarked': 'S',
	'Fare': 7.925,
	'Name': 'Heikkinen, Miss. Laina',
	'Pclass': 3,
	'Sex': 'female',
	'Survived': 1
}

row4 = {'Age': 2,
	'Embarked': 'S',
	'Fare': 21.075,
	'Name': 'Palsson, Master. Gosta Leonard',
	'Pclass': 3,
	'Sex': 'male',
	'Survived': 0
}

row5 = {'Age': 14,
	'Embarked': 'C',
	'Fare': 30.0708,
	'Name': 'Nasser, Mrs. Nicholas (Adele Achem)',
	'Pclass': 2,
	'Sex': 'female',
	'Survived': 1
}

row6 = {'Age': 4,
	'Embarked': 'S',
	'Fare': 16.7,
	'Name': 'Sandstrom, Miss. Marguerite Rut',
	'Pclass': 3,
	'Sex': 'female',
	'Survived': 1
}

row7 = {'Age': 58,
	'Embarked': 'S',
	'Fare': 26.55,
	'Name': 'Bonnell, Miss. Elizabeth',
	'Pclass': 1,
	'Sex': 'female',
	'Survived': 1
}

titanic_starter_table = [row1, row2, row3, row4, row5, row6, row7]

try:
	female_ages =[row['Age'] for row in titanic_starter_table if row['Sex'] == 'female']
        n = len(female_ages)
        total = sum (female_ages)
        average_female_age = total/n  

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	average_female_age		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(average_female_age, int):
	report('Data type bug', 'average_female_age is not an int', 'No further help available')
	sys.exit(1)

try:
	xfemale_ages = [row['Age'] for row in titanic_starter_table if row['Sex'] == 'female']
	check = (average_female_age == sum(xfemale_ages)/len(xfemale_ages))
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in average_female_age of ' + str(average_female_age), 'No further help available')
