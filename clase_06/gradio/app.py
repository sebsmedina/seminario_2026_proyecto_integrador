import gradio as gr
# import spaces
import os
from datetime import datetime, date
from transformers import pipeline


# Se comenta la siguiente línea ya que solamente es válida para cuando se realiza
# el deploy mediante Spaces de Hugging Face
# @spaces.GPU

# Función principal
def saludar_y_calcular_edad(nombre, fecha_nacimiento_str):
    if not nombre or not fecha_nacimiento_str:
        return "Por favor, completa todos los campos."

    try:
        # Convertir de texto a fecha (Formato: AAAA-MM-DD)
        fecha_nac = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        hoy = date.today()
        
        # Cálculo exacto de la edad considerando mes y día
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

        if edad < 0:
            return "La fecha de nacimiento no puede ser en el futuro."

        return f"¡Hola, {nombre}! Tienes {edad} años."
    
    except ValueError:
        return "Por favor, ingresa la fecha en formato AAAA-MM-DD (ejemplo: 1995-08-25)."

def analizar_sentimiento(texto):
    if not texto or not texto.strip():
        return "Por favor, ingresa un texto para analizar el sentimiento."

    # Cargar el modelo de análisis de sentimientos en español
    analizador = pipeline(model="jobanpreet123/sentiment-spanish")
    
    # Analizar el sentimiento del texto
    resultado = analizador(texto)
    
    # Devolver el resultado como una cadena legible
    return f"Sentimiento: {resultado[0]['label']}, Confianza: {resultado[0]['score']:.2f}"

# Separamos aplicaciones por pestañas
# Estructura con Blocks
with gr.Blocks() as demo:
    gr.Markdown("# Aplicaciones Clase N° 6 Seminario de actualización")
    with gr.Tab("Calculadora de edad"):
        gr.Markdown("Ingresa tu nombre y fecha de nacimiento para calcular tu edad.")
        nombre = gr.Textbox(label="Tu nombre", placeholder="Ej. Ana")
        fecha_nacimiento = gr.Textbox(
            label="Fecha de nacimiento", 
            placeholder="AAAA-MM-DD (ej. 2000-05-15)"
        )
        salida = gr.Textbox(label="Respuesta")
        boton = gr.Button("Calcular edad")

        # Se pasan ambos componentes como una lista en inputs
    boton.click(
        fn=saludar_y_calcular_edad, 
        inputs=[nombre, fecha_nacimiento], 
        outputs=salida
        )
    with gr.Tab("Análisis de Sentimientos"):
        gr.Markdown("Resumen en una frase como te sentiste en tu cumpleaños:")
        texto_sentimiento = gr.Textbox(label="Texto para analizar", placeholder="Ej. Me sentí muy feliz.")
        salida_sentimiento = gr.Textbox(label="Resultado")
        boton_sentimiento = gr.Button("Analizar sentimiento")

        # Se pasan ambos componentes como una lista en inputs
    boton_sentimiento.click(
        fn=analizar_sentimiento,
        inputs=[texto_sentimiento],
        outputs=salida_sentimiento
    )

# Main
if __name__ == "__main__":
    demo.launch(share=True)