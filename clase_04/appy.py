# Importamos la librería:
import gradio as gr
import spaces

@spaces.GPU
def saludar(nombre):
    return f"Hola, {nombre}!"

with gr.Blocks() as demo:
    nombre = gr.Textbox(label="Tu nombre")
    salida = gr.Textbox(label="Respuesta")
    boton  = gr.Button("Saludar")
 
    boton.click(fn=saludar, inputs=nombre, outputs=salida)
 
if __name__ == "__main__":
    demo.launch()
