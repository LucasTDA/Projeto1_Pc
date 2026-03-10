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