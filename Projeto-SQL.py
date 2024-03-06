import sqlite3

conn = sqlite3.connect('banco-dados.sdb')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL)''')

nome = input('Digite o nome do usuário: ')
email = input('Digite o email do usuário: ')
senha = input('Digite a senha do usuário: ')

cursor.execute('INSERT INTO user (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))

conn.commit()

conn.close()
