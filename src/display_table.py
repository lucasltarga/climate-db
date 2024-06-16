from tabulate import tabulate
from sqlalchemy import text
import pandas as pd

def display_table(dataframe):
    '''Displays table from a dataframe using "psql" tabulate library format.'''
    print(tabulate(dataframe, headers='keys', tablefmt='psql'))

def show_table_data(engine, table, limit):
        query = f"SELECT * FROM {table} LIMIT {limit}"
        with engine.connect() as connection:
            result = connection.execute(text(query))
            data = result.fetchall()
            columns = result.keys()
            return pd.DataFrame(data, columns=columns)