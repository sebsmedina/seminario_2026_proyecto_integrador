"""
rutas/prediccion.py · RUTAS DE LA API

Función: define la "puerta" por la que se le pide una predicción
al modelo:  POST /predecir-ingresos
"""

# PASO 1 · Liberías necesarias
from fastapi import APIRouter               # Define rutas en un archivo aparte de main.py
from pydantic import BaseModel, Field       # Describe y valida los datos que llegan
from prediccion import predecir_ingresos    # Función que usa el modelo

# PASO 2 · Crea el router
# Acá se anotan las rutas.
# main.py las suma a la aplicación con include_router.
router = APIRouter()

# PASO 3 · El modelo de datos: el CONTRATO de entrada.
# Esta clase describe qué JSON tiene que mandar el frontend:
# 3 números con estos nombres.
# float -> número con decimales
# gt = 0 -> tiene que ser mayor que 0
# examples -> valor de ejemplo que se muestra en /docs
class IngresoInput(BaseModel):
    inversion_tv: float = Field(..., gt = 0, examples = [125.0],
                                description="Inversión en publicidad en TV")
    inversion_radio: float = Field(..., gt = 0, examples = [10.0],
                                   description="Inversión en publicidad en radio")
    inversion_prensa: float = Field(..., gt = 0, examples = [50.0],
                                    description="Inversión en publicidad en prensa")

# PASO 4 · La ruta de la API
@router.post("/predecir-ingresos")
# Lógica del modelo: recibe un objeto IngresoInput con 
# las variables de entrada, llama a predecir_ingresos()
# y devuelve el resultado.
def predecir_ingresos_endpoint(ingreso: IngresoInput):
    return predecir_ingresos(
        inversion_tv=ingreso.inversion_tv,
        inversion_radio=ingreso.inversion_radio,
        inversion_prensa=ingreso.inversion_prensa
    )