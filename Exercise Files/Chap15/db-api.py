#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sqlite3 as sq

def main():
    print('connect')
    
    '''
    To create a databases using the connect() function of the sqlite3 module.
    db is the connection object.
    '''
    db = sq.connect('db-api.db')
    
    '''
    Create a Cursor object to call its execute() method to perform SQL commands:
    '''
    cur = db.cursor()
    
    print('create')
    
    '''
    Executes an SQL statement using execute()
    
    DROP TABLE IF EXISTS SQL statement checks if the table exists prior to drop/delete it 
    '''
    cur.execute("DROP TABLE IF EXISTS test")
    
    '''
    CREATE TABLE() to create a table
    '''
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    '''
    to save the table use commit()
    '''
    db.commit()
    
    print('count')
    
    '''
    SELECT COUNT find the number of products
    '''
    cur.execute("SELECT COUNT(*) FROM test")
    
    
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()
