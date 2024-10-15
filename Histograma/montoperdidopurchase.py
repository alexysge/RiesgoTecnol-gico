import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Histograma del monto perdido por mes por transacciones de tipo "purchase" con estado fraudulento:

data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas y nuevos usuarios
fraudulent_transactions = data[(data['status'] == 'fraudulent')]

# Filtrar para transacciones de tipo "purchase"
purchase_fraud = fraudulent_transactions[fraudulent_transactions['transaction_type'] == 'purchase']

# Crear el histograma para mostrar el monto perdido por mes en transacciones de tipo "purchase"
plt.figure(figsize=(12, 6))
sns.histplot(data=purchase_fraud, x='month', weights='amount', bins=12, kde=True, color='green', label='purchase fraud')

# Títulos y etiquetas
plt.title('Monto perdido por mes en transacciones de tipo purchase fraudulentas')
plt.xlabel('Mes')
plt.ylabel('Monto perdido')
plt.grid(True)

# Mostrar la gráfica
plt.legend()
plt.show()


