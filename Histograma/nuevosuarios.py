import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Histograma de nuevos usuarios por mes y el monto de transacción fraudulenta:

# Cargar el archivo CSV
data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas y nuevos usuarios
fraudulent_transactions = data[data['status'] == 'fraudulent']

# Extraer el mes de la columna 'date'
fraudulent_transactions['month'] = pd.to_datetime(fraudulent_transactions['date']).dt.month

# Filtrar para nuevos usuarios
new_user_fraud = fraudulent_transactions[fraudulent_transactions['new_user'] == 1]

# Crear el histograma para mostrar la cantidad de nuevos usuarios por mes y el monto de transacciones fraudulentas
plt.figure(figsize=(12, 6))
sns.histplot(data=new_user_fraud, x='month', weights='amount', bins=12, kde=True, color='purple', label='fraude nuevos usuarios')

# Títulos y etiquetas
plt.title('Monto perdido por nuevos usuarios por mes en transacciones fraudulentas')
plt.xlabel('Mes')
plt.ylabel('Monto perdido')
plt.grid(True)

# Mostrar la gráfica
plt.legend()
plt.show()




