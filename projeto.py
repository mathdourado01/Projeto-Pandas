#Percorrer os arquivos de Vendas
import os
import pandas as pd

lista_arquivos = os.listdir("C:\\Users\\mathd\\OneDrive\\Área de Trabalho\\VSCODE TRABALHOS\\Projeto Pandas Aplicações\\Vendas-20240605T164912Z-001\\Vendas")
tabela_total = pd.DataFrame()

#Importar a base de arquivos em vendas
for arquivo in lista_arquivos:
        if "Vendas" in arquivo: 
                print(f"Vendas - {arquivo}")
                tabela = pd.read_csv("C:\\Users\\mathd\\OneDrive\\Área de Trabalho\\VSCODE TRABALHOS\\Projeto Pandas Aplicações\\Vendas-20240605T164912Z-001\\Vendas")
                tabela_total = tabela_total.append(tabela)
                print(tabela)
#Calcular o produto mais vendido 
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendidas", ascending=False)
print(tabela_produtos)
#Calcular o produto que mais faturou(em faturamento)
tabela_total["Faturamento"] =tabela_total['Quantidade Vendida'] * tabela_total["Preco Unitario"] 
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento2 = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento2)
#Calcular a loja que mais vendeu(em faturamento)
tabela_lojas = tabela_total.groupby('Lojas').sum()
tabela_lojas = tabela_lojas["Faturamento"]
print(tabela_lojas)