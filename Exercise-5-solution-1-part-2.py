#Part 2:	
import pandas as pd
#https://www.shanelynn.ie/python-pandas-read-csv-load-data-from-csv-files/
data = pd.read_csv('./data/6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

from nose.tools import ok_, assert_equal
import inspect
import sys

# Number of rows in the dataframe:
df = pd.DataFrame(data)
rows = df.shape[0]  # Gives number of rows
cols = df.shape[1]  # Gives number of columns
#print(df)

# Column names:
# https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
# https://www.geeksforgeeks.org/python-pandas-dataframe/
column_names = []
for col in df.columns:
    column_names.append(col)

# Column datatypes:
# https://datatofish.com/data-type-pandas-dataframe/
column_datatypes = []
for col in df.columns:
    column_datatypes.append(df[col].dtypes)

# Print the number of rows in the dataframe:
print('There are ' + str(rows) + ' rows')

# Print the column names:
print('The columns are: \n', column_names)

# Print the column datatypes:
print('The column types are: \n', column_datatypes)






