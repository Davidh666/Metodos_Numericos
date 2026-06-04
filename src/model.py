import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Cargar datos
df = pd.read_csv('data/churn_data.csv')
X = df.drop('is_churn', axis=1)
y = df['is_churn']

# 2. Preprocesamiento (Escalado crucial para Regresión Logística)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Entrenamiento
model = LogisticRegression()
model.fit(X_scaled, y)

# 4. Guardar modelo y scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Modelo entrenado y guardado exitosamente.")