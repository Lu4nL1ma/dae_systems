# from django.test import TestCase
import sqlite3
import pandas as pd


conn = sqlite3.connect('C:\\Users\\corpl\\OneDrive\\DA3_SYSTEMS\\dae_sys\\db.sqlite3')

cursor = conn.cursor()


# #ler dados
dados = ['SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'METROPOLITANA', 'METROPOLITANA', 'METROPOLITANA', 'METROPOLITANA', 'METROPOLITANA', 'METROPOLITANA', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'METROPOLITANA', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'METROPOLITANA', 'NORDESTE', 'METROPOLITANA', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'SUDESTE', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'MARAJÓ', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'SUDESTE', 'NORDESTE', 'METROPOLITANA', 'NORDESTE', 'NORDESTE', 'SUDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'SUDESTE', 'SUDESTE', 'NORDESTE', 'SUDESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'METROPOLITANA', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'NORDESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE', 'BAIXO', 'AMAZONAS', 'BAIXO', 'AMAZONAS', 'SUDOESTE', 'SUDOESTE', 'SUDOESTE']

# df = pd.DataFrame(dados)

# print(df)

# # Inserindo os dados do DataFrame na tabela 'pessoas' (assumindo que ela já existe)
# df.to_sql('dae_web_sys_custos', conn, if_exists='append', index=False)

# Listando todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(table[0])

# cursor.execute('DELETE FROM dae_web_sys_regiao_municipio')

# conn.execute('''
#           CREATE TABLE IF NOT EXISTS minha_tabela (
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               meso TEXT,
#               regiao TEXT,
#               municipio TEXT
#           )
#           ''')

# for i in range(1, 145):
#     valor = dados[i]  # Exemplo de valor para a nova coluna
#     conn.execute(f"UPDATE dae_web_sys_regiao_municipio SET meso = '{valor}' WHERE id = {i}")

# # Visualizando os dados de uma tabela específica
# cursor.execute("SELECT * FROM dae_web_sys_regiao_municipio")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# # Comando para apagar a tabela "minha_tabela"
# cursor.execute("DROP TABLE IF EXISTS dae_web_sys_regiao_municipio")


# Fechando a conexão
conn.close()