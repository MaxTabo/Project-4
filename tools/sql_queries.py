from config.sql_connection import engine
import pandas as pd



def get_everything ():
    query = """SELECT * FROM anisql;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_name (name):
    query = f"""SELECT * 
    FROM anisql
    WHERE name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_text (name):
    query = f"""SELECT text 
    FROM anisql
    WHERE name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_compound (name):
    query = f"""SELECT anisql.name,avg(compound) FROM project4.anisql
where anisql.name='{name}'
group by name;"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


#POST



def insert_one_row (name, text, compound):
    query = f"""INSERT INTO anisql
     (name, text, compound) 
        VALUES ('{name}', '{text}', {compound});
    """
    engine.execute(query)
    return f"YOU ARE A POST MASTER!"

def delete_row(name):
    query=f"""DELETE FROM anisql
     WHERE name='{name}';
    """
    engine.execute(query)
    return f"You have deleted your post!"




