import psycopg2
from faker import Faker

try:

    conn = psycopg2.connect(database="postgres", user="postgres", password="8710", host="127.0.0.1", port="5432")
    print("Conexão com banco de dados feita com sucesso!")
    cur = conn.cursor()
    fake = Faker('pt_BR')
    cur.execute("""CREATE TABLE IF NOT EXISTS produto 
    (codigo  INT PRIMARY KEY NOT NULL,
    Nome TEXT NOT NULL,
    preco REAL);""")
    print('Tabela produto criada com sucesso!')

    n = 10
    for i in range(n):
        codigo = i + 10
        nome = 'produto_' + str(i + 1)
        preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
        print(preco)
        print(nome)

        insert_SQL = """INSERT INTO public."produto" ("codigo","nome","preco")
                        VALUES (%s,%s,%s)"""
        registro = (codigo, nome, preco)
        cur.execute(insert_SQL, registro)

    conn.commit()
    conn.close()

except ConnectionError as erro:
    print("Erro de conexão ", erro)
