import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Histograma de los meses con transacciones fraudolentas

data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas y nuevos usuarios
fraudulent_transactions = data[(data['status'] == 'fraudulent')]

# Extraer el mes de la columna 'date'
fraudulent_transactions['month'] = pd.to_datetime(fraudulent_transactions['date']).dt.month

# Crear el histograma para mostrar las transacciones fraudulentas por mes
plt.figure(figsize=(12, 6))
sns.histplot(data=fraudulent_transactions, x='month', bins=12, kde=True, color='orange', label='transacciones fraudulentas')

# Títulos y etiquetas
plt.title('Distribución de transacciones fraudulentas por mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de transacciones')
plt.grid(True)

# Mostrar la gráfica
plt.legend()
plt.show()

