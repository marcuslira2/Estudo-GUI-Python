import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Combobox')
janela.geometry('800x640')

ttk.Label(janela, text="Combobox Widget", background='green', foreground='white',
          font=("Times New Roman", 15)).grid(row=0, column=1)

ttk.Label(janela, text="Selecione um mes: ",
          font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25)

n = tk.StringVar()
escolha = ttk.Combobox(janela, width=27, textvariable=n)

escolha['values'] = ('Janeiro',
                     'Fevereiro',
                     'Março',
                     'Abril')
escolha.grid(column=1, row=5)
escolha.current()
janela.mainloop()
