"""
Archivo: prediccion.py
Este archivo contiene la lógica del modelo de predicción. 
Se encarga de cargar el modelo entrenado y predice los ingresos 
basados en el presupuesto de publicidad en TV, radio y periódico.
"""

# PASO 1 · Importar las herramientas
from pathlib import Path   # Arma la ruta del archivo del modelo
import joblib              # Carga el modelo guardado

# PASO 2 · Carga del modelo UNA sola vez
# Se ejecuta cuando arranca la API.
RUTA_MODELO = Path(__file__).parent / "modelos" / "modelo.joblib"
modelo = joblib.load(RUTA_MODELO)

# Paso 4 · Función que predice los ingresos
def predecir_ingresos(inversion_tv, inversion_radio, inversion_prensa):
    # 4.1 · scikit-learn espera una tabla (lista de filas), aunque sea una sola predicción.
    presupuesto = [[inversion_tv, inversion_radio, inversion_prensa]]

    # 4.2 · predict devuelve una lista con la predicción; [0] toma la primera (y única).
    ingresos_predichos = modelo.predict(presupuesto)[0]

    # 4.3 · Devolver el resultado como diccionario: FastAPI lo convertirá en JSON
    return {
        "ingresos_predichos": round(float(ingresos_predichos), 2)
    }

# PASO 5 · Prueba rápida (opcional): descomentar para probar el modelo sin la API
# if __name__ == "__main__":
#     print(predecir_ingresos(125.1, 63.5, 71.4))