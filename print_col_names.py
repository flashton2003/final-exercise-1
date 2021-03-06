# EXERCISE INSTRUCTIONS
# This script should output a list of column names from a CSV file with any spaces replaced by underscores (the '_' character)
# This script was started by someone else, and you've been asked to fix any errors and provide this functionality

import pandas

def remove_whitespace(each, replace):
        each = each.split()
	each = '_'.join(each)
	return each
	#return each.replace(' ', replace)

def test_what_whitespace(each):
	each = each.strip()
	try:
		assert len(each.split(' ')) == len(each.split())
	except AssertionError:
		print '''
ERROR ERROR ERROR
you might have tabs or other whitespace than single spaces
ERROR ERROR ERROR
'''


data = pandas.read_csv("weather_data/pa_weather_year.csv")
new_col_names = []
col_names = data.columns.values.tolist()
for each in col_names:
	each = each.strip()
	#test_what_whitespace(each)
	new_col_names.append(remove_whitespace(each, '_'))

outhandle = open('columnNames', 'w')

for each in new_col_names:
	test_what_whitespace(each)
	outhandle.write('%s\n' % each)


# STEP 1 - Define a function below called "replace_whitespace" that can replace characters in a string with others. The function should take two parameters, the first being the string that needs whitespace characters replacing, and the second being the character to insert instead of the whitespace.



# STEP 2 - output the new column names generated by running your replace_whitespace function
# BONUS - trim any leading (at the front of the string) or trailing (at the end) whitespace characters from each column name before you call your replace_whitespace function



# STEP 3 - Using the shell:
# (a) write ONLY the new non-whitespace column names to a new file called columnNames instead of the shell output (stdout)
# (b) similarly, sort the outputted column names into a new file called sortedColumnNames

# Push the following files to Aleksandra's github: this file containing the fixed code, file with the column names with spaces removed, and the file with the sorted names
# This will raise a pull request, so we can check your script
