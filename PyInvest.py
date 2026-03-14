import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

capital= float(input("Capital: "))
aporte= float(input("Aporte Mensal: "))
meses= float(input('Prazo (meses):'))
cdiAnual = float(input("Cdi Anual (%) "))/100
perc_cdb = float (input('Percentual do CDI (%)'))/100
perc_lci = float(input("Percentual LCI (%)"))/100
taxa_fii = float(input("Rentabilidade Mensal FII"))/100
meta = float(input('Meta financeira (R$)'))


#Conversão CDI
cdi_mensal = math.pow((1 + cdiAnual), 1/12 ) -1

#Total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital*math.pow((1 + taxa_cdb), meses) + (aporte*meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb*0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital*math.pow((1 + taxa_lci), meses )+ (aporte*meses))

#POUPANCA
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca), meses) + (aporte * meses))

#FII - SIMULAÇÕES 

montante_base_fii = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))

variacao1 = montante_base_fii * (1 + random.uniform(-0.03, 0.03))
variacao2 = montante_base_fii * (1 + random.uniform(-0.03, 0.03))
variacao3 = montante_base_fii * (1 + random.uniform(-0.03, 0.03))
variacao4 = montante_base_fii * (1 + random.uniform(-0.03, 0.03))
variacao5 = montante_base_fii * (1 + random.uniform(-0.03, 0.03))

media_fii = statistics.mean([variacao1, variacao2, variacao3, variacao4, variacao5])
mediana_fii = statistics.median([variacao1, variacao2, variacao3, variacao4, variacao5])
desvio_padrao_fii = statistics.stdev([variacao1, variacao2, variacao3, variacao4, variacao5])

# DATA DA SIMULAÇÃO E RESGATE
data_atual = datetime.datetime.now()
data_final = data_atual + datetime.timedelta(days=meses * 30)

# META FINANCEIRA
meta_atingida = media_fii >= meta

# FORMATAÇÃO MONETÁRIA
capital_formatado = locale.currency(capital, grouping=True)
aporte_formatado = locale.currency(aporte, grouping=True)
total_investido_formatado = locale.currency(total_investido, grouping=True)
montante_cdb_liquido_formatado = locale.currency(montante_cdb_liquido, grouping=True)
montante_lci_formatado = locale.currency(montante_lci, grouping=True)
montante_poupanca_formatado = locale.currency(montante_poupanca, grouping=True)
media_fii_formatado = locale.currency(media_fii, grouping=True)
mediana_fii_formatado = locale.currency(mediana_fii, grouping=True)
desvio_padrao_fii_formatado = locale.currency(desvio_padrao_fii, grouping=True)

# GRÁFICOS ASCII
grafico_cdb = '█' * int(montante_cdb_liquido / 1000)
grafico_lci = '█' * int(montante_lci / 1000)
grafico_poupanca = '█' * int(montante_poupanca / 1000)
grafico_fii = '█' * int(media_fii / 1000)

# RELATÓRIO FINAL
print(f"""
======================================
{'PyInvest - Simulador de Investimentos':^38}
======================================
Data da simulação: {datetime.datetime.strftime(data_atual, '%d/%m/%Y')}
Data estimada de resgate: {datetime.datetime.strftime(data_final, '%d/%m/%Y')}
======================================

Total investido: {total_investido_formatado}

--- RESULTADOS FINANCEIROS ---
CDB: {montante_cdb_liquido_formatado}
{grafico_cdb}

LCI/LCA: {montante_lci_formatado}
{grafico_lci}

Poupança: {montante_poupanca_formatado}
{grafico_poupanca}

FII (média): {media_fii_formatado}
{grafico_fii}

--- ESTATÍSTICAS FII ---
Mediana: {mediana_fii_formatado}
Desvio padrão: {desvio_padrao_fii_formatado}

Meta atingida? {meta_atingida}
======================================
""")


