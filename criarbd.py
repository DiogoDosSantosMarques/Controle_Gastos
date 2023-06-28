import sqlite3 as lite

con = lite.connect('dados.db')

# Criando tabela Categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT)")

# Criando tabela receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT,categoria TEXT, adicionado_em DATE, valor DECIMAL)")


with con:
    cur = con.cursor()    
    cur.execute("CREATE TABLE Gastos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")
   
