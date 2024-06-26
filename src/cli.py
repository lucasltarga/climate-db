import typer
import os
from rich import print
from rich.table import Table


from config.db_config import save_db_config, load_db_config
from connection import get_engine, test_connection
from tree_view import get_db_tree
from query_table import query_table
from display_table import display_table, get_table_data
from export_data import export_to_csv, export_to_json

app = typer.Typer()

@app.command()
def configure(db_type: str, host: str, port: int, user: str, password: str, database: str):
    save_db_config(db_type, host, port, user, password, database)
    print("[green] Configuration saved successfully [/green]")

@app.command()
def test():
    config = load_db_config()
    engine = get_engine(config)
    if test_connection(engine):
        print("[green] Connection successful. [/green]")
    else:
        print("[red] Connection failed. [/red]")

@app.command()
def show_tree():
    config = load_db_config()
    engine = get_engine(config)
    tree = get_db_tree(engine)
    print(tree)

@app.command()
def query(query):
    config = load_db_config()
    engine = get_engine(config)
    df = query_table(engine, query)
    display_table(df)

@app.command()
def show_table(table, limit = 1000):
    config = load_db_config()
    engine = get_engine(config)
    df = get_table_data(engine, table, limit)
    display_table(df)

@app.command()
def export_query(sql: str, file_type: str = "json"):    
    os.makedirs('../data', exist_ok=True)
    file_path = "../data/export"

    config = load_db_config()
    engine = get_engine(config)
    df = query_table(engine, sql)
    if file_type.lower() == 'csv':
        export_to_csv(df, file_path)
    elif file_type.lower() == 'json':
        export_to_json(df, file_path)
    print(f"[green]Data exported to {file_path}[/green]")

@app.command()
def export_table(table, limit = 1000, file_type = "json"):
    os.makedirs('../data', exist_ok=True)
    file_path = "../data/export"
    
    config = load_db_config()
    engine = get_engine(config)
    df = get_table_data(engine, table, limit)

    if file_type.lower() == "csv":
        export_to_csv(df, file_path)
        print("[green] Data exported to ../data/export [/green]")
    if file_type.lower() == "json":
        export_to_json(df, file_path)
        print("[green] Data exported to ../data/export [/green]")

if __name__ == "__main__":
    app()