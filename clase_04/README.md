## Clase N° 4 - Del repositorio local al Spaces

Actividades que llevamos a cabo en la clase:

1. Comenzamos la clase revisando algunos conceptos de programación: clases, funciones (métodos y atributos), variables locales y globales, Backend, Frontend y API. Entendimos que nuestro código solamente contenía el Backend de la aplicación, que nos faltaba todo lo demás para poder desplegarla.

2. Conocimos Hugging Face Spaces, una herramienta gratuita que permite alojar, probar y compartir aplicaciones web interactivas de inteligencia artificial y aprendizaje automático. Generamos un usuario y una cuenta.

3. Creamos un Space en HF para poder alojar allí nuestro repositorio. La diferencia entre GitHub y HF es que éste último levanta nuestro código y lo deja funcionando.

4. Una vez generado nuestro Space, observamos que el mismo posee ya su primer commit y un README.md creado automáticamente:

```bash
---
title: Mi App
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: ...
app_file: app.py
pinned: false
---


```
El sitio del repo en HF funciona correctamente.

5. En nuestra máquina, generamos un nuevo destino remoto para nuestro repo con el link del Space. Cuando conectemos, nos pedirá autorizar la conexión con el sitio de HF mediante un token de escritura (WRITE) generado allí mismo:

```bash
git remote add space https://huggingface.co/spaces/USUARIO/NOMBRE
git remote -v

```

"space" es el alias de nuestro nuevo repo remoto en HF.

6. Ejecutamos un push a dicho repo:

```bash
git push space main
```

Y nos devuelve un fallo. Se debe a la coexistencia del README.md generado de manera local en la clase 2 y el creado en el Space de HF. 
Con la siguiente linea le decimos a Git que tiene permiso para mezclarlos:

```bash
git pull space main --allow-unrelated-histories
```

Nos sugiere un nuevo README.md con la siguiente estructura:

```bash
<<<<<<< HEAD
(tu README, el de la Clase 2)
=======
(el README del Space, con su configuración)
>>>>>>>
```

7. Nos quedamos con nuestra versión inicial, borrando la otra y los marcadores. Ejecutamos *add*, *commit* y *push*:

```bash
git add README.md
git commit -m "Resuelvo el conflicto del README"
git push space main
```

El Space se construye, pero al ir al espacio inicial nos da ERROR.

8. El README.md creado por el Space contiene la configuración de la plataforma. Sin ella, no puede funcionar. Volvemos atrás con los cambios, dejamos la sugerencia (albergando ambos README.md en el mismo archivo) y nuevamente ejecutamos *add*, *commit* y *push*:

```bash
# Reponemos el encabezado al principio del README
git add README.md
git commit -m "Repongo la configuración del Space"
git push space main
```
