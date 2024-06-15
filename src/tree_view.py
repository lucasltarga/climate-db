from rich.tree import Tree
from sqlalchemy import inspect

def get_db_tree(engine):
    inspector = inspect(engine)
    tree = Tree("Database Schema")
    
    for table_name in inspector.get_table_names():
        table_tree = tree.add(f"Table: {table_name}")
        for column in inspector.get_columns(table_name):
            column_info = f"{column['name']} ({column['type']})"
            table_tree.add(column_info)
    
    for view_name in inspector.get_view_names():
        view_tree = tree.add(f"View: {view_name}")
        for column in inspector.get_columns(view_name):
            column_info = f"{column['name']} ({column['type']})"
            view_tree.add(column_info)
    
    return tree