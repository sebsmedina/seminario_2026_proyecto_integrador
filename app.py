<<<<<<< HEAD
# Importamos la librería:
import gradio as gr
import spaces

@spaces.GPU

# Definimos la función principal:
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

# Estructura general del programa:
demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

if __name__ == "__main__":
    demo.launch()
=======
import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
>>>>>>> b898c28aee8a4a58c6929fafad5c6ddd0e5a12d5
