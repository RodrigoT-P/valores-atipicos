import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print("hello outliers")
df = pd.read_csv("ventas_totales_sinnulos (1).csv", index_col=0)
#print(df.head())

valores_nulos=df.isnull().sum()
#print(valores_nulos)

"""fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()"""

"""fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
plt.show()"""

y=df["ventas_precios_corrientes"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)
     
#Obtenemos datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
data_clean_iqr
     

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()
     
#Realizamos diagrama de caja o bigote
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corrientes")
plt.show() #dibujamos el diagrama

fig = plt.figure(figsize =(5, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corriente')
plt.xlabel('ventas_precios_corriente')
plt.ylabel('Frecuencia')
plt.show()


fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corrientes")
plt.show()
     

data_clean_iqr["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes.csv')
#files.download('ventas_precios_corrientes.csv')


fig = plt.figure(figsize =(5, 3))
plt.hist(x=df["ventas_precios_constantes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_constantes')
plt.xlabel('ventas_precios_constantes')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_constantes"]) 
plt.title("Outliers de ventas_precios_constantes")
plt.show()


#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["ventas_precios_constantes"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)


#Obtenemos datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
data_clean_iqr


#Realizamos diagrama de caja o bigote
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["ventas_precios_constantes"]) 
plt.title("Outliers de ventas_precios_constantes")
plt.show() #dibujamos el diagrama


fig = plt.figure(figsize =(5, 3))
plt.hist(x=df["ventas_totales_canal_venta"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_totales_canal_venta')
plt.xlabel('ventas_totales_canal_venta')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_totales_canal_venta"]) 
plt.title("Outliers de ventas_totales_canal_venta")
plt.show()


fig = plt.figure(figsize =(5, 3))
plt.hist(x=df["salon_ventas"], color='blue', rwidth=0.50)
plt.title('Histograma de salon ventas')
plt.xlabel('Salon Ventas')
plt.ylabel('Frecuencia')
plt.show()


"""fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_constantes')
plt.xlabel('ventas_precios_constantes')
plt.ylabel('Frecuencia')
plt.show()"""

