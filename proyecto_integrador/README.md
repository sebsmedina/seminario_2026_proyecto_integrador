# Traductor EN/ES (Transformers + Gradio)

App de traducción con HuggingFace `pipeline` e interfaz web Gradio, correspondiente al Trabajo Práctico Integrador de la materia **Seminario de Actualización** de la Tecnicatura en Ciencia de Datos e IA del IFTS N° 18. La construcción del mismo será mostrada en clase mediante una presentación, junto a un informe realizado en PDF y el notebook de Jupyter donde se detallan las decisiones llevadas a cabo por el alumno.

## Ejecutar local

```bash
pip install -r requirements.txt
python app_gradio.py
# abrir http://localhost:7860
```

## Despliegues opcionales:

## 1. Deploy en Render (Docker, recomendado)

1. Subir este repo a GitHub.
2. En Render: **New + → Web Service → conectá el repo**.
3. Runtime: **Docker** (En caso de elegir ésta opción, crear el `Dockerfile` correspondiente).
4. El build descarga los pesos de los modelos una sola vez (quedan en la imagen).
5. Variable de entorno: `PORT` la inyecta Render solo (no hace falta setearla).

## Deploy en Render (nativo, sin Docker)

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app_gradio.py`
- Los pesos se descargan en el primer request. Para evitarlas, agregar al build command:
  `python -c "from huggingface_hub import snapshot_download; snapshot_download('Helsinki-NLP/opus-mt-es-en'); snapshot_download('Helsinki-NLP/opus-mt-en-es')"`

## Notas

- Free tier de Render: 512 MB RAM y se apaga tras 15 min de inactividad.
  La app carga **un solo modelo a la vez** para entrar en ese límite.
- De necesitar más RAM o arranque en frío más rápido, contemplar un plan pago o
  un disco persistente apuntando `HF_HOME=/data/hf_cache`.
