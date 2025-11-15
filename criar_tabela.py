import sqlite3

conn = sqlite3.connect("censoescolar.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS instituicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo INTEGER,
    nome TEXT,
    co_uf INTEGER,
    co_municipio INTEGER,
    qt_mat_bas INTEGER,
    qt_mat_prof INTEGER,
    qt_mat_eja INTEGER,
    qt_mat_esp INTEGER
)
""")

conn.commit()
conn.close()

print("Tabela criada com sucesso.")