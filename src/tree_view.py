from rich.tree import Tree
from sqlalchemy import inspect

def get_db_tree(engine):
    '''
    Uses the Tree class of rich module to generate a tree visualization of the database 
    including tables, views and columns details like name, type and if it is a primary key.
    
    Structure example:
    Table1: table_name
        column1 (type(size)) PK

        column2 (type(size))

    Table2: table2_name
        column3 (type(size)) PK

        column4 (type(size))
    '''
    inspector = inspect(engine)
    tree = Tree("Database Schema")
    
    for table_name in inspector.get_table_names():
        primary_keys = inspector.get_pk_constraint(table_name)['constrained_columns']
       
        table_tree = tree.add(f"Table: {table_name}")
        for column in inspector.get_columns(table_name):
            column_info = f"{column['name']} ({column['type']})"
            if column['name'] in primary_keys:
                column_info += " PK"
            table_tree.add(column_info)
    
    for view_name in inspector.get_view_names():
        view_tree = tree.add(f"View: {view_name}")
        for column in inspector.get_columns(view_name):
            column_info = f"{column['name']} ({column['type']})"
            view_tree.add(column_info)
    
    return tree