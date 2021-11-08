import psycopg2


class AppBd:

    def __init__(self):
        print("Metodo construtor")

    # ------------------------------------------------------------------------------------
    #       Iniciar conexão com o banco de dados
    # ------------------------------------------------------------------------------------

    def abrirconexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="8710",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="postgres")
            print("Conexão com banco de dados feita com sucesso!")
        except (Exception, psycopg2.Error) as err:
            if (self.connection):
                print(f'Falha ao conectar com o banco de dados, erro: {err} ')

        # ------------------------------------------------------------------------------------
        #       Selecionar Dados
        # ------------------------------------------------------------------------------------

    def selecionarDados(self):
        try:
            self.abrirconexao()
            cur = self.connection.cursor()
            print("selecionando todos os produtos")

            selecionar = """select * from public."produto" """
            cur.execute(selecionar)
            registros = cur.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as err:
            print(f"Erro na operação de selecionar, erro {err}")
        finally:
            if (self.connection):
                cur.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")
        return registros

        # ------------------------------------------------------------------------------------
        #       Inserir Dados
        # ------------------------------------------------------------------------------------

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirconexao()
            cur = self.connection.cursor()
            inserir = """INSERT INTO public."produto" 
                    ("codigo","nome","preco") VALUES (%s,%s,%s)"""
            registro = (codigo, nome, preco)
            cur.execute(inserir, registro)
            self.connection.commit()
            count = cur.rowcount
            print(count, "Registro inserido com sucesso na tabela Produto")
        except(Exception, psycopg2.Error) as err:
            print(f"Falha ao inserir registro na tabela, erro: {err}")

        finally:
            if (self.connection):
                cur.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")

        # ------------------------------------------------------------------------------------
        #       Alterar Dados
        # ------------------------------------------------------------------------------------

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirconexao()
            cur = self.connection.cursor()
            print("Registro antes da atualização")
            selecionar = """select * from public."produto" where "codigo" = %s """
            cur.execute(selecionar, (codigo,))
            registrar = cur.fetchone()
            print(registrar)
            atualizar = """Update public."produto" set "nome" = %s, "preco" = %s
                                    where "codigo" = %s"""
            cur.execute(atualizar, (nome, preco, codigo))
            self.connection.commit()
            count = cur.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro após atualização")
            selecionar = """select * from public."produto" where "codigo" =%s"""
            cur.execute(selecionar, (codigo,))
            registrar = cur.fetchone()
            print(registrar)
        except(Exception, psycopg2.Error) as err:
            print("Erro na atualização", err)

        finally:
            if (self.connection):
                cur.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")

        # ------------------------------------------------------------------------------------
        #       Deletar Dados
        # ------------------------------------------------------------------------------------

    def deletarDados(self, codigo):
        try:
            self.abrirconexao()
            cur = self.connection.cursor()
            deletar = """delete from public."produto" where "codigo" = %s"""
            cur.execute(deletar, (codigo,))
            self.connection.commit()
            count = cur.rowcount
            print(count, "Registro excluido com sucesso!")
        except(Exception, psycopg2.Error) as err:
            print(f"Erro na exclusão: erro {err}")

        finally:
            if (self.connection):
                cur.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")
