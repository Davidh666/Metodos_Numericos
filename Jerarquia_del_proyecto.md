Metodos_Numericos/
├── data/
│   ├── churn_data.csv        # Dataset original con la telemetría
│   └── generar_datos.py      # Script para la síntesis de datos
├── src/
│   ├── inference.py          # Script principal de inferencia (Demo)
│   ├── model.py              # Lógica de entrenamiento y definición del modelo
│   └── spline_processor.py   # Módulo de preprocesamiento avanzado
├── .gitignore                # Configuración de control de versiones
├── generar_datos_root.py     # Script generador de datos (Nivel raíz)
├── Jerarquia_del_proyecto.md # Documentación detallada de la estructura
├── model.pkl                 # Artefacto: Modelo entrenado (serializado)
├── README.md                 # Documentación técnica del proyecto
├── requirements.txt          # Dependencias y librerías necesarias
└── scaler.pkl                # Artefacto: Scaler (normalizador) serializado