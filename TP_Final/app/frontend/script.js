/* ============================================================
   script.js — Lógica de la aplicación: interacción con el
   formulario, validación, sincronización de deslizadores,
   renderizado de resultados e historial local (localStorage).
   Depende de cliente.js (variable global: clienteAPI).
   ============================================================ */

(function () {
  "use strict";

  const CLAVE_HISTORIAL = "predicciones_historial";
  const MAX_HISTORIAL = 10;

  // ---------- Referencias al DOM ----------
  const formulario     = document.getElementById("form-prediccion");
  const inputTv        = document.getElementById("tv");
  const inputRadio     = document.getElementById("radio");
  const inputPrensa    = document.getElementById("prensa");
  const rangoTv        = document.getElementById("tv-rango");
  const rangoRadio     = document.getElementById("radio-rango");
  const rangoPrensa    = document.getElementById("prensa-rango");
  const btnPredecir    = document.getElementById("btn-predecir");
  const btnTexto       = btnPredecir.querySelector(".btn-texto");
  const btnCargando    = btnPredecir.querySelector(".btn-cargando");
  const btnLimpiar     = document.getElementById("btn-limpiar");
  const mensaje        = document.getElementById("mensaje");
  const resultado      = document.getElementById("resultado");
  const valorResultado = document.getElementById("valor-resultado");
  const estadoPunto    = document.getElementById("estado-punto");
  const estadoTexto    = document.getElementById("estado-texto");
  const historialVacio = document.getElementById("historial-vacio");
  const historialCont  = document.getElementById("historial-contenedor");
  const cuerpoHistorial= document.getElementById("cuerpo-historial");
  const btnBorrarHist  = document.getElementById("btn-borrar-historial");

  // ---------- Sincronización input numérico ↔ deslizador ----------
  function sincronizar(entrada, rango) {
    const valor = parseFloat(entrada.value);
    if (Number.isFinite(valor)) {
      // si el valor supera el máximo del rango, lo amplía dinámicamente
      if (valor > parseFloat(rango.max)) rango.max = valor;
      rango.value = valor;
    }
  }
  function sincronizarInversa(rango, entrada) {
    entrada.value = rango.value;
  }

  inputTv.addEventListener("input",     () => sincronizar(inputTv, rangoTv));
  inputRadio.addEventListener("input",  () => sincronizar(inputRadio, rangoRadio));
  inputPrensa.addEventListener("input", () => sincronizar(inputPrensa, rangoPrensa));
  rangoTv.addEventListener("input",     () => sincronizarInversa(rangoTv, inputTv));
  rangoRadio.addEventListener("input",  () => sincronizarInversa(rangoRadio, inputRadio));
  rangoPrensa.addEventListener("input", () => sincronizarInversa(rangoPrensa, inputPrensa));

  // ---------- Validación ----------
  function leerYValidar() {
    const tv = parseFloat(inputTv.value);
    const radio = parseFloat(inputRadio.value);
    const prensa = parseFloat(inputPrensa.value);

    if (![tv, radio, prensa].every(v => Number.isFinite(v))) {
      throw new Error("Completá los tres campos con valores numéricos.");
    }
    if (tv < 0 || radio < 0 || prensa < 0) {
      throw new Error("Los valores de inversión no pueden ser negativos.");
    }
    return { tv, radio, prensa };
  }

  // ---------- Mensajes de estado ----------
  function mostrarMensaje(texto, tipo) {
    mensaje.textContent = texto;
    mensaje.className = "mensaje visible " + (tipo || "info");
  }
  function ocultarMensaje() {
    mensaje.className = "mensaje";
    mensaje.textContent = "";
  }

  // ---------- Cargando ----------
  function establecerCargando(cargando) {
    btnPredecir.disabled = cargando;
    btnTexto.hidden = cargando;
    btnCargando.hidden = !cargando;
    btnLimpiar.disabled = cargando;
  }

  // ---------- Formato del resultado ----------
  function formatearValor(numero) {
    const formateado = new Intl.NumberFormat("es", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(numero);
    return formateado + " " + (typeof UNIDAD_RESULTADO !== "undefined" ? UNIDAD_RESULTADO : "u.m.");
  }

  // ---------- Historial (localStorage) ----------
  function cargarHistorial() {
    try {
      return JSON.parse(localStorage.getItem(CLAVE_HISTORIAL)) || [];
    } catch {
      return [];
    }
  }

  function guardarEnHistorial(registro) {
    const historial = cargarHistorial();
    historial.unshift(registro); // más reciente primero
    if (historial.length > MAX_HISTORIAL) historial.length = MAX_HISTORIAL;
    localStorage.setItem(CLAVE_HISTORIAL, JSON.stringify(historial));
    renderizarHistorial();
  }

  function renderizarHistorial() {
    const historial = cargarHistorial();
    if (historial.length === 0) {
      historialVacio.hidden = false;
      historialCont.hidden = true;
      return;
    }
    historialVacio.hidden = true;
    historialCont.hidden = false;

    cuerpoHistorial.innerHTML = historial.map(reg => `
      <tr>
        <td>${reg.fecha}</td>
        <td>${reg.tv}</td>
        <td>${reg.radio}</td>
        <td>${reg.prensa}</td>
        <td class="destacado">${formatearValor(reg.prediccion)}</td>
      </tr>
    `).join("");
  }

  btnBorrarHist.addEventListener("click", () => {
    localStorage.removeItem(CLAVE_HISTORIAL);
    renderizarHistorial();
  });

  // ---------- Limpiar formulario ----------
  btnLimpiar.addEventListener("click", () => {
    formulario.reset();
    [rangoTv, rangoRadio, rangoPrensa].forEach(r => r.value = 0);
    resultado.hidden = true;
    ocultarMensaje();
    inputTv.focus();
  });

  // ---------- Envío del formulario ----------
  formulario.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    ocultarMensaje();
    resultado.hidden = true;

    let datos;
    try {
      datos = leerYValidar();
    } catch (error) {
      mostrarMensaje(error.message, "error");
      return;
    }

    establecerCargando(true);
    mostrarMensaje(
      "Enviando datos al modelo… La primera petición puede tardar hasta 30 segundos (plan gratuito de Render).",
      "info"
    );

    try {
      const prediccion = await clienteAPI.predecir(datos);
      valorResultado.textContent = formatearValor(prediccion);
      resultado.hidden = false;
      ocultarMensaje();

      guardarEnHistorial({
        fecha: new Date().toLocaleString("es", { dateStyle: "short", timeStyle: "short" }),
        tv: datos.tv,
        radio: datos.radio,
        prensa: datos.prensa,
        prediccion: prediccion
      });

      resultado.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } catch (error) {
      mostrarMensaje(error.message, "error");
    } finally {
      establecerCargando(false);
    }
  });

  // ---------- Indicador de estado del servidor ----------
  async function comprobarServidor() {
    const alcanzable = await clienteAPI.servidorAlcanzable();
    if (alcanzable) {
      estadoPunto.className = "punto ok";
      estadoTexto.textContent = "Backend en línea";
    } else {
      estadoPunto.className = "punto error";
      estadoTexto.textContent = "Backend no alcanzable";
    }
  }

  // ---------- Inicialización ----------
  renderizarHistorial();
  comprobarServidor();
  inputTv.focus();
})();
