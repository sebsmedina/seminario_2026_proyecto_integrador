import gradio as gr
import spaces
import os
from datetime import datetime, date

@spaces.GPU
def saludar_y_calcular_edad(nombre, fecha_nacimiento_str):
    if not nombre or not fecha_nacimiento_str:
        return "Por favor, completa todos los campos."

    try:
        # Convertir el texto a un objeto fecha (Formato: AAAA-MM-DD)
        fecha_nac = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        hoy = date.today()
        
        # Cálculo exacto de la edad considerando mes y día
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

        if edad < 0:
            return "La fecha de nacimiento no puede ser en el futuro."

        return f"¡Hola, {nombre}! Tienes {edad} años."
    
    except ValueError:
        return "Por favor, ingresa la fecha en formato AAAA-MM-DD (ejemplo: 1995-08-25)."


with gr.Blocks() as demo:
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

if __name__ == "__main__":
    demo.launch()