/* ============================================================
   cliente.js — Cliente HTTP que se comunica con la API en Render.
   Toda la configuración de conexión está concentrada acá para
   que solo tengas que tocar un lugar al desplegar.
   ============================================================ */

// ╔══════════════════════════════════════════════════════════╗
// ║  CONFIGURACIÓN — MODIFICAR ESTOS VALORES AL DESPLEGAR    ║
// ╚══════════════════════════════════════════════════════════╝

// 1) URL de tu API en Render. SIN barra al final.
//    Ejemplo: "https://prediccion-ventas-api.onrender.com"
const API_BASE_URL = "https://seminario-2026-proyecto-integrador-tp.onrender.com";

// 2) Ruta del endpoint de predicción (la que definiste en rutas/prediccion.py).
//    Ejemplos comunes: "/predecir", "/prediccion", "/api/prediccion", "/predict".
const ENDPOINT_PREDICCION = "/predecir-ingresos";

// 3) Nombres de los campos que espera tu backend en el cuerpo JSON.
//    Si tu modelo Pydantic usa otros nombres (ej: "television", "periodico"),
//    cambialos acá. La clave de la izquierda es interna (no tocar).
const CAMPOS_SOLICITUD = {
  tv:     "inversion_tv",      // nombre de la clave para Inversión en Televisión
  radio:  "inversion_radio",   // nombre de la clave para Inversión en Radio
  prensa: "inversion_prensa"   // nombre de la clave para Inversión en Prensa
};

// 4) Tiempo máximo de espera (ms). El plan gratuito de Render puede tardar
//    hasta ~30 s en reactivarse tras estar inactivo.
const TIMEOUT_MS = 120000;

// 5) Unidad con la que se muestran los ingresos en la interfaz.
const UNIDAD_RESULTADO = "u.m.";


// ╔══════════════════════════════════════════════════════════╗
// ║  IMPLEMENTACIÓN DEL CLIENTE (no hace falta modificar)    ║
// ╚══════════════════════════════════════════════════════════╝

class ClientePrediccion {

  constructor(baseUrl, endpoint) {
    this.baseUrl = baseUrl.replace(/\/+$/, ""); // quita barras finales
    this.endpoint = endpoint.startsWith("/") ? endpoint : "/" + endpoint;
  }

  /**
   * Envía los tres valores de inversión y devuelve la predicción numérica.
   * @param {{tv: number, radio: number, prensa: number}} datos
   * @returns {Promise<number>} valor predicho de ingresos por ventas
   */
  async predecir(datos) {
    const cuerpo = {};
    cuerpo[CAMPOS_SOLICITUD.tv]     = Number(datos.tv);
    cuerpo[CAMPOS_SOLICITUD.radio]  = Number(datos.radio);
    cuerpo[CAMPOS_SOLICITUD.prensa] = Number(datos.prensa);

    const controlador = new AbortController();
    const temporizador = setTimeout(() => controlador.abort(), TIMEOUT_MS);

    let respuesta;
    try {
      respuesta = await fetch(this.baseUrl + this.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(cuerpo),
        signal: controlador.signal
      });
    } catch (error) {
      clearTimeout(temporizador);
      if (error.name === "AbortError") {
        throw new Error("El servidor tardó demasiado en responder. Si usás el plan gratuito de Render, esperá unos segundos y volvé a intentar.");
      }
      throw new Error("No se pudo conectar con el servidor. Verificá la URL de la API en cliente.js y que el backend esté activo en Render.");
    }
    clearTimeout(temporizador);

    if (!respuesta.ok) {
      let detalle = "";
      try {
        const errJson = await respuesta.json();
        detalle = errJson.detail ? JSON.stringify(errJson.detail) : "";
      } catch { /* la respuesta no era JSON */ }
      throw new Error(
        `El servidor respondió con error ${respuesta.status} (${respuesta.statusText}).` +
        (detalle ? ` Detalle: ${detalle}` : "")
      );
    }

    let datosRespuesta;
    try {
      datosRespuesta = await respuesta.json();
    } catch {
      throw new Error("La respuesta del servidor no es un JSON válido. Verificá que el endpoint devuelva JSON.");
    }

    return this._extraerPrediccion(datosRespuesta);
  }

  /**
   * Busca el valor numérico de la predicción dentro de la respuesta JSON,
   * probando los nombres de campo más habituales (flexible ante distintos backends).
   */
  _extraerPrediccion(datos) {
    const claves = [
      "prediccion", "prediccion_ingresos", "prediccion_ventas",
      "ingresos", "ventas", "valor", "resultado", "prediccion_valor",
      "predicted_sales", "prediction", "sales"
    ];

    // 1) búsqueda directa en el primer nivel
    for (const clave of claves) {
      if (typeof datos[clave] === "number" && Number.isFinite(datos[clave])) {
        return datos[clave];
      }
    }

    // 2) si viene dentro de un objeto anidado (data / detalle / resultado)
    for (const contenedor of ["data", "detalle", "resultado", "respuesta"]) {
      if (datos[contenedor] && typeof datos[contenedor] === "object") {
        for (const clave of claves) {
          const v = datos[contenedor][clave];
          if (typeof v === "number" && Number.isFinite(v)) return v;
        }
      }
    }

    // 3) último recurso: primer valor numérico finito encontrado
    for (const clave of Object.keys(datos)) {
      const v = datos[clave];
      if (typeof v === "number" && Number.isFinite(v)) return v;
    }

    throw new Error(
      "No se encontró el valor de la predicción en la respuesta del servidor. " +
      "Ajustá la función _extraerPrediccion en cliente.js según el formato que devuelve tu API."
    );
  }

  /**
   * Comprueba si el servidor es alcanzable (sin depender de CORS).
   * Usado para el indicador de estado del encabezado.
   */
  async servidorAlcanzable() {
    try {
      const controlador = new AbortController();
      setTimeout(() => controlador.abort(), 8000);
      // no-cors: no podemos leer el estado, pero si resuelve, el servidor está en línea
      await fetch(this.baseUrl, { method: "GET", mode: "no-cors", signal: controlador.signal });
      return true;
    } catch {
      return false;
    }
  }
}

// Instancia global que usará script.js
const clienteAPI = new ClientePrediccion(API_BASE_URL, ENDPOINT_PREDICCION);
