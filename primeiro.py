import json
import dados
import tkinter as tk

def primeiros(x):
    with open("dados/primeiro.json", "r", encoding="utf-8") as data: J1 = json.load(data)


    

    janela = tk.Toplevel(x)

    janela.title("vendas e comissoes")
    janela.geometry("600x500")

    frametext = tk.Frame(janela,width=770, height=300)
    frametext.pack()
    frametext.pack_propagate(False)
    scroll = tk.Scrollbar(frametext)
    scroll.pack(side="left", fill="both")
    scrollhorizontal = tk.Scrollbar(frametext, orient="horizontal")
    scrollhorizontal.pack(side="bottom", fill="x")
    liste = tk.Listbox(frametext, yscrollcommand=scroll.set, xscrollcommand=scrollhorizontal.set)
    liste.pack(side="left", fill="both", expand=True)
    scroll.config(command=liste.yview)
    scrollhorizontal.config(command=liste.xview)

    frametextt = tk.Frame(janela,width=770, height=150)
    frametextt.pack()
    frametextt.pack_propagate(False)
    scrolll = tk.Scrollbar(frametextt)
    scrolll.pack(side="left", fill="both")
    scrollhorizontall = tk.Scrollbar(frametextt, orient="horizontal")
    scrollhorizontall.pack(side="bottom", fill="x")
    listee = tk.Listbox(frametextt, yscrollcommand=scrolll.set, xscrollcommand=scrollhorizontall.set)
    listee.pack(side="left", fill="both", expand=True)
    scrolll.config(command=listee.yview)
    scrollhorizontall.config(command=listee.xview)

    quadroentrada = tk.Frame(janela)
    quadroentrada.pack()

    tk.Label(quadroentrada, text="Vendedor:").grid(row=0, column=0)
    campo_vendedor = tk.Entry(quadroentrada)
    campo_vendedor.grid(row=0, column=1)

    tk.Label(quadroentrada, text="Valor:").grid(row=0, column=2)
    campo_valor = tk.Entry(quadroentrada)
    campo_valor.grid(row=0, column=3)


    def adicionar():
        vendedor = campo_vendedor.get()
        valor = float(campo_valor.get())

        novo = {
            "vendedor": vendedor,
            "valor": valor
        }

        J1["vendas"].append(novo)

        with open("dados/primeiro.json", "w", encoding="utf-8") as data:
            json.dump(J1, data, ensure_ascii=False, indent=4)
        campo_vendedor.delete(0, tk.END)
        campo_valor.delete(0, tk.END)


    botaoadicionar = tk.Button(
        quadroentrada,
        text="Adicionar venda",
        command=adicionar
    )
    botaoadicionar.grid(row=1, column=2)




    comi = {}
    for venda in J1["vendas"]:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        if vendedor not in comi:
            comi[vendedor] = {}
            comi[vendedor]["totalvendas"] = 0
            comi[vendedor]["totalcomi"] = 0
    

        print(vendedor, valor)
        if valor < 100:
            linhas = f'{vendedor} recebeu comissão de {valorcomi} na venda no valor de {valor})'
            liste.insert(tk.END, linhas)
            valorcomi = 0
        elif valor < 500:
            valorcomi = round(valor * 0.01,2)
            valorT = round(valor + valorcomi,2)
            linhas = f'{vendedor} recebeu comissão de {valorcomi} na venda no valor de {valor})'
            liste.insert(tk.END, linhas)
        elif valor >= 500:
            valorcomi = round(valor * 0.05, 2)
            valorT = round(valor + valorcomi,2)
            linhas = f'{vendedor} recebeu comissão de {valorcomi} na venda no valor de {valor})'
            liste.insert(tk.END, linhas)

        comi[vendedor]["totalvendas"] += valor
        comi[vendedor]["totalcomi"] += valorcomi



    for vendedor, dados in comi.items():
        comi[vendedor]["totalvendas"] = round(comi[vendedor]["totalvendas"], 2)
        comi[vendedor]["totalcomi"] = round(comi[vendedor]["totalcomi"], 2)
        linhas = f'{vendedor} arrecadou um total de {dados["totalcomi"]} em comissões e faturou {dados["totalvendas"]} em vendas'
        listee.insert(tk.END, linhas)

    

    janela.mainloop()


