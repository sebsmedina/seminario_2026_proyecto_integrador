import streamlit as st
from datetime import date


def calcular_edad(fecha_nac: date) -> int:
    """Calcula la edad exacta considerando mes y día."""
    hoy = date.today()
    edad = hoy.year - fecha_nac.year - (
        (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day)
    )
    return edad


# Configuración de la página 
st.set_page_config(
    page_title="Saludo y calculadora de Edad",
    page_icon="🎂",
    layout="centered",
)

st.title("🎂 Calculadora de edad")
st.markdown("Ingresa tu nombre y tu fecha de nacimiento para saber cuántos años tienes.")

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

# ---------- Lógica de salida ----------
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

        # Detalle extra: días vividos
        dias_vividos = (date.today() - fecha_nacimiento).days
        # st.caption(f"📅 Has vivido aproximadamente {dias_vividos:,} días.")

st.divider()
# st.caption("Aplicación creada con Streamlit · Lista para desplegar en Render")