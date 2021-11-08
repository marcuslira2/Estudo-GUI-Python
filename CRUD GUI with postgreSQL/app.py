import tkinter as tk
from tkinter import ttk
import crud as crud


class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBd()
        ## Componentes
        self.lbCodigo = tk.Label(win, text='Código do produto: ')
        self.lbNome = tk.Label(win, text="Nome do produto: ")
        self.lbPreco = tk.Label(win, text="Preço ")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(win, text="Cadastrar", command=self.cadastrarProduto)
        self.btnAtualizar = tk.Button(win, text="Atualizar", command=self.atualizarProduto)
        self.btnExcluir = tk.Button(win, text="Excluir", command=self.excluirProduto)
        self.btnLimpar = tk.Button(win, text="Limpar tela", command=self.limparTela)

        ## Componentes do TreeView
        self.dadosColunas = ("Código", "Nome", "Preço")

        self.treeProdutos = ttk.Treeview(win,
                                         columns=self.dadosColunas,
                                         selectmode='browse')

        self.scrollbar = ttk.Scrollbar(win,
                                       orient="vertical",
                                       command=self.treeProdutos.yview)
        self.scrollbar.pack(side='right', fill='x')

        self.treeProdutos.configure(yscrollcommand=self.scrollbar.set)

        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")

        self.treeProdutos.column("Código", minwidth=0, width=100)
        self.treeProdutos.column("Nome", minwidth=0, width=100)
        self.treeProdutos.column("Preço", minwidth=0, width=100)

        self.treeProdutos.pack(padx=10, pady=10)
        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        ## Posicionar os componentes na tela

        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lbNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lbPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)
        self.scrollbar.place(x=805, y=300, height=225)
        self.carregarDadosIniciais()

    # Apresentar registros selecionados

    def apresentarRegistrosSelecionados(self, event):
        self.limparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo, nome, preco = item["values"][0:3]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

    # Carregar dados iniciais

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.jd = 0
            registros = self.objBD.selecionarDados()
            print("dados disponiveis no BD")
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print("Código = ", codigo)
                print("Nome = ", nome)
                print("Preço = ", preco, "\n")

                self.treeProdutos.insert('', 'end',
                                         jd=self.jd,
                                         values=(codigo,
                                                 nome,
                                                 preco))
                self.jd = self.jd + 1
                self.id = self.id + 1
                print("dados da base")
        except:
            print("Ainda não existe dados para carregar!")

    # Ler dados da tela
    def lerCampos(self):
        try:
            print("Dados disponiveis")
            codigo = int(self.txtCodigo.get())
            print('Codigo', codigo)
            nome = self.txtNome.get()
            print('Nome', nome)
            preco = float(self.txtPreco.get())
            print('Preço', preco)
            print("Leitura dos dados com sucesso")
        except:
            print("Não foi possivel ler os dados")
        return codigo, nome, preco

    # Cadastrar Produtos
    def cadastrarProduto(self):
        try:
            print("Dados disponiveis")
            codigo, nome, preco = self.lerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert('', 'end',
                                     jd=self.jd,
                                     values=(codigo,
                                             nome,
                                             preco))
            self.jd = self.jd + 1
            self.id = self.id + 1
            self.limparTela()
            print("Produto cadastrado com sucesso!")
        except:
            print("Não foi possivel fazer o cadastro")

    # Atualizar produto
    def atualizarProduto(self):
        try:
            print("Dados disponiveis")
            codigo, nome, preco = self.lerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.limparTela()
            print("Produto atualizado com sucesso")
        except:
            print("Não foi possivel fazer a atualização")

    # Deletar produto

    def excluirProduto(self):
        try:
            print("Dados disponiveis")
            codigo, nome, preco = self.lerCampos()
            self.objBD.excluirDados(codigo)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.limparTela()
            print("Produto excluido com sucesso")
        except:
            print("Não foi possivel excluir o produto")

    def limparTela(self):
        try:
            print("Dados disponiveis")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("Campos limpos")
        except:
            print("Nao foi possivel limpar os campos")


janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem vindo a aplicação de banco de dados ( que deus ponha mão nesse codigo )")
janela.geometry("820x660+10+10")
janela.mainloop()
