#1. Importar os dados
import pandas as pd

dados = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")

#2. Limpeza de dados
dados = dados[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

dados_portugal = dados[dados['Country Name'] == 'Portugal']
dados_brazil = dados[dados['Country Name'] == 'Brazil']

#3. Calculo  Variação Percentual para Portugal e Brasil
def calculo_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100

consumo_portugal_1990 = dados_portugal['1990 [YR1990]'].values[0]
consumo_portugal_2000 = dados_portugal['2000 [YR2000]'].values[0]

consumo_brazil_1990 = dados_brazil['1990 [YR1990]'].values[0]
consumo_brazil_2000 = dados_brazil['2000 [YR2000]'].values[0]

variacao_percentual_portugal = calculo_variacao_percentual(consumo_portugal_1990, consumo_portugal_2000)
print("A variação percentual do consumo de energia elétrica de Portugal nos últimos 10 anos é de:", str(round(variacao_percentual_portugal, 2)),"%.")

print("")
variacao_percentual_brazil = calculo_variacao_percentual(consumo_brazil_1990, consumo_brazil_2000)
print("A variação percentual do consumo de energia elétrica de Brasil nos últimos 10 anos é de:", str(round(variacao_percentual_brazil, 2)),"%.")