import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Histograma del monto perdido por mes por transacciones de tipo "transfer" con estado fraudulento:

data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas y nuevos usuarios
fraudulent_transactions = data[(data['status'] == 'fraudulent')]

# Formato para extraer solo la hora de la columna 'time'
fraudulent_transactions['hour'] = pd.to_datetime(fraudulent_transactions['time'], format='%H:%M').dt.hour

#Se define y se crea la gráfica
plt.figure(figsize=(12, 6))  # Ajusta el tamaño de la figura
sns.histplot(data=fraudulent_transactions, x='hour', weights='amount', bins=24, kde=True, color='red', label='fraudulent')

#Titulos
plt.title('Distribución del monto de transacciones fraudulentas por hora del día')
plt.xlabel('Hora del día')
plt.ylabel('Monto')
#cuadrícula en la gráfica 
plt.grid(True)  

#Mostramos la gráfica
plt.legend()
plt.show()

# Filtrar para transacciones de tipo "transfer"
transfer_fraud = fraudulent_transactions[fraudulent_transactions['transaction_type'] == 'transfer']

# Crear el histograma para mostrar el monto perdido por mes en transacciones de tipo "transfer"
plt.figure(figsize=(12, 6))
sns.histplot(data=transfer_fraud, x='month', weights='amount', bins=12, kde=True, color='orange', label='transfer fraud')

# Títulos y etiquetas
plt.title('Monto perdido por mes en transacciones de tipo transfer fraudulentas')
plt.xlabel('Mes')
plt.ylabel('Monto perdido')
plt.grid(True)

# Mostrar la gráfica
plt.legend()
plt.show()

