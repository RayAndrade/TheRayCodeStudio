import sqlite3

DATABASE = "../database/theraycode.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection