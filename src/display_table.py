from tabulate import tabulate
from sqlalchemy import text
import pandas as pd

def display_table(dataframe):
    '''Displays table from a dataframe using "psql" tabulate library format.'''
    print(tabulate(dataframe, headers='keys', tablefmt='psql'))