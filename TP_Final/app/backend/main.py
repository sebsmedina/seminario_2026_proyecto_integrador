"""
main.py · LA APLICACIÓN (la API)
"""

# PASO 1 · Importar lo necesario
from fastapi import FastAPI                               # el framework: la clase con la que se crea la API
from fastapi.middleware.cors import CORSMiddleware        # la pieza que resuelve CORS
from rutas.prediccion import router as rutas_prediccion   # las rutas del modelo, definidas en otro archivo

# PASO 2 · La aplicación
# "app" es una instancia de la clase FastAPI. Todo lo demás se configura 
# sobre ella.
# El título es el que aparece en la documentación automática (/docs).
app = FastAPI(title="API del modelo de predicción de ventas")

# PASO 3 · Ruta de prueba
@app.get("/")
def raiz():
    return {"mensaje": "La API del modelo está funcionando"}   # FastAPI convierte el diccionario en JSON

# PASO 3b · El chequeo de salud (health check)
@app.get("/health")
def health():
    return {"estado": "ok"}

# PASO 4 · Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # "*" = cualquier origen puede llamar a la API (cómodo para practicar;
                           #       al publicar conviene poner solo la dirección de tu frontend)
    allow_methods=["*"],   # se permiten todos los métodos (GET, POST, ...)
    allow_headers=["*"],   # se permiten todos los encabezados (incluye Content-Type)
)

# PASO 5 · Enchufar las rutas del modelo
app.include_router(rutas_prediccion, tags=["prediccion"])