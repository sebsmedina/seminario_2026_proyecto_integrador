"""
rutas/prediccion.py · RUTAS DE LA API
"""

# PASO 1 · Importar lo necesario
from fastapi import APIRouter               # permite definir rutas en un archivo aparte de main.py
from pydantic import BaseModel, Field       # para describir y validar los datos que llegan
from prediccion import predecir_ingresos    # la función que usa el modelo

# PASO 2 · Crear el router
# Es como una "mini app": acá se anotan las rutas y después main.py
# las suma a la aplicación con include_router.
router = APIRouter()

# PASO 3 · El modelo de datos: el CONTRATO de entrada
class IngresoInput(BaseModel):
    inversion_tv: float = Field(..., description="Inversión en publicidad en TV")
    inversion_radio: float = Field(..., description="Inversión en publicidad en radio")
    inversion_prensa: float = Field(..., description="Inversión en publicidad en prensa")

# PASO 4 · La ruta de la API
@router.post("/predecir-ingresos")
def predecir_ingresos_endpoint(ingreso: IngresoInput):
    return predecir_ingresos(
        inversion_tv=ingreso.inversion_tv,
        inversion_radio=ingreso.inversion_radio,
        inversion_prensa=ingreso.inversion_prensa
    )