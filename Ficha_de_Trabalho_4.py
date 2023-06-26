#1. Importar os dados
import pandas as pd

dados = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")

#2. Limpeza de dados
dados = dados[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

dados_portugal = dados[dados['Country Name'] == 'Portugal']
dados_brazil = dados[dados['Country Name'] == 'Brazil']
