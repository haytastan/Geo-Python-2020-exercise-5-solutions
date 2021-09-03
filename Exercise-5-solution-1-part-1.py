#Part 1:
import pandas as pd
#https://www.shanelynn.ie/python-pandas-read-csv-load-data-from-csv-files/
data = pd.read_csv('./data/6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])
print(data)

from nose.tools import ok_, assert_equal
import inspect
import sys

# Check that pandas module is imported
if ok_('pandas' in sys.modules):
    print('Pandas module is not imported')
else:
    print('Pandas module is imported')

# Check that the variable data exists:
if ok_('data' in locals()):
    print('the variable data does not exist')
else:
    print('the variable data exists')