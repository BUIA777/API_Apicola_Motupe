import os
import math

from flask import Flask, request, jsonify
from dotenv import load_dotenv

from modelo_sensor import SensorColmena


# Cargar variables de entorno
load_dotenv()

# Crear servidor Flask
app = Flask(__name__)

# Historial temporal de mediciones
historial_colmenas = []

# Leer configuracion
nombre_empresa = os.environ.get(
    "NOMBRE_EMPRESA",
    "Apicola Motupe"
)

modo_sistema = os.environ.get(
    "MODO_SISTEMA",
    "PRODUCCION"
)

puerto = int(os.environ.get("PUERTO_LOCAL", 5000))


# ==========================================
# ENDPOINT 1: PAGINA PRINCIPAL
# ==========================================

@app.route("/", methods=["GET"])
def ruta_principal():

    return jsonify({
        "servicio": nombre_empresa,
        "modo": modo_sistema,
        "mensaje": "API Apicola Motupe funcionando correctamente"
    }), 200


# ==========================================
# ENDPOINT 2: CONSULTAR COLMENAS
# ==========================================

@app.route("/colmenas", methods=["GET"])
def consultar_colmenas():

    lista_colmenas = [
        colmena.convertir_a_diccionario()
        for colmena in historial_colmenas
    ]

    return jsonify({
        "total": len(lista_colmenas),
        "colmenas": lista_colmenas
    }), 200


# ==========================================
# ENDPOINT 3: REGISTRAR COLMENA
# ==========================================

@app.route("/colmenas", methods=["POST"])
def registrar_colmena():

    datos = request.get_json(silent=True)

    # Validar que se reciba un objeto JSON
    if not isinstance(datos, dict):

        return jsonify({
            "error": "Se requiere enviar un objeto JSON valido"
        }), 400

    # Validar campos obligatorios
    campos = ["apiario", "temperatura", "humedad"]

    for campo in campos:

        if campo not in datos:

            return jsonify({
                "error": f"Falta el campo obligatorio: {campo}"
            }), 400

    try:

        apiario = str(datos["apiario"]).strip()

        temperatura = float(datos["temperatura"])
        humedad = float(datos["humedad"])

        # Validar datos
        if not apiario:

            return jsonify({
                "error": "El nombre del apiario no puede estar vacio"
            }), 400

        if not math.isfinite(temperatura) or not math.isfinite(humedad):

            return jsonify({
                "error": "Los valores deben ser numeros validos"
            }), 400

        if not 0 <= humedad <= 100:

            return jsonify({
                "error": "La humedad debe estar entre 0 y 100"
            }), 400

        # Crear objeto SensorColmena
        nueva_colmena = SensorColmena(
            apiario,
            temperatura,
            humedad
        )

        # Guardar medicion
        historial_colmenas.append(nueva_colmena)

        # Respuesta JSON
        return jsonify({

            "mensaje": "Medicion registrada correctamente",

            "datos_guardados": nueva_colmena.convertir_a_diccionario()

        }), 201

    except (ValueError, TypeError):

        return jsonify({
            "error": "Formato de datos incorrecto"
        }), 400


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=puerto,
        debug=True
    )