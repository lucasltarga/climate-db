from tabulate import tabulate

def display_table(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='psql'))