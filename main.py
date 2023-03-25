# база_данных
# sql - язык структурированных данных
# СУБД-системы управления баз данных
# реляционные
# CRUD CREATE REED UPDATE DELETE

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


global connection
database = r'puge.db'
connection = create_connection(database)


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def read(conn):
    try:
        sql = 'SELECT * FROM student'
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for i in rows:
            print(i)
    except Error as e:
        print(e)


def create_student(conn, student):
    sql = '''INSERT INTO student (fullname,mark,hobby,b_date,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)


def delete_students(connection, id):
    try:
        sql = '''DELETE FROM student WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except Error as e:
        print(e)


def update_student(conn):
    sql = '''UPDATE student SET fullname == "busy" WHERE is_married > 0'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname NOT NULL DEFAULT 0.0,
mark FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL ,
is_married BOOLEAN DEFAULT FALSE
);
'''

if connection is not None:
    create_table(connection, sql_create_table)
    create_student(connection, ('Бека', 10.2, 'пишу', '2003-06-06', False))
    delete_students(connection, 1)
    read(connection)
    print('все работает')