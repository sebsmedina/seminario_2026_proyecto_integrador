# ===============================================================
#   Traductor Inglés <-> Español con Hugging Face Transformers
#   Prototipo de aplicación interactiva para traducir frases.
# ===============================================================

# Importar librerías necesarias:
import os
import gradio as gr
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

# Función que llama a Gradio:
def traducir(par: str, texto: str) -> str:
    if not texto or not texto.strip():
        return ""
    traductor = crear_traductor(par)
    return traducir_texto(traductor, texto.strip())

# Interfaz de usuario con Gradio:


with gr.Blocks(title="Traductor EN/ES", theme=gr.themes.Soft()) as demo:
    gr.Markdown("#  Traductor Inglés <-> Español")

    par_idioma = gr.Dropdown(
        choices=list(MODELOS.keys()),
        value="Español -> Inglés (es-en)",
        label="Par de idiomas",
    )

    with gr.Row():
        with gr.Column():
            texto_entrada = gr.Textbox(
                lines=6, label="Texto original", placeholder="Escribí acá el texto a traducir..."
            )
            with gr.Row():
                btn_traducir = gr.Button("Traducir", variant="primary")
        with gr.Column():
            texto_salida = gr.Textbox(lines=6, label="Traducción", interactive=False)

    btn_traducir.click(
        fn=traducir,
        inputs=[par_idioma, texto_entrada],
        outputs=texto_salida,
    )

    # Enter en el cuadro de texto también dispara la traducción
    texto_entrada.submit(
        fn=traducir,
        inputs=[par_idioma, texto_entrada],
        outputs=texto_salida,
    )


# Launch de la aplicación:
if __name__ == "__main__":
    demo.launch(share=True)
