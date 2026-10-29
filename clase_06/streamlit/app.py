import streamlit as st
from datetime import date
from transformers import pipeline

# Función principal
def calcular_edad(fecha_nac: date) -> int:
    """Calcula la edad exacta considerando mes y día."""
    hoy = date.today()
    edad = hoy.year - fecha_nac.year - (
        (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day)
    )
    return edad

def analizar_sentimiento(texto):
    if not texto or not texto.strip():
        return "Por favor, ingresa un texto para analizar el sentimiento."

    # Cargar el modelo de análisis de sentimientos en español
    analizador = pipeline(model="jobanpreet123/sentiment-spanish")
    
    # Analizar el sentimiento del texto
    resultado = analizador(texto)
    
    # Devolver el resultado como una cadena legible
    return f"Sentimiento: {resultado[0]['label']}, Confianza: {resultado[0]['score']:.2f}"

# Configuración de pestañas:
tab1, tab2 = st.tabs(["Calculadora de Edad", "Analizador de Sentimientos"])

# Configuración de la página "Calculadora de Edad"
with tab1:
    st.set_page_config(
        page_title="Calculadora de Edad",
        page_icon="🎂",
        layout="centered",
    )
    # Título de app
    st.title("🎂 Calculadora de edad")
    st.markdown("Ingresa tu fecha de nacimiento para saber cuántos años tienes:")

    # Formulario de entrada
    with st.form("formulario_edad"):
        nombre = st.text_input(
            "Tu nombre",
            placeholder="Ej. Ana",
            max_chars=50,
        )

        fecha_nacimiento = st.date_input(
            "Fecha de nacimiento",
            value=None,
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            format="YYYY-MM-DD",
            help="Selecciona tu fecha de nacimiento del calendario.",
        )

        enviar = st.form_submit_button("Calcular edad", type="primary")

    # Respuesta de la app
    if enviar:
        if not nombre.strip():
            st.warning("Por favor, ingresa tu nombre.")
        elif fecha_nacimiento is None:
            st.warning("Por favor, selecciona tu fecha de nacimiento.")
        elif fecha_nacimiento > date.today():
            st.error("La fecha de nacimiento no puede estar en el futuro!")
        else:
            edad = calcular_edad(fecha_nacimiento)
            nombre_limpio = nombre.strip().title()

            st.success(
                f"¡Hola, **{nombre_limpio}**! Tienes **{edad}** "
                f"{'año' if edad == 1 else 'años'}."
            )
with tab2:
    st.set_page_config(
        page_title="Analizador de Sentimientos",
        page_icon="📝",
        layout="centered",
    )
    st.title("📝 Analizador de Sentimientos")
    st.markdown(
        "Ingresa un texto para analizar el sentimiento expresado en él."
    )

    # Formulario de entrada
    with st.form("formulario_sentimiento"):
        texto = st.text_area(
            "Texto para analizar",
            placeholder="Ej. Me sentí muy feliz.",
            max_chars=500,
            height=150,
        )

        enviar_sentimiento = st.form_submit_button(
            "Analizar sentimiento", type="primary"
        )

    # Respuesta de la app
    if enviar_sentimiento:
        if not texto.strip():
            st.warning("Por favor, ingresa un texto para analizar.")
        else:
            analisis = analizar_sentimiento(texto)
            st.success(analisis)

st.divider()