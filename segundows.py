import tkinter as tk
import json
import datetime as dt
def segundo(s):

    with open("dados/estoque.json", "r", encoding="utf-8") as data: J2 = json.load(data)
    with open("dados/historico.json", "r", encoding="utf-8") as data: J0 = json.load(data)
    janela = tk.Toplevel(s)

    janela.title("Controle de Estoque")
    janela.geometry("600x500")



    quadroprodutos = tk.Frame(janela, width=500, height=300)
    quadroprodutos.pack()
    barra = tk.Scrollbar(quadroprodutos)
    barra.pack(side="right", fill="y")
    quadroprodutos.pack_propagate(False)
    lista = tk.Listbox(quadroprodutos, yscrollcommand= barra.set)
    lista.pack(side= "left", fill="both", expand=True)


    global linha


    quadroentrada = tk.Frame(janela)
    quadroentrada.pack()

    global campo_codigo
    global campo_movimentacao

    tk.Label(quadroentrada, text="Código:").grid(row=0, column=0)
    campo_codigo = tk.Entry(quadroentrada)
    campo_codigo.grid(row=0, column=1)

    tk.Label(quadroentrada, text="Movimentação:").grid(row=1, column=0)
    campo_movimentacao = tk.Entry(quadroentrada)
    campo_movimentacao.grid(row=1, column=1)






    global liste
    liste = None
    def prints():
        linha = f' CODIGO    |    ITEM    |    QTD '
        lista.insert(tk.END, linha)
        for item in J2["estoque"]:
            linha = f'{item["codigoProduto"]} | {item["descricaoProduto"]} | {item["estoque"]}'
            lista.insert(tk.END, linha)
        atulizarhist()

    def submit():
        global codigo
        global movimentacao
        codigo = int(campo_codigo.get())
        movimentacao = int(campo_movimentacao.get())

        for i in J2["estoque"]:
            if codigo == i["codigoProduto"]:
                antes = i["estoque"]
                i["estoque"] += movimentacao
                depois = i["estoque"]
                dataa = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(dataa)
                J0["historico"].append({

                    "codigo": codigo,
                    "descricao": i["descricaoProduto"],
                    "valorAntigo": antes,
                    "valorNovo": depois,
                    "data" : dataa
                })

        lista.delete(0, tk.END)
        prints()

        campo_codigo.delete(0, tk.END)
        campo_movimentacao.delete(0, tk.END)




        

    def save():
        with open("dados/estoque.json", "w", encoding="utf-8") as data:
            json.dump(J2, data, ensure_ascii=False, indent=4)
        with open("dados/historico.json", "w", encoding="utf-8") as data:
            json.dump(J0, data, ensure_ascii=False, indent=4)


    def hist():

        telahisto = tk.Toplevel(janela)
        telahisto.title("historico")
        telahisto.geometry("800x500")
        frametext = tk.Frame(telahisto,width=770, height=470)
        frametext.pack()
        frametext.pack_propagate(False)
        scroll = tk.Scrollbar(frametext)
        scroll.pack(side="left", fill="both")
        scrollhorizontal = tk.Scrollbar(frametext, orient="horizontal")
        scrollhorizontal.pack(side="bottom", fill="x")
        liste = tk.Listbox(frametext, yscrollcommand=scroll.set, xscrollcommand=scrollhorizontal.set)
        liste.pack(side="left", fill="both", expand=True)
        for item in J0["historico"]:
            print(item)
            linhas = f'Movimentação registrada — Produto:{item["descricao"]} (Código:{item["codigo"]}). estoque anterior:{item["valorAntigo"]}. Estoque atual:{item["valorNovo"]}. Data da movimentação:{item["data"]}'
            liste.insert(tk.END, linhas)
        scroll.config(command=liste.yview)
        scrollhorizontal.config(command=liste.xview)
    def atulizarhist():
        if liste is None:
            return

        liste.delete(0, tk.END)
        for item in J0["historico"]:    
            linhas = f'Movimentação registrada — Produto:{item["descricao"]} (Código:{item["codigo"]}). estoque anterior:{item["valorAntigo"]}. Estoque atual:{item["valorNovo"]}. Data da movimentação:{item["data"]}'
            liste.insert(tk.END, linhas)

        
        

    botaohisto = tk.Button(janela, text="histórico", command=hist)
    botaohisto.place(relx=1.0, x=-17, y=490, anchor="se")

    botaosave = tk.Button(janela, text="Save", command=save)
    botaosave.place(relx=0, x=10, y=490, anchor="sw")

    botao = tk.Button(quadroentrada, text="Submit", command=submit)
    botao.grid(row=2, column=1)

    prints()
    janela.mainloop()