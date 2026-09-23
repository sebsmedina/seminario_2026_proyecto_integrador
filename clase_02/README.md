## Clase N° 2 - Preparación del entorno de desarrollo

Actividades que llevamos a cabo en la clase:

1. Creamos un archivo *app.py* en el se alojará todo el front-end de nuestra aplicación en Gradio.

2. Creamos el entorno virtual de nuestro proyecto con el siguiente comando:

```bash
# crear y activar (Windows)
> py -m venv .venv
> .venv\Scripts\activate

# macOS / Linux
$ python3 -m venv .venv
$ source .venv/bin/activat
```

Verificamos si está activado correctamente:

```bash
python -c "import sys;
print(sys.executable)"
```

3. Instalamos todas las librerías necesarias con *pip* y las almacenamos en un archivo *requimerents.txt* para que puedan ser replicadas en el futuro.

```bash
(.venv) > pip install requests               # instalamos dependencias

(.venv) > pip freeze > requirements.txt      # guardamos la lista

(.venv) > pip install -r requirements.txt    # para quien necesite replicarla
```

4. Uso de Git para organizar las distintas versiones de nuestro proyecto.

Identificarnos con Git al iniciarlo (necesario para ejecutar nuestros commits). Lo realizamos una única vez.

```bash
> git --version         # Versión de Git

> git config --global user.name "Nombre Apellido"   # Nuestro nombre
> git config --global user.email "tu@correo.com"    # Correo asociado a nuestra cuenta de GitHub
> git config --global init.defaultBranch main       # Setear nuestra rama principal
```

5. Creación de *.gitignore* para evitar que Git mueva archivos y/o carpetas que no queramos.
Por ejemplo:
```bash
.venv/
__pycache__/
```

Visualizamos que tenemos en nuestro repositorio local:

```bash
> git init              # Iniciamos un nuevo repositorio
> git status -u         # Lo que Git ve en la carpeta de nuestro proyecto
```

6. Añadimos nuestros archivos con las últimas modificaciones al área de preparación (*add*) y las guardamos en el historial de nuestro repositorio local (*commit*).

```bash
> git add .                         # Agregamos todos los
                                    # archivos al área de preparación
> git commit -m "mi_primer_commit"  # Guardamos la actualización
                                    # junto con un mensaje descriptivo
```




