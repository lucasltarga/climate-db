from tabulate import tabulate
from sqlalchemy import text
import pandas as pd
import os

from export_data import export_to_csv, export_to_json

def display_table(dataframe):
    '''Displays table from a dataframe using "psql" tabulate library format.'''
    print(tabulate(dataframe, headers='keys', tablefmt='psql'))

def get_table_data(engine, table, limit):
        query = f"SELECT * FROM {table} LIMIT {limit}"
        with engine.connect() as connection:
            result = connection.execute(text(query))
            data = result.fetchall()
            columns = result.keys()
            df = pd.DataFrame(data, columns=columns)
             
            return df