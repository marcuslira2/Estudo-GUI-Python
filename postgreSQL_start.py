import psycopg2

psycopg2.connect(database="Bancoteste",user="",senha="",host="127.0.0.1",porta="5432")

nomeDaTabela = 'tabelaExemplo'
cursor.execute(f"insert into {tabelaExemplo} values {[10,20]}")

