## Clase N° 6 - Consumir un modelo de IA por API

Actividades que llevamos a cabo en la clase:

1. Repaso de la ruta de aprendizaje desarrollada en la materia hasta el momento y de algunos conceptos y diferencias (función, clase, instancia, atributo, método)

2. Cómo consumir un modelo de IA:

a. *pipeline* de la librería *transformers* de Hugging Face:

```bash
from transformers import pipeline
pipe = pipeline(
"text-classification",
model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
)
pipe("Esta clase está buenísima")
```

Vemos que *pipeline* es una clase:

```bash
>>> type(pipeline)
<class 'function'>
```
*pipe* es una instancia de ella:
```bash
>>> type(pipe)
<class 'transformers.pipelines.text_classification.
TextClassificationPipeline'>
```
Y lo que devuelve:
```bash
>>> pipe("Esta clase está buenísima")
[{'label': 'Positive', 'score': 0.9...}]
```

3. Planteamos la diferencia entre entrenamiento e inferencia de un modelo de IA.

4. Diferencias entre *pipeline* e *InferenceClient()*:

| --- | pipeline | InferenceClient |
| --- | --- | --- |
| Dónde corre el modelo | En tu máquina (o en Colab) | En los servidores del proveedor |
| Qué instalás | transformers + PyTorch, y bajás el modelo | huggingface_hub, liviano 
| Qué necesitás | RAM y disco para el modelo | Internet y un token |
| Quién pone el límite | Tu hardware | El proveedor: cuota y disponibilidad |
| Tus datos | No salen de tu máquina | Viajan al proveedor |

5. Model card: el README.md del repositorio del modelo contiene la información para poder usarlo (cómo fue entrenado, con qué datos fue entranado, finalidad y limitaciones)

Exploramos la model card del siguiente modelo: huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment

6. Uso de *InferenceClient()*. Configuración del token de Hugging Face

```bash
import os
from huggingface_hub import InferenceClient
client = InferenceClient(
provider="hf-inference",
api_key=os.environ["HF_TOKEN"],
)
resultado = client.text_classification(
"esta clase me está costando pero se entiende",
model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
top_k=3,
)
for r in resultado:
print(r.label, r.score)
```

Tipos de error:
a. **401 Unauthorized**: Token mal copiado. Lo responde Hugging Face: el pedido sí llegó.

b. **KeyError: 'HF_TOKEN'**: La variable no está definida. Lo da nuestro dispositivo, antes de mandar algo.

7. Diferencias entre *pipeline* y *InferenceClient*()* en el código.

| --- | pipeline | InferenceClient |
| --- | --- | --- |
| Qué es | Función que devuelve un objeto | Clase que instanciás |
| El modelo | Se elige al crear el pipeline | En cada llamado al método |
| Qué devuelve | Lista de diccionarios: r["label"] | Lista de objetos: r.label |
| Cuántas etiquetas | Por defecto, solo la ganadora | Las que pidas con top_k |
| Token | token= | api_key=|

8. Agregado de los modelos a nuestras apps en Gradio y Streamlit de la clase 5.

a.  Gradio en Render: una pestaña nueva (gr.Tab), sin tocar lo que ya andaba. HF_TOKEN en Environment.

b. Streamlit en Community Cloud: el mismo llamado. HF_TOKEN en Advanced settings → Secrets.

c. huggingface_hub en el requirements.txt de las dos.

**ACLARACIÓN**: 

1. En la carpeta de la clase 6 están los repositorios para desplegar de forma local las app en Gradio y Streamlit respectivamente, separadas en la interfaz de la app de la clase 05 mediante pestañas. Se utilizó *pipeline* de *transformers* ya que actualmente no cuento con créditos en mi cuenta gratuita de Hugging Face :') para poder utilizar *InferenceClient()*.

2. El elegido es un modelo de análisis de sentimientos en idioma español. 
Link al modelo (No presenta model card :/):
[jobanpreet123/sentiment-spanish](https://huggingface.co/jobanpreet123/sentiment-spanish)

Desplegar de forma local la app en Gradio
```bash
>>> python app.py
```

Desplegar de forma local la app en Streamlit
```bash
>>> streamlit run app.py
```