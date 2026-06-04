import pandas as pd
import numpy as np
import os

# Asegurarnos de que la carpeta existe
if not os.path.exists('data'):
    os.makedirs('data')

# Generar los datos
np.random.seed(42)
df = pd.DataFrame({
    'session_duration': np.random.normal(30, 10, 500),
    'api_calls': np.random.normal(100, 25, 500),
    'support_tickets': np.random.poisson(2, 500),
    'is_churn': np.random.choice([0, 1], 500, p=[0.7, 0.3])
})

# Guardar forzando el formato correcto
df.to_csv('data/churn_data.csv', index=False, sep=',')
print("Archivo 'data/churn_data.csv' generado correctamente.")