import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('pedidos.csv')

# Procesar los datos para obtener la información necesaria

# Convertir la columna 'pedido' de string a lista de tuplas
df['pedido'] = df['pedido'].apply(eval)

# Obtener la cantidad de pedidos de delivery y pickup
cantidad_tipo_pedido = df['tipo_pedido'].value_counts()

# Obtener la cantidad de cada tipo de pizza
cantidad_tipos_pizza = df['pedido'].apply(lambda x: pd.Series(x)).stack().value_counts()

# Crear un filtro para contar las veces que se pide pizza mediana y grande
filtro_mediana = df['pedido'].apply(lambda x: any('mediano' in sublist for sublist in x))
filtro_grande = df['pedido'].apply(lambda x: any('grande' in sublist for sublist in x))

# Obtener la cantidad de veces que se pide pizza mediana y grande
cantidad_mediana = df[filtro_mediana].shape[0]
cantidad_grande = df[filtro_grande].shape[0]

# Generar gráfico de pizza para cantidad pedidos delivery y pickup
plt.figure(figsize=(8, 6))
plt.pie(cantidad_tipo_pedido, labels=cantidad_tipo_pedido.index, autopct='%1.1f%%', startangle=140)
plt.title('Cantidad de Pedidos: Delivery vs Pickup')
plt.axis('equal')
plt.show()

# Generar gráfico de barras para cantidad de tipos de pizza
plt.figure(figsize=(8, 6))
cantidad_tipos_pizza.plot(kind='bar', color='skyblue')
plt.title('Cantidad de cada Tipo de Pizza')
plt.xlabel('Tipo de Pizza')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Obtener la cantidad de veces que se pide pizza mediana y grande
cantidad_mediana = df[filtro_mediana].shape[0]
cantidad_grande = df[filtro_grande].shape[0]
# Generar histograma para cantidad de veces que se pide pizza mediana y grande
plt.figure(figsize=(6, 8))
# Crear una lista con los datos de cantidad de veces de pizza mediana y grande
data = [cantidad_mediana, cantidad_grande]
# Crear barras con la frecuencia en el eje y
plt.bar(['Pizza Mediana', 'Pizza Grande'], data, color=['lightgreen', 'lightblue'])
plt.title('Cantidad de Veces que se Pide Pizza Mediana y Grande')
plt.xlabel('Tamaño de Pizza')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()

