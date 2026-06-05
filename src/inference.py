import pandas as pd
import joblib

# Cargar modelo y scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

print("========================================")
print("     SISTEMA DE PREDICCIÓN DE CHURN     ")
print("========================================")

def get_clean_input(prompt):
    while True:
        try:
            val = input(prompt).replace(',', '.')
            return float(val)
        except ValueError:
            print(">> Error: Ingresa solo números.")

try:
    # 1. Capturar datos del usuario
    sesion = get_clean_input("Ingrese tiempo de sesión: ")
    api = get_clean_input("Ingrese llamadas API: ")
    tickets = get_clean_input("Ingrese tickets de soporte: ")
    almacenamiento = get_clean_input("Ingrese GB de almacenamiento: ")

    # 2. CREAR DATAFRAME CON LOS NOMBRES QUE EL MODELO/SCALER ESPERAN
    # Preferir los nombres guardados en el scaler, si existen; si no, usar los del modelo.
    if hasattr(scaler, 'feature_names_in_'):
        expected_names = list(scaler.feature_names_in_)
    elif hasattr(model, 'feature_names_in_'):
        expected_names = list(model.feature_names_in_)
    else:
        expected_names = ['session_duration', 'api_calls', 'support_tickets', 'almacenamiento']

    # Mapear los inputs capturados a los nombres esperados por el estimador.
    values = {'session': sesion, 'api': api, 'tickets': tickets, 'almacenamiento': almacenamiento}

    def match_name(name):
        n = name.lower()
        if any(k in n for k in ('session', 'sesion', 'durat', 'time')):
            return values['session']
        if 'api' in n:
            return values['api']
        if any(k in n for k in ('ticket', 'support', 'soporte')):
            return values['tickets']
        if any(k in n for k in ('almacen', 'storage', 'gb')):
            return values['almacenamiento']
        return None

    row = []
    for i, nm in enumerate(expected_names):
        v = match_name(nm)
        if v is None:
            # fallback por posición si no encontramos una coincidencia por texto
            fallback_order = ['session', 'api', 'tickets', 'almacenamiento']
            key = fallback_order[i] if i < len(fallback_order) else fallback_order[-1]
            v = values[key]
        row.append(v)

    input_data = pd.DataFrame([row], columns=expected_names)

    # 3. Inferencia
    scaled_data = scaler.transform(input_data)
    # Algunos modelos no implementan `predict_proba`; manejar eso.
    if hasattr(model, 'predict_proba'):
        prob = model.predict_proba(scaled_data)[0][1]
    else:
        pred = model.predict(scaled_data)[0]
        prob = float(pred)

    print("\n========================================")
    print(f"ANÁLISIS DE RIESGO: {prob * 100:.2f}%")
    print("========================================\n")

except Exception as e:
    print(f"\n--- ERROR ---")
    # Mostrar nombres esperados por scaler y por modelo (si están disponibles)
    try:
        scaler_names = getattr(scaler, 'feature_names_in_', None)
        model_names = getattr(model, 'feature_names_in_', None)
        print(f"Scaler espera: {scaler_names}")
        print(f"Modelo espera: {model_names}")
    except Exception:
        pass
    print(f"Detalle: {e}")