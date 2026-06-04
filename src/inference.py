import joblib
import numpy as np

# Cargar modelo y scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Datos de prueba (ejemplo: usuario con bajo tiempo y muchos tickets)
new_user = np.array([[10, 150, 5]]) # session=10, api=150, tickets=5
new_user_scaled = scaler.transform(new_user)

# Predicción
prob = model.predict_proba(new_user_scaled)[0][1]
print(f"Probabilidad de abandono (Churn): {prob:.2%}")