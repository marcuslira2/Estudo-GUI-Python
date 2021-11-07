import tkinter
from tkinter import ttk

janela = tkinter.Tk()
# Titulo da aplicação
janela.title("Aplicação GUI")
# Tornando a aplicação fixa ( não podendo mexer na altura e largura da tela)
janela.resizable(False, False)

# Uso do Label

ttk.Label(janela, text="Componente Label").grid(column=0, row=0)

# Loop principal da aplicação
janela.mainloop()
