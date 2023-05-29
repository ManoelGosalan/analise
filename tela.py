import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Create a Tkinter window
window = tk.Tk()
window.title("Results")
window.geometry("400x200")

# Carregar o arquivo xls
caminho_arquivo = 'Planilha_Contador.xls'  # Substitua pelo caminho real do seu arquivo XLS

# Carregar o arquivo xls
df_xls = pd.read_excel(caminho_arquivo)

nome_coluna = 'VALOR'  # Nome da coluna que deseja verificar

# Verificar se a coluna existe
columns = df_xls.columns

# Limpar os valores na coluna 'VALOR' removendo pontos e convertendo para numérico
df_xls[nome_coluna] = df_xls[nome_coluna].str.replace('.', '').str.replace(',', '.').astype(float)

# Calcular as somas por número de série
soma_serie_1 = df_xls.loc[df_xls['SÉRIE'] == 1, nome_coluna].sum()
soma_serie_3 = df_xls.loc[df_xls['SÉRIE'] == 3, nome_coluna].sum()
soma_serie_4 = df_xls.loc[df_xls['SÉRIE'] == 4, nome_coluna].sum()

# Filtrar as NFC-e com séries
quantidade_serie_1 = len(df_xls[df_xls['SÉRIE'] == 1])
quantidade_serie_3 = len(df_xls[df_xls['SÉRIE'] == 3])
quantidade_serie_4 = len(df_xls[df_xls['SÉRIE'] == 4])

# Create labels to display the results
label_1 = tk.Label(window, text=f"NFC-e com série 1 total de: {quantidade_serie_1}")
label_2 = tk.Label(window, text=f"NFC-e com série 3 total de: {quantidade_serie_3}")
label_3 = tk.Label(window, text=f"NFC-e com série 4 total de: {quantidade_serie_4}")
label_4 = tk.Label(window, text=f"A soma da coluna {nome_coluna} para série 1 é de: R$ {soma_serie_1:,.2f}")
label_5 = tk.Label(window, text=f"A soma da coluna {nome_coluna} para série 3 é de: R$ {soma_serie_3:,.2f}")
label_6 = tk.Label(window, text=f"A soma da coluna {nome_coluna} para série 4 é de: R$ {soma_serie_4:,.2f}")

# Pack the labels into the window
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()
label_6.pack()

# Carregar o arquivo CSV
caminho_arquivo = 'Planilha_Contador.csv'  # Substitua pelo caminho real do seu arquivo CSV
nome_coluna1 = 'VALOR'  # Substitua pelo nome da coluna que deseja somar

# Carregar o arquivo CSV e selecionar a coluna desejada
df = pd.read_csv(caminho_arquivo, delimiter=';')

# Limpar os valores na coluna 'VALOR' removendo pontos e convertendo para numérico
df[nome_coluna1] = df[nome_coluna1].str.replace('.', '').str.replace(',', '.').astype(float)

# Calcular a soma da coluna
soma = df[nome_coluna1].sum()

# Create a label to display the result
label_7 = tk.Label(window, text='O Valor total das Notas no arquivo é de: R$ {:,.2f}'.format(soma))
label_7.pack()

# Show the Tkinter window
window.mainloop()
