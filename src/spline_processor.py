import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def suavizar_actividad_usuario(nodos_x, valores_y):
    """
    Usa un Spline Cúbico para reconstruir una curva suave de actividad.
    nodos_x: Puntos en el tiempo (ej. horas del día)
    valores_y: Nivel de actividad observado
    """
    # Creamos el spline
    spline = CubicSpline(nodos_x, valores_y)
    
    # Generamos una curva suave con más puntos para el análisis
    x_suave = np.linspace(nodos_x.min(), nodos_x.max(), 100)
    y_suave = spline(x_suave)
    
    return x_suave, y_suave

# --- Ejemplo de aplicación en tu proyecto ---
if __name__ == "__main__":
    # Supongamos que tenemos datos de actividad de un usuario a ciertas horas
    horas = np.array([0, 6, 12, 18, 24])
    actividad = np.array([10, 45, 110, 70, 15]) # Datos con "ruido" o dispersos
    
    x_s, y_s = suavizar_actividad_usuario(horas, actividad)
    
    plt.plot(horas, actividad, 'ro', label='Datos originales')
    plt.plot(x_s, y_s, 'b-', label='Spline Cúbico (Tendencia)')
    plt.title("Suavizado de actividad con Splines Cúbicos")
    plt.legend()
    plt.show()