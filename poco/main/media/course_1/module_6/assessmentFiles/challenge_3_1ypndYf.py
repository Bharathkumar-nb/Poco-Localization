#Module 3

#Challenge 3

'''
expensive_class1_table = [row for row in expensive_table if row['Pclass'] == '1']
'''
import sys

#d = {'Name': 'debugging', 'Short': 'check1', 'Long': 'nothing'}
#print(str(d))

def report( name, shortd, longd):
  d = {'Name': name, 'Short': shortd, 'Long': longd}
  print(str(d))

#Mock data goes first

xrow1 = {'Age': '22',
  'Embarked': 'S',
  'Fare': '7.25',
  'Name': 'Braund, Mr. Owen Harris',
  'Pclass': '3',
  'Sex': 'male',
  'Survived': '0'
}

xrow2 = {'Age': '38',
  'Embarked': 'C',
  'Fare': '71.2833',
  'Name': 'Cuming, Mrs. John Bradley (Florence Briggs Thayer)',
  'Pclass': '1',
  'Sex': 'female',
  'Survived': '1'
}

xrow3 = {'Age': '26',
  'Embarked': 'S',
  'Fare': '7.925',
  'Name': 'Heikkinen, Miss. Laina',
  'Pclass': '3',
  'Sex': 'female',
  'Survived': '1'
}

xrow4 = {'Age': '2',
  'Embarked': 'S',
  'Fare': '21.075',
  'Name': 'Palsson, Master. Gosta Leonard',
  'Pclass': '3',
  'Sex': 'male',
  'Survived': '0'
}
 
xrow5 = {'Age': '14',
  'Embarked': 'C',
  'Fare': '30.0708',
  'Name': 'Nasser, Mrs. Nicholas (Adele Achem)',
  'Pclass': '2',
  'Sex': 'female',
  'Survived': '1'
}

xrow6 = {'Age': '4',
  'Embarked': 'S',
  'Fare': '16.7',
  'Name': 'Sandstrom, Miss. Marguerite Rut',
  'Pclass': '3',
  'Sex': 'female',
  'Survived': '1'
}

xrow7 = {'Age': '58',
  'Embarked': 'S',
  'Fare': '26.55',
  'Name': 'Bonnell, Miss. Elizabeth',
  'Pclass': '1',
  'Sex': 'female',
  'Survived': '1'
}

titanic_starter_table = [xrow1, xrow2, xrow3, xrow4, xrow5, xrow6, xrow7]

expensive_table = [row for row in titanic_starter_table if float(row['Fare'])>30]

try:
	&&&  # paste user code here

except Exception as e:
	report('Generic error', 'On your own', e)
	sys.exit(1)

try:
	expensive_class1_table		# does var exist?
except NameError as e:
	report('Name error', 'Typically a typo', e)
	sys.exit(1)

if not isinstance(expensive_class1_table, list):
	report('Data type bug', 'expensive_class1_table is not a list', 'No further help available')
	sys.exit(1)

if len(expensive_class1_table) != 1:
	report('Length bug', 'expensive_class1_table should have length of 1 but has length ' + str(len(expensive_class1_table)), 'Remember to quote the 1 - it is a string')
	sys.exit(1)

try:
	check = (expensive_class1_table == [row for row in expensive_table if row['Pclass']=='1'])
except Exception as e:
	report('Generic error', 'On your own', e)
else:
	if not check:
		report('Value bug', 'Wrong value in expensive_class1_table of ' + str(expensive_class1_table), 'No further help available')
