"""
main.py · ARCHIVO PRINCIPAL DEL BACKEND
Función: crea la aplicación (la API), le configura CORS y 
enlaza las rutas del modelo, que están en rutas/prediccion.py.
"""

# PASO 1 · Importar lo necesario
from fastapi import FastAPI                               # Framework: la clase con la que se crea la API
from fastapi.middleware.cors import CORSMiddleware        # Pieza que resuelve CORS
from rutas.prediccion import router as rutas_prediccion   # Rutas del modelo, definidas en otro archivo

# PASO 2 · La aplicación
# "app" es una instancia de la clase FastAPI. Todo lo demás se configura 
# sobre ella.
# El título es el que aparece en la documentación automática (/docs).
app = FastAPI(title="API del modelo de predicción de ventas")

# PASO 3 · Ruta de prueba
# @app.get("/") -> DECORADOR: le dice a FastAPI "cuando llegue un GET,
# ejecutá la función de abajo". Sirve para comprobar que la API está viva
# abriendo http://localhost:8000 en el navegador.
@app.get("/")
def raiz():
    return {"mensaje": "La API del modelo está funcionando"}   # FastAPI convierte el diccionario en JSON

# PASO 3b · El chequeo de salud (health check)
# Verifica que la API sigue "viva". Si no responde, la plataforma
# en la nube (Render, Hugging Face, etc.) la reinicia.
@app.get("/health")
def health():
    return {"estado": "ok"}

# PASO 4 · Configurar CORS
# Petmite que el navegador pueda pedirle datos a la API 
# desde otro origen (dominio o puerto).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sebsmedina.github.io"],   # La ruta donde se aloja el frontend (GitHub Pages)
    allow_methods=["*"],   # se permiten todos los métodos (GET, POST, ...)
    allow_headers=["*"],   # se permiten todos los encabezados (incluye Content-Type)
)

# PASO 5 · Enlace de las rutas del modelo
# El router de rutas/prediccion.py se suma a la aplicación 
# con include_router.
app.include_router(rutas_prediccion, tags=["prediccion"])