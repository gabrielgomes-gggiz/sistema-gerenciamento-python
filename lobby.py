import tkinter as tk
import primeiro as p
import segundows as s
import terceiro as t

tela = tk.Tk()
def abrir_primeiro():
    p.primeiros(tela)


def abrir_segundo():
    s.segundo(tela)

def abrir_terceiro():
    t.terceiros(tela)


tela.geometry("500x500")
tela.title("OLA!")
botao1 = tk.Button(tela, text="vendas e comissoes", command=abrir_primeiro )
botao1.grid(row=5, column= 2)
botao2 = tk.Button(tela, text="controel de estoque", command=abrir_segundo )
botao2.grid(row=5, column= 4)
botao3 = tk.Button(tela, text="controle de vendas", command=abrir_terceiro)
botao3.grid(row=5,column=6)
tela.mainloop()