import psycopg2

try:

    conn = psycopg2.connect(database="postgres", user="postgres", password="8710", host="127.0.0.1", port="5432")
    print("Conexão com banco de dados feita com sucesso!")
    cur = conn.cursor()
    cur.execute("""select * from public."agenda" where "id" = 1""")
    registro = cur.fetchone()
    print(registro)
    conn.commit()
    print("Seleção realizada com sucesso")
    conn.close()

except ConnectionError as erro:
    print("Erro de conexão ", erro)
