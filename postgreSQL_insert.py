import psycopg2

try:

    conn = psycopg2.connect(database="postgres", user="postgres", password="8710", host="127.0.0.1", port="5432")
    print("Conexão com banco de dados feita com sucesso!")
    cur = conn.cursor()
    cur.execute("""INSERT INTO public."agenda"("id","nome","telefone") 
                    VALUES (1,'Pessoa','012234567891')""")
    conn.commit()
    print("Inserção reaizada com sucesso!")
    conn.close()

except ConnectionError as erro:
    print("Erro de conexão ", erro)