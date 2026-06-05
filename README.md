# Proyecto: Predicción de Churn en Servicios SaaS (Regresión Logística)

Este repositorio contiene la implementación de un modelo de clasificación binaria para predecir el abandono (churn) de clientes. El proyecto forma parte de la asignatura de **Métodos Numéricos**, aplicando técnicas de optimización y estadística computacional.

## Estructura del Proyecto
- `/data`: Contiene el dataset sintético `churn_data.csv`.
- `/src`: Contiene la lógica de negocio.
    - `model.py`: Script para el entrenamiento y serialización del modelo.
    - `inference.py`: Script para realizar predicciones sobre nuevos datos.
- `model.pkl` y `scaler.pkl`: Modelos entrenados y escaladores serializados para inferencia.

## Requisitos
- Python 3.x
- Librerías: `pandas`, `numpy`, `scikit-learn`, `joblib`

Instalación de dependencias:
```bash
pip install -r requirements.txt
```
## Para probar que funciona la interfaz pon eso en la terminal

```bash
python src/inference.py   
```  

y introduce los datos que te piden para ver si dio