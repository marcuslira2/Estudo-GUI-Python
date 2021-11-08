import tkinter as tk


def mostrar_nomes():
    print(f'Nome: {e1.get()}\nSobrenome: {e2.get()}')


janela = tk.Tk()
janela.title("Aplicaç~~ao de GUI com o Widget Entry")
tk.Label(janela, text="Nome").grid(row=0)
tk.Label(janela, text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair',
          command=janela.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
