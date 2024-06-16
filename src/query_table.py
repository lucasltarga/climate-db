from sqlalchemy import text
import pandas as pd

def query_table(engine, query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        data = result.fetchall()
        columns = result.keys()
        return pd.DataFrame(data, columns=columns)