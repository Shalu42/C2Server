import sqlite3

def init_db():
    conn = sqlite3.connect('c2server.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY,
            command TEXT NOT NULL,
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_command(command):
    conn = sqlite3.connect('c2server.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO agents (command) VALUES (?)', (command,))
    conn.commit()
    conn.close()
