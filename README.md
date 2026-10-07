# Sistema de Gerenciamento

Projeto desenvolvido em Python como parte de uma avaliação técnica para um processo seletivo.

O sistema possui uma interface gráfica desenvolvida com Tkinter e utiliza arquivos JSON para armazenamento dos dados.

## Funcionalidades

### Vendas e comissões

* Leitura de vendas armazenadas em JSON.
* Cálculo automático de comissão de acordo com o valor da venda.
* Visualização das vendas e das comissões acumuladas por vendedor.
* Cadastro de novas vendas pela interface.

### Controle de estoque

* Visualização dos produtos cadastrados.
* Registro de entradas e saídas de estoque.
* Atualização da quantidade disponível.
* Histórico das movimentações com data e horário.
* Armazenamento das alterações em JSON.

### Controle de dívidas

* Cadastro de dívidas com ID, valor e data de vencimento.
* Verificação de vencimentos.
* Cálculo de juros de 2,5% por dia de atraso.
* Visualização das dívidas e dos valores atualizados.

## Tecnologias utilizadas

* Python 3.11
* Tkinter
* JSON
* Datetime

## Estrutura do projeto

```text
├── dados/
│   ├── primeiro.json
│   ├── estoque.json
│   ├── historico.json
│   └── juros.json
├── lobby.py
├── primeiro.py
├── segundows.py
└── terceiros.py
```

## Como executar

É necessário ter o Python instalado.

Execute o arquivo principal:

```bash
python lobby.py
```

## Executável

O projeto também pode ser executado através do arquivo `.exe` gerado com PyInstaller.

Para gerar o executável:

```bash
python -m PyInstaller --onedir --windowed lobby.py
```

O executável será criado dentro da pasta `dist/lobby/`.

## Observações

Os dados utilizados pelo sistema são armazenados nos arquivos JSON presentes na pasta `dist/lobby/dados/`.

Este projeto foi desenvolvido com foco na implementação das funcionalidades solicitadas na avaliação técnica e na aplicação prática dos conceitos de Python, manipulação de arquivos JSON e desenvolvimento de interfaces gráficas com Tkinter.
