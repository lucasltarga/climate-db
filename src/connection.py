from sqlalchemy import create_engine

def get_engine(config):
    db_url = ''
    if config['db_type'] == 'mysql':
        db_url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    elif config['db_type'] == 'postgresql':
        db_url = f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    return create_engine(db_url)

def test_connection(engine):
    try:
        conn = engine.connect()
        conn.close()
        return True
    except:
        return False