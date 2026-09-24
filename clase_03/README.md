## Clase N° 3 - Preparación del entorno de desarrollo

Actividades que llevamos a cabo en la clase: GitHub, Codespaces y control de versiones

1. Iniciamos con un repaso rápido sobre los comandos que aprendimos en la clase 2 con respecto a la creación de un
entorno de desarollo y configurarlo para utilizar Git en él:

```bash
python --version
python -m venv .venv

.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
git add .
git commit -m "mensaje"
```
2. Generamos una cuenta en GitHub y creamos nuestro primero repositorio. Obtuvimos su URL para utilizarlo en el futuro.

ATENCIÓN! Si ya generaste un archivo README.md en tu repositorio local, al crear un repositorio remoto, no tildar la opción *generar un archivo README.md*


3. Aprendimos el concepto de un Codespace: un entorno de desarrollo brindado por GitHub que corre en Linux. Ideal para cuando no disponemos de nuestra máquina o no queremos instalar programas en ella. Gratuito, pero de uso limitado. Vemos que cuando lo inicializamos, se conecta automaticamente a nuestro repositorio en GitHub:

```bash
$ git remote -v
origin  https://github.com/usuario/repo.git (fetch)
origin  https://github.com/usuario/repo.git (push)
```

4. Utilizamos Copilot, la IA de asistencia brindada tanto por GitHub como por Visual Studio Code.

5. Conectamos nuestro repositorio local (en nuestra máquina) con el repositorio remoto (en nuestra cuenta de GitHub):

```bash
git remote -v
git remote add origin https://github.com/usuario/repo.git
git remote -v
git push -u origin main
```
Se establece la diferencia entre la rama "*main*" (local) y la rama "*origin*" (remoto).

6. Comandos básicos para manipular ramas en Git:

```bash
git branch              # Lista las ramas, marca con * la activa
#   main
# * feature-login
git checkout main       # (o: git switch main) Cambiar entre ramas
git branch -m nombre_viejo nombre_nuevo     # Renombrar rama
```

