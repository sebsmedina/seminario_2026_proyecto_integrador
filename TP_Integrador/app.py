# ===============================================================
#   Traductor Inglés <-> Español con Hugging Face Transformers
# ===============================================================

# Importar librerías necesarias:
import os
import gradio as gr
from transformers import pipeline

# Modelos de traducción:
MODELOS = {
    "Español -> Inglés (es-en)": "Helsinki-NLP/opus-mt-es-en",
    "Inglés -> Español (en-es)": "Helsinki-NLP/opus-mt-en-es",
}

# Función para crear el pipeline de traducción:
# Crea y devuelve un pipeline de traducción para el par de idiomas elegido.
def crear_traductor(par: str):
    if par not in MODELOS:
        raise ValueError(
            f"Par '{par}' no soportado. Opciones: {', '.join(MODELOS)}")
    return pipeline(
        task="translation",
        model=MODELOS[par])

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

# Respuestas predeterminadas para el usuario:
respuestas_predeterminadas = [
    ["Muchas gracias por su comentario. Lo esperamos nuevamente!"],
    ["Le pedimos disculpas por los inconvenientes ocasionados. Trabajaremos para mejorar nuestro servicio."],
    ["Valoramos su sugerencia. La tendremos en cuenta para futuras mejoras."],
    ["Le agradecemos por sus estrellas. Nos alegra saber que tuvo una buena experiencia con nuestro servicio."]
]

# Encabezado y descripción de la aplicación:
with gr.Blocks(title="Traductor EN/ES", theme=gr.themes.Soft()) as demo:
    gr.Markdown("#  Traductor Inglés <-> Español")
    gr.Markdown("Elige el par de idiomas, escribe o pega tu frase y presiona Traducir.")

    par_idioma = gr.Dropdown(choices=list(MODELOS.keys()),
                             value="Inglés -> Español (en-es)",
                             label="Par de idiomas")

# Diseño de la interfaz con filas y columnas:
    with gr.Row():
        with gr.Column():
            texto_entrada = gr.Textbox(lines=6,
                                       label="Texto original",
                                       placeholder="Escribe o pega aquí el texto a traducir...")
            with gr.Row():
                btn_traducir = gr.Button("Traducir", variant="primary")
                btn_limpiar = gr.Button("Limpiar")

        with gr.Column():
            texto_salida = gr.Textbox(lines=6,
                                      label="Traducción",
                                      interactive=False,
                                      placeholder="La traducción aparecerá acá...",
                                      buttons=["copy"])

    # Acciones de los botones:
    # Botón Traducir:
    btn_traducir.click(
        fn=traducir,
        inputs=[par_idioma, texto_entrada],
        outputs=texto_salida,
    )
    # Botón Limpiar:
    btn_limpiar.click(lambda: ("", ""),
                    outputs=[texto_entrada,
                            texto_salida])

    # Código para que al preionar Enter en el cuadro de 
    # texto también dispare la traducción:
    texto_entrada.submit(
        fn=traducir,
        inputs=[par_idioma, texto_entrada],
        outputs=texto_salida,
    )

    # Cuadro para mostrar las respuestas predeterminadas:
    gr.Examples(label="Respuestas predeterminadas", examples=respuestas_predeterminadas, inputs=[texto_entrada])


# Launch de la aplicación:
if __name__ == "__main__":
    demo.launch(share=True)
