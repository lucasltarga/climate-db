from sqlalchemy import text
import pandas as pd

def query_table(engine, table, limit):
    query = f"SELECT * FROM {table} LIMIT {limit}"
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return pd.DataFrame(result.fetchall(), columns=result.keys())