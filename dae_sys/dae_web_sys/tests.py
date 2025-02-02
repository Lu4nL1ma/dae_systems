# # from django.test import TestCase
# import sqlite3
# import pandas as pd

# #ler dados
# dados = pd.read_excel('custos.xlsx')

# df = pd.DataFrame(dados)

# conn = sqlite3.connect('C:\\Users\\corpl\\OneDrive\\DA3_SYSTEMS\\dae_sys\\db.sqlite3')

# cursor = conn.cursor()

# # Inserindo os dados do DataFrame na tabela 'pessoas' (assumindo que ela já existe)
# df.to_sql('dae_web_sys_custos', conn, if_exists='append', index=False)

# # # # Listando todas as tabelas
# # # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# # # tables = cursor.fetchall()
# # # for table in tables:
# # #     print(table[0])

# # # Visualizando os dados de uma tabela específica
# # cursor.execute("SELECT * FROM dae_web_sys_regiao_municipio")
# # results = cursor.fetchall()
# # for row in results:
# #     print(row)

# # Comando para apagar a tabela "minha_tabela"
# # cursor.execute("DROP TABLE IF EXISTS dae_web_sys_regiao_municipio")

# # # Criando a tabela com uma coluna ID autoincrementada
# # cursor.execute("""
# #     CREATE TABLE dae_web_sys_regiao_municipio (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         municipio TEXT,       
# #         regiao TEXT
# #     )
# # """)

# # Fechando a conexão
# conn.close()

# var = (56.88 + 292.90) / (1-0.1-0.2-0.1704)

# print(var)