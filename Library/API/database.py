"""
Maxwell Dulin 
Super Secure Library 
"""

import sqlite3
from abstract_database_connection import AbstractDatabaseConnection


create_statements = {
    # Create statement for album table.
    'author_sql' : """CREATE TABLE IF NOT EXISTS author (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );""", 
	'book_sql': """CREATE TABLE IF NOT EXISTS books ( 
		book_id INTEGER PRIMARY KEY AUTOINCREMENT, 
		author_id INTEGER, 
		title TEXT, 
		release_date INT, 
		FOREIGN KEY (author_id) REFERENCES author(author_id)
	);""",
	'library_sql': """CREATE TABLE library (
		book_id INTEGER PRIMARY KEY AUTOINCREMENT, 
		book_serial INTEGER,
		checked_out boolean, 
		FOREIGN KEY (book_serial) REFERENCES books(book_id)
	);""", 
	'secret': """CREATE TABLE secret ( 
		flag text
	); """
	
}

insert_statements = {
    # Insert statement for album table.
    'author insert' : """INSERT INTO author(name) VALUES
        ("JK Rowling")
    """,
	'book_insert_sql' : """INSERT INTO 	books(author_id,title, release_date) VALUES 
		(1, "Harry Potter I", 999302400),
		(1, "Harry Potter II", 100000000) 
	""", 
	'library_insert_sql': """INSERT INTO 	library(book_serial,checked_out) VALUES 
		(1,1) 
	""", 
	'flag text': """INSERT INTO secret(flag) 
		VALUES("flg{SQLi_1s_fUn}") 
		
	"""
}

def create_tables():
    """
    Creates all tables in the database.
    """
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
        for cs in create_statements:
            cursor.execute(create_statements[cs])
        conn.commit()

def seed():
    """
    Insert sample data to tables in the database.
    """
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
        for ins in insert_statements:
            cursor.execute(insert_statements[ins])
        conn.commit()

def delete_tables():

	with AbstractDatabaseConnection('library.db') as conn:
		cursor = conn.cursor()
		cursor.execute("""DROP TABLE IF EXISTS author""")
		cursor.execute("""DROP TABLE IF EXISTS books""")
		cursor.execute("""DROP TABLE IF EXISTS library""")
		cursor.execute("""DROP TABLE IF EXISTS secret""")
		conn.commit()
		
def test():
	with AbstractDatabaseConnection('library.db') as conn:
		cursor = conn.cursor()
		conn.commit()
		cursor.execute("""UPDATE library SET checked_out = 1 WHERE book_id = 1;""") 
	
def setup():
	"""
	Create and seed the database.
	"""
	delete_tables()
	create_tables()
	seed()
	test() 

if __name__ == '__main__':
    setup()