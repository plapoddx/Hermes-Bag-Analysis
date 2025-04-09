from sqlalchemy import create_engine
import pandas as pd

user = 'user'
password = 'pw'
host = 'host'
port ='port'
db = 'db'


def connect_postgres(user, password, host, port, db):
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

#Dataframe to PostgreSQL Database

def pipe_to_sql(df, table_name, schema):
    try:
        df.to_sql(name=table_name, con=connect_postgres(user, password, host, port, db), schema = schema, if_exists='append', index=False)
        print(f"✅ Successfully saved DataFrame to '{table_name}' table.")
    except Exception as e:
        print(f"❌ Error saving to SQL: {e}")
