## Clase N° 3 - GitHub, Codespaces y control de versiones

#### 🎯 Objetivos:
Conectar nuestro repositorio local con GitHub. Importancia del README.

#### 📂 Contenido de esta Carpeta
| Nombre del archivo | Descripción |
|---|---|
| `README.md` | Pasos para conectar nuestro repositorio local con el remoto |

#### ⚙️ Requisitos Previos
- Tener inicializado Git en nuestro repositorio local y habernos autenticado por única vez.

#### 📋 Desarrollo

1. Generar una cuenta en GitHub.

2. Crear nuestro primer repositorio con el botón **New** y le damos nombre y caracter de público o privado. 

**ATENCIÓN!** Si ya generaste un archivo README.md en tu repositorio local, al crear un repositorio remoto, no tildar la opción *generar un archivo README.md*

**NOTA**: crear un archivo README.md es opcional tecnicamente, pero es lo primero que se ve cuando entramos en cualquier repositorio.

3. Una vez creado el repositorio, con el botón **Code** -> HTTPS copiamos la URL para utilizarlo en el futuro.

4. Se genera un Codespace: un entorno de desarrollo brindado por GitHub que corre en Linux. Ideal para cuando no disponemos de nuestra máquina o no queremos instalar programas en ella. Gratuito, pero de uso limitado. Se conecta automaticamente a nuestro repositorio en GitHub al inicializarlo:

**Terminal CODESPACE**
```bash
$ git remote -v
origin  https://github.com/usuario/repo.git (fetch)
origin  https://github.com/usuario/repo.git (push)
```

5. Conectamos nuestro repositorio local (en nuestra máquina) con el repositorio remoto (en nuestra cuenta de GitHub):

```bash
git remote -v
git remote add origin https://github.com/usuario/repo.git # enlace a nuestro repositorio remoto en GitHub
git remote -v
git push -u origin main
```
*git push origin main* envía todos los archivos que guardamos en el **staging area** con *git add* y luego de guardar el punto de control con *git commit*.

Se establece la diferencia entre la rama "*main*" (local) y la rama "*origin*" (remoto).

6. Comandos básicos para manipular ramas en Git:

```bash
git branch              # Lista las ramas, marca con * la activa
#   main
# * feature-login
git checkout main       # (o: git switch main) Cambiar entre ramas
git branch -m nombre_viejo nombre_nuevo     # Renombrar rama
```

