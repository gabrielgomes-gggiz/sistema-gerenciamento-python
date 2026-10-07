import datetime as dt
import tkinter as tk
import json

def terceiros(z):
    with open("dados/juros.json", "r", encoding="utf-8") as data: J3 = json.load(data)

    janela = tk.Toplevel(z)
    janela.title("controle de vendas")
    janela.geometry("600x500")

    fundo = tk.Frame(janela,width=500, height=400)
    fundo.pack()
    barra = tk.Scrollbar(fundo)
    barra.pack(side="right", fill="y")
    fundo.pack_propagate(False)
    lista = tk.Listbox(fundo, yscrollcommand= barra.set)
    lista.pack(side= "left", fill="both", expand=True)

    hoje = dt.date.today()
    print (hoje)
    for data in J3["dividas"]:

        vencimento = dt.datetime.strptime(data["vencimento"], "%Y-%m-%d").date()
        acumulo = (hoje - vencimento).days
        if hoje <= vencimento:
            textp = (f'(sem juros acumuldados. divida id {data["id"]} vence dia {data["vencimento"]}. {-acumulo} dias restantes)')
        else:

            juros = round(data["valor"]* (1 + 0.025 * acumulo), 2)
            textp = (f'(divida atrasada em {acumulo} dias. juros atual de ({data["valor"]} > {juros}))')
        lista.insert(tk.END, textp)

    quadroentrada = tk.Frame(janela)
    quadroentrada.pack()


    def adicionar():
        novo = {
            "id": int(campo_id.get()),
            "valor": float(campo_valor.get()),
            "vencimento": campo_vencimento.get()
        }

        J3["dividas"].append(novo)

        with open("dados/juros.json", "w", encoding="utf-8") as data:
            json.dump(J3, data, ensure_ascii=False, indent=4)

        campo_id.delete(0, tk.END)
        campo_valor.delete(0, tk.END)
        campo_vencimento.delete(0, tk.END)


    tk.Label(quadroentrada, text="ID:").grid(row=0, column=0)
    campo_id = tk.Entry(quadroentrada)
    campo_id.grid(row=0, column=1)

    tk.Label(quadroentrada, text="Valor:").grid(row=0, column=2)
    campo_valor = tk.Entry(quadroentrada)
    campo_valor.grid(row=0, column=3)

    tk.Label(quadroentrada, text="Vencimento:").grid(row=0, column=4)
    campo_vencimento = tk.Entry(quadroentrada)
    campo_vencimento.grid(row=0, column=5)

    botaoadicionar = tk.Button(
        quadroentrada,
        text="Adicionar dívida",
        command=adicionar
    )
    botaoadicionar.grid(row=1, column=3)
    janela.mainloop()