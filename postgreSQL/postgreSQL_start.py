import psycopg2

try:

    conn = psycopg2.connect(database="postgres", user="postgres", password="8710", host="127.0.0.1", port="5432")
    print("Conexão com banco de dados feita com sucesso!")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Agenda
    (Id  INT PRIMARY KEY NOT NULL,
    Nome TEXT NOT NULL,
    Telefone CHAR(12));""")
    print('Tabela Agenda criada com sucesso!')
    conn.commit()
    conn.close()

except ConnectionError as erro:
    print("Erro de conexão ", erro)


