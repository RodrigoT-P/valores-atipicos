# importamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Abrimos el archivo
df = pd.read_csv('ventas_sinnulos.csv')

#checamos si en verdad hay datos nulos
print(df.isnull().sum())

df.head()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["alimentos_preparados_rotiseria"], color='blue', rwidth=0.50)
plt.title('Histograma de alimentos_preparados_rotiseria')
plt.xlabel('alimentos_preparados_rotiseria')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["alimentos_preparados_rotiseria"]) 
plt.title("Outliers de Preparados Rosticeria")
plt.show()

y=df["alimentos_preparados_rotiseria"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior_iqr)|(y<Limite_Inferior_iqr)]
outliers_iqr

#Obtenemos datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
data_clean_iqr

#Realizamos diagrama de caja o bigote
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["alimentos_preparados_rotiseria"]) 
plt.title("Outliers de alimentos_preparados_rotiseria")
plt.show() #dibujamos el diagrama

data_clean_iqr["alimentos_preparados_rotiseria"].to_csv('alimentos_preparados_rotiseria.csv')

#Valores atipicos de otros

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["otros"], color='blue', rwidth=0.50)
plt.title('Histograma de otros')
plt.xlabel('Otros')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["otros"]) 
plt.title("Outliers de otros")
plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["otros"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior_iqr)|(y<Limite_Inferior_iqr)]
outliers_iqr

#Obtenemos datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
data_clean_iqr

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["otros"]) 
plt.title("Outliers de otros")
plt.show()

data_clean_iqr["otros"].to_csv('otros.csv')

#LIMPIEZA PARA SALON DE VENTAS

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["salon_ventas"], color='blue', rwidth=0.50)
plt.title('Histograma de salon_ventas')
plt.xlabel('Otros')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["salon_ventas"]) 
plt.title("Outliers de salon_ventas")
plt.show()

#Método aplicando desviación estandar. Encuentro los valores extremos
y=df["salon_ventas"]
Limite_Superior= y.mean() + 3*y.std()
Limite_Inferior= y.mean() - 3*y.std()
print("Limite superior permitido", Limite_Superior)
print("Limite inferior permitido", Limite_Inferior)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior)|(y<Limite_Inferior)]
outliers_iqr

#Obtenemos datos limpios
data_clean= df[(y<=Limite_Superior)&(y>=Limite_Inferior)]
data_clean

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["salon_ventas"]) 
plt.title("Outliers de salon_ventas")
plt.show()

data_clean["salon_ventas"].to_csv('salon_ventas.csv')


