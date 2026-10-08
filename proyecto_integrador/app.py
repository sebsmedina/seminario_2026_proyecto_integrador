# ===============================================================
#   Traductor Inglés <-> Español con Hugging Face Transformers
#   Prototipo de aplicación interactiva para traducir frases.
# ===============================================================

# Importar librerías necesarias:
from transformers import pipeline

# Modelos de traducción:
MODELOS = {
    "es-en": "Helsinki-NLP/opus-mt-es-en",
    "en-es": "Helsinki-NLP/opus-mt-en-es",
}

# Función para crear el pipeline de traducción:
def crear_traductor(par: str):
    """Crea y devuelve un pipeline de traducción para el par de idiomas elegido."""
    if par not in MODELOS:
        raise ValueError(
            f"Par '{par}' no soportado. Opciones: {', '.join(MODELOS)}"
        )
    
    return pipeline(
        task="translation",
        model=MODELOS[par],
    )

# Función para traducir un texto:
def traducir_texto(traductor, texto: str, max_length: int = 200) -> str:
    resultado = traductor(texto, max_length=max_length)
    return resultado[0]["translation_text"]

# Función principal:
def main():
    print("=== Traductor interactivo ===")
    print("Pares disponibles:", " | ".join(MODELOS))
    par = input("Elegí un par (ej: es-en): ").strip()
    traductor = crear_traductor(par)
    print(f"Traductor {par} listo. Ingrese texto para traducir o 'salir' para terminar.\n")
    while True:
        texto = input(">>> ").strip()
        if texto.lower() in ("salir", "exit", "quit"):
            break
        if not texto:
            continue
        print("Frase ingresada: ", texto)
        print("Traduccion: ", traducir_texto(traductor, texto), "\n")

# Función main:
if __name__ == "__main__":
    main()