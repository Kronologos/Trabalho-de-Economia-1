import numpy as np
import pandas as pd 

colunas = [20     ,22     ,24     ,26     ,27     ,28       ,30    ]#columns
linhas = [70,72,74,76,78,80,81,82]#index
matriz = [
    [22.71  ,23.444 ,24.133 ,24.786 ,25.1   ,25.406   ,25.997],#70
    [23.033 ,23.776 ,24.476 ,25.138 ,25.456 ,25.766   ,26.366],#72
    [23.35  ,24.104 ,24.813 ,25.484 ,25.807 ,26.122   ,26.729],#74
    [23.664 ,24.428 ,25.146 ,25.826 ,26.153 ,26.472   ,27.088],#76
    [23.973,24.747  ,25.475 ,26.164 ,26.495 ,26.818   ,27.442],#78
    [24.278 ,25.062 ,25.8   ,26.497 ,26.833 ,27.16    ,27.792],#80
    [24.43  ,25.218 ,25.96  ,26.662 ,27     ,27.329   ,27.965],#81
    [24.58  ,25.374 ,26.12  ,26.827 ,27.166 ,27.497   ,28.137]]#82
data = np.array(matriz)
dados = pd.DataFrame(data=data,index=linhas,columns=colunas)
def f(k,l):
    return dados._get_value(index=l,col=k)
#print(dados)

#Cálulo dos custos:
c_22 = []
c_26 = []
for l in linhas:
    value = 2*22 + l  
    c_22.append(value)
c_22 = np.array(c_22)
for l in linhas:
    value = 2*26 + l 
    c_26.append(value)
c_26=np.array(c_26)
#Tabelas de custo:
tab_cust = pd.DataFrame(data=np.array([c_22,c_26]).T,index=linhas,columns=[22,26])
tab_cust.to_csv('cust.csv')
#Cálculo do Lucro:
l_22 = []
l_26 = []
for l in linhas:
    luc_22 = round(6*f(22,l)-(2*22+l),3)
    luc_26 = round(6*f(26,l)-(2*26+l),3)
    l_22.append(luc_22)
    l_26.append(luc_26)
#Tabelas de custo
tab_luc = pd.DataFrame(data=np.array([l_22,l_26]).T,index=linhas,columns=[22,26])
tab_luc.to_csv('luc.csv')
#Contas Pmgk e Pmgl:
#Pmgk
Pmgk = []
for k in range(len(colunas)):
    temp = []
    for l in range(len(linhas)):
        if(k+1<len(colunas)):
            value = (f(colunas[k+1] , linhas[l]) - f(colunas[k] , linhas[l]))/(colunas[k+1]-colunas[k])
            temp.append(round(value,3))
        else:
            temp.append('-')
    Pmgk.append(temp)
Pmgk = pd.DataFrame(data = np.array(Pmgk).T[0:-1,:],index=linhas[:-1],columns=colunas)
Pmgk.to_csv('Pmgk.csv')
#Pmgl
Pmgl = []
for k in range(len(colunas)):
    temp = []
    for l in range(len(linhas)):
        if(l+1<len(linhas)):
            value = (f(colunas[k] , linhas[l+1]) - f(colunas[k] , linhas[l]))/(linhas[l+1]-linhas[l])
            temp.append(round(value,3))
        else:
            temp.append('-')
    Pmgl.append(temp)
Pmgl = pd.DataFrame(data = np.array(Pmgl).T[0:-1,:],index=linhas[:-1],columns=colunas)
Pmgl.to_csv('Pmgl.csv')



