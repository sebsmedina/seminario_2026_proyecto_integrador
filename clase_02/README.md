## Clase N° 2 - Preparación del entorno de desarrollo

#### 🎯 Objetivos:
Carpeta del Proyecto Integrador. Entorno virtual creado y activado. *requirements.txt* generado. Git configurado. Repositorio local con nuestro primer commit.

#### 📂 Contenido de esta Carpeta
| Nombre del archivo | Descripción |
|---|---|
| `app.py` | Contiene el código de una pequeña app en Gradio|
| `README.md` | Pasos para editar nuestro archivo `app.py` |
| `requirements.txt` | Archivo de texto con las librerías necesarias para nuestro entorno virtual |

#### ⚙️ Requisitos Previos
Antes de ejecutar el código, asegúrate de tener instalado:
- Visual Studio Code (o cualquier editor de código de tu preferencia)
- Python 3.8 o superior

#### 💻 Instalación y Uso Local

```bash
# Clonar repositorio
git clone https://github.com/sebsmedina/seminario_2026_proyecto_integrador/clase_02
cd clase_02
```

#### 📋 Desarrollo

1. Dentro de la carpeta de nuestro proyecto, crear una carpeta de nombre `clase_02`. Dentro de ella y, mediante nuestro editor de código (Visual Studio code), creamos un archivo *app.py*, el cual se alojará todo el Back-end de nuestra aplicación.

2. Creamos el entorno virtual de nuestro proyecto ingresando por la terminal el siguiente comando:

```bash
# crear y activar (Windows)
> python -m venv .venv
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

**CONSEJO**: siempre crear un entorno virtual para cada proyecto. Asegura aislamiento, organización y reproducibilidad.

3. Utilizaremos Gradio, una librería de Python que permite crear interfaces web interactivas para modelos de aprendizaje automático y funciones de inteligencia artificial, para gestionar la API y la interfaz de nuestra aplicación.

Instalaremos todas las librerías necesarias con *pip* utilizando *requierements.txt*

```bash
(.venv) > pip install -r requirements.txt
```
Instalará entre otras librerías:

```bash
gradio        # Framework para desplegar apps basadas en modelos de ML
spaces        # paquete de utilidades de Hugging Face para desplegar trabajos en HF Spaces
streamlit     # otro framework de código abierto
requests      # instalamos dependencias para consumir API's
```

4. Almacenamos en un archivo *requimerents.txt* las librerías instaladas para que puedan ser replicadas en el futuro.

```bash
(.venv) > pip freeze > requirements.txt     # guardamos la lista
                                            # para quien necesite replicarla
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
.venv/          # carpeta de nuestro entorno virtual
__pycache__/    # contiene código fuente de Python escrito en bajo nivel
```

6. Para visualizar que tenemos en nuestro repositorio local:

```bash
> git init              # Iniciamos un nuevo repositorio
> git status -u         # Lo que Git ve en la carpeta de nuestro proyecto
```

7. Añadimos nuestros archivos con las últimas modificaciones al área de preparación (*add*) y las guardamos en el historial de nuestro repositorio local (*commit*).

```bash
> git add .                         # Agregamos todos los
                                    # archivos al área de preparación (en nuestro solamente app.py)
> git commit -m "mi_primer_commit"  # Guardamos la actualización
                                    # junto con un mensaje descriptivo
```