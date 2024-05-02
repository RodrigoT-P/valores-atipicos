# importamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creamos un dataframe por cada hoja del archivo excel
df2020 = pd.read_excel('gastos_costos_20_23.xlsx', sheet_name='2020')
df2021 = pd.read_excel('gastos_costos_20_23.xlsx', sheet_name='2021')
df2022 = pd.read_excel('gastos_costos_20_23.xlsx', sheet_name='2022')
df2023 = pd.read_excel('gastos_costos_20_23.xlsx', sheet_name='2023')

#TRATAMIENTO DE DATOS NULOS

print(df2020.info())

print(df2020.head(10))

#funcion que calclula el porcentaje de datos nulos por columna, y borrará las que tengan un porcentaje superior al 70%
def porcentaje_nulos(df):
    for i in df:
        if df[i].isnull().sum()/df.shape[0] > 0.7:
            df.drop(i, axis=1, inplace=True)
    return df

new2020 = porcentaje_nulos(df2020)
new2020.info()

print(new2020.isnull().sum())

#función que por cada columna numérica de datos nulos, los rellena con la mediana de la columna
def rellenar_nulos(df):
    for i in df:
        if df[i].dtype == 'int64' or df[i].dtype == 'float64':
            df[i].fillna(df[i].median(), inplace=True)
    
    df.dropna(inplace = True)
    return df

new2020 = rellenar_nulos(new2020)
new2020.isnull().sum()

#Hacemos una funcion que itere las funciones rellena_nulos, y porcentaje_nulos, por cada df en una lista dada
def nulos(df):
    g = porcentaje_nulos(df)
    h = rellenar_nulos(g)
    return h

new2020 = nulos(df2020)
new2021 = nulos(df2021)
new2022 = nulos(df2022)
new2023 = nulos(df2023)

#Creamos una funcion que cree un boxplot por cada año, de una columna dada en un solo grafico
def boxplots(df,df2,df3,df4, columna):
    #normalizamos los datos de la columna

    fig, ax = plt.subplots()
    ax.boxplot([df[columna],df2[columna],df3[columna],df4[columna]])
    ax.set_xticklabels(['2020', '2021', '2022', '2023'])
    ax.set_title(columna)
    ax.set_ylabel('Valor')
    plt.show()
    
boxplots(new2020, new2021, new2022, new2023, 'IVA')

boxplots(new2020, new2021, new2022, new2023, 'TOTAL SAT')

boxplots(new2020, new2021, new2022, new2023, 'TOTAL MX')

def histogramas(df,df2,df3,df4, columna):
    fig, ax = plt.subplots()
    ax.hist(df[columna], bins=10, alpha=0.5, label='2020')
    ax.hist(df2[columna], bins=10, alpha=0.5, label='2021')
    ax.hist(df3[columna], bins=10, alpha=0.5, label='2022')
    ax.hist(df4[columna], bins=10, alpha=0.5, label='2023')
    ax.set_title(columna)
    ax.set_ylabel('Frecuencia')
    ax.set_xlabel('Valor')
    ax.legend()
    plt.show()

histogramas(new2020, new2021, new2022, new2023, 'IVA')

histogramas(new2020, new2021, new2022, new2023, 'TOTAL SAT')

histogramas(new2020, new2021, new2022, new2023, 'TOTAL MX')

def quitar_atipicos(df, columna, df_name):
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    df = df[(df[columna] >= q1 - 1.5*iqr) & (df[columna] <= q3 + 1.5*iqr)]
    print('DataFrame name: ', df_name, 'Columna: ', columna)
    print('limite superior: ',  q3 + 1.5*iqr)
    print('limite inferior: ',  q1 - 1.5*iqr)
    return df

#generamos una funcion que regresa un nuevo dataframe sin valores atipicos de una columna dada con 2 veces la desviacion estandar
def quitar_atipicosstd(df, columna, df_name):
    std = df[columna].std()
    mean = df[columna].mean()
    df = df[(df[columna] >= mean - 2*std) & (df[columna] <= mean + 2*std)]
    print('DataFrame name: ', df_name, 'Columna: ', columna)
    print('limite superior: ',  mean + 2*std)
    print('limite inferior: ',  mean - 2*std)
    return df


new2020 = quitar_atipicos(new2020, 'IVA', '2020')
new2021 = quitar_atipicos(new2021, 'IVA', '2021')
new2022 = quitar_atipicos(new2022, 'IVA',  '2022')
new2023 = quitar_atipicos(new2023, 'IVA', '2023')

new2020 = quitar_atipicos(new2020, 'TOTAL SAT', '2020')
new2021 = quitar_atipicos(new2021, 'TOTAL SAT', '2021')
new2022 = quitar_atipicos(new2022, 'TOTAL SAT', '2022')
new2023 = quitar_atipicos(new2023, 'TOTAL SAT', '2023')

new2020 = quitar_atipicosstd(new2020, 'TOTAL MX', '2020')
new2021 = quitar_atipicosstd(new2021, 'TOTAL MX', '2021')
new2022 = quitar_atipicosstd(new2022, 'TOTAL MX', '2022')
new2023 = quitar_atipicosstd(new2023, 'TOTAL MX', '2023')

boxplots(new2020, new2021, new2022, new2023, 'IVA')

boxplots(new2020, new2021, new2022, new2023, 'TOTAL SAT')

#Creamos una funcion que exporta todos estos dataframes a un archivo csv
def exportar_csv(df, df2, df3, df4):
    df.to_csv('2020_sinatipicos.csv')
    df2.to_csv('2021_sinatipicos.csv')
    df3.to_csv('2022_sinatipicos.csv')
    df4.to_csv('2023_sinatipicos.csv')

exportar_csv(new2020, new2021, new2022, new2023)
