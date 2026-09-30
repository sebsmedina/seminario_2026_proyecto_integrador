## Clase N° 5 - Del link que se cae al deploy propio

Actividades que llevamos a cabo en la clase:

1. Para comenzar vimos como funciona realmente Gradio de forma local (ante la imposibilidad de correrlo en Hugging Faces) y porque al cerrar nuestra PC dejaba de funcionar la app.

2. Vimos los conceptos de servidor y hosting, con sus diferencias. Vimos distintos tipos y como nos pueden ayudar (o no) para deployar nuestra app escrita en Python, siendo el PaaS el ideal para dicha tarea.

3. Exixten dos tipos de PaaS: WSGI y ASGI, siendo éste último el ideal para Gradio ya que usa Websockets, un protocolo de comunicación bidireccional entre cliente y servidor.

4. Generamos una cuenta en Render para poder deployar nuestra app. Ventajas: gratuito, soporta ASGI y se conecta desde GitHub.

5. Eliminamos las siguientes líneas en nuestro código que hacían referencia al decorador de Spaces de Hugging Face:

```bash
import spaces

@spaces.GPU
```

Y agregamos las siguientes que configuran el puerto de forma correcta para Render (localhost solo es accesible desde la máquina misma,
no puede atender solicitudes del exterior):
```bash
import os
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
```
Actualizamos nuestro repositorio luego de los cambios con *add*, *commit* y *push*.

6. En nuestro hub de Render vamos al boton *+New* y seleccionamos *New Web Service*. Allí seleccionamos el repositorio que aloja nuestra app. Solamente completamos el apartado *Start Command* y colocamos:
```bash
python app.py
```
En *Compute* pinchamos en la opción *Free* y luego en el botón *Deploy Web Service* y listo! Nuestra app está en proceso de ser desplegada.

7. App en Streamlit. Al igual que en Render, creamos una cuenta en Streamlit al conectarla con nuestro repositorio en GitHub.

8. Una vez creada nuestra cuenta, sobre el apartado Streamlit Playground seleccionamos crear una nueva app desde un repositorio en GitHub. Al solicitarnos la dirección del repositorio, colocaremos la que contiene nuestro proyecto integrador. Streamlit por si solo encontrará la ruta que contiene la aplicación. Solamente nos quedará apretar el botón *Deploy* para deplegar nuestra app.