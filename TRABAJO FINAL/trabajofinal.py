# Trabajo Final Modulos y Paquetes

# Curso: Módulos y Paquetes para Machine Learning con Python
# Nombre: Cynthia Farfan Penagos
# ID: 1640976

## Análisis de Datos con NumPy, Pandas y Matplotlib

### Objetivo
#Aplicar los conocimientos de **NumPy, Pandas y Matplotlib** para analizar un conjunto de datos, realizar cálculos estadísticos y visualizar los resultados mediante gráficos.

#---

# Creación del Dataset

#1. Crear un conjunto de datos que contenga información de ventas con las siguientes columnas:

#- Producto
#- Precio
#- Cantidad
#- Ciudad

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame con los datos de ventas de productos de Misha Rastrera

data = {
    'Producto': ['Agua de Rosas 50 ml', 'Shampoo Solido Rulos 70 g', 'Mix Oliva y Oregano 30 ml', 'Pomada de Calendula 20 g', 'Repelente de Hierba Luisa 75 ml', 'Aceite de Ricino 30 ml'],
    'Precio': [18, 25, 25, 17, 18, 20],
    'Cantidad': [77, 100, 133, 29, 36, 85],
    'Ciudad': ['Lima', 'Cusco', 'Lima', 'Trujillo', 'Huaraz', 'Cusco']
}

# Convertir estos datos en un **DataFrame de Pandas**

ventas_mr = pd.DataFrame(data)

# Mostrar el DataFrame completo en consola.
print("-------------------------Dataset de Ventas--------------------")
print(ventas_mr)
print("\n")

# Manipulación de Datos con Pandas
#Realizar las siguientes operaciones sobre el DataFrame:

#1. Crear una nueva columna llamada **Ventas**, calculada como:
#Precio × Cantidad

ventas_mr['Ventas'] = ventas_mr['Precio'] * ventas_mr['Cantidad']

#2. Mostrar el DataFrame actualizado con la nueva columna.
print("-------------------------Dataset con Columna Ventas--------------------")
print(ventas_mr)
print("\n")

#3. Calcular las siguientes estadísticas:

#- Promedio de ventas
#- Venta máxima
#- Venta mínima
#- Suma total de ventas

stats_pandas = {
    'Promedio de Ventas': ventas_mr['Ventas'].mean(),
    'Venta Maxima': ventas_mr['Ventas'].max(),
    'Venta Minima': ventas_mr['Ventas'].min(),
    'Suma Total de Ventas': ventas_mr['Ventas'].sum()
}
print("-------------------------Estadisticas con Pandas--------------------")
for key, value in stats_pandas.items():
    print(f"{key}: {value}")
print("\n")

# Filtrado de Datos

#Realizar los siguientes filtros:

#1. Mostrar solo las ventas realizadas en una ciudad específica (por ejemplo: Lima).

ventas_lima = ventas_mr[ventas_mr['Ciudad'] == 'Lima']
print("-------------------------Ventas en Lima--------------------")
print(ventas_lima)
print("\n")

ventas_cusco = ventas_mr[ventas_mr['Ciudad'] == 'Cusco']
print("-------------------------Ventas en Cusco--------------------")
print(ventas_cusco)
print("\n")

#2. Mostrar los productos cuyas ventas sean mayores a 1000.
ventas_mayores_1000 = ventas_mr[ventas_mr['Ventas'] > 1000]
print("-------------------------Productos con Ventas Mayores a 1000--------------------")
print(ventas_mayores_1000)
print("\n")

#3. Mostrar los productos cuya cantidad vendida sea mayor a 5.
ventas_cantidad_mayor_5 = ventas_mr[ventas_mr['Cantidad'] > 5]
print("-------------------------Productos con Cantidad Vendida Mayor a 5--------------------")
print(ventas_cantidad_mayor_5)
print("\n")

# Cálculos con NumPy

#1. Convertir la columna **Ventas** del DataFrame en un **array de NumPy**.
ventas_array = np.array(ventas_mr['Ventas'])
print("-------------------------Array de Ventas--------------------")
print(ventas_array)
print("\n")

#2. Usar NumPy para calcular:

#- Media
#- Desviación estándar
#- Valor máximo
#- Valor mínimo

media_ventas = np.mean(ventas_array)
desviacion_ventas = np.std(ventas_array)
max_ventas = np.max(ventas_array)
min_ventas = np.min(ventas_array)   
print("-------------------------Estadisticas con NumPy--------------------")
print(f"Media de Ventas: {media_ventas}")
print(f"Desviación Estándar de Ventas: {desviacion_ventas}")
print(f"Valor Máximo de Ventas: {max_ventas}")
print(f"Valor Mínimo de Ventas: {min_ventas}")
print("\n")

# Visualización de Datos con Matplotlib

#Crear los siguientes gráficos:

### 1. Gráfico de Barras
#Mostrar las **ventas por producto**.

# Configurar el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(ventas_mr['Producto'], ventas_mr['Ventas'], color='skyblue')
plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_misha.png')  # Guardar el gráfico como imagen
plt.show()

### 2. Gráfico de Líneas
#Mostrar la **cantidad vendida de los productos**.
# Configurar el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(ventas_mr['Producto'], ventas_mr['Cantidad'], marker='o', color='orange', linestyle='--')
plt.title('Cantidad Vendida por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('unidades_vendidas.png')  # Guardar el gráfico como imagen
plt.show()

### 3. Gráfico de Pastel
#Mostrar la **distribucion de ventas por ciudad**.
# Agrupar las ventas por ciudad
ventas_por_ciudad = ventas_mr.groupby('Ciudad')['Ventas'].sum() 

# Configurar el gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(ventas_por_ciudad, labels=ventas_por_ciudad.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribucion de Ventas por Ciudad')
plt.axis('equal')  # Para que el gráfico sea circular
plt.savefig('distribucion_ventas_ciudad.png')  # Guardar el gráfico como imagen
plt.show()

# Análisis de Resultados

#Responder las siguientes preguntas:

#1. ¿Qué producto genera mayores ventas?

# El producto estrella es el Mix Oliva y Oregano 30 ml.
#Aunque no es el producto más caro, su volumen de ventas (133 unidades) lo impulsa a generar un ingreso total de S/ 3,325.
#Supera incluso al Shampoo Sólido, que tiene un precio mayor pero menos unidades vendidas.

#2. ¿Qué ciudad tiene mayor volumen de ventas?

#Lima lidera en ventas con un total de S/ 4,711.00, gracias principalmente al éxito del Mix Oliva y Oregano.

#3. ¿Cuál es el promedio de ventas?

# El promedio de Ventas: 1675.33 soles

#4. ¿Existe mucha variación en las ventas?

#Sí, existe mucha variación. Esto se debe a que el portafolio de productos de Misha Rastrera es heterogéneo. 
#Tenemos productos de alta demanda y precio moderado (como el Mix de Oliva y el Shampoo Sólido) que elevan las ventas, 
#frente a productos de nicho o menor rotación (como la Pomada de Caléndula) que se encuentran muy por debajo del promedio. 
#Esta dispersión sugiere que la empresa depende fuertemente de 2 o 3 productos estrella."

#5. ¿Qué producto debería promocionarse más según los datos?

#El producto que debería promocionarse más es la Pomada de Calendula 20 g.



