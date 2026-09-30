# Importamos la librería:
import gradio as gr
import spaces

# Decorador para Spaces
@spaces.GPU

# Definimos la función principal:
def greet(name, intensity):
    return "Hola, " + name + "!" * int(intensity)

# Estructura general del programa:
demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

# Main:
if __name__ == "__main__":
    demo.launch()