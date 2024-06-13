import os
import json

CONFIG_FILE = 'config/db_config.json'

def save_db_config(db_type, host, port, user, password, database):
    config = {
        'db_type': db_type,
        'host': host,
        'port': port,
        'user': user,
        'password': password,
        'database': database
    }
    
    os.makedirs('config', exist_ok=True)
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def load_db_config():
    with open(CONFIG_FILE, 'r') as file:
        return json.load(file)