import typer
from rich import print
from rich.table import Table

from config.db_config import save_db_config, load_db_config
from connection import get_engine, test_connection
from tree_view import get_db_tree
from query_table import query_table
from display_table import display_table

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
def query(table, limit = 1000):
    config = load_db_config()
    engine = get_engine(config)
    df = query_table(engine, table, limit)
    display_table(df)

if __name__ == "__main__":
    app()