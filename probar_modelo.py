from modelo_sensor import SensorColmena


def ejecutar_pruebas_unitarias():

    # PRUEBA 1: Temperatura baja
    colmena_fria = SensorColmena("APIARIO-01", 30.0, 65.0)

    assert colmena_fria.estado_microclima == "ALERTA: ENFRIAMIENTO DE CRIA", \
        "Error en la alerta de temperatura baja"


    # PRUEBA 2: Temperatura optima
    colmena_optima = SensorColmena("APIARIO-02", 34.0, 60.0)

    assert colmena_optima.estado_microclima == "MICROCLIMA OPTIMO", \
        "Error en el rango de temperatura optima"


    # PRUEBA 3: Temperatura elevada
    colmena_caliente = SensorColmena("APIARIO-03", 38.0, 70.0)

    assert colmena_caliente.estado_microclima == "ALERTA: ESTRES TERMICO", \
        "Error en la alerta de temperatura elevada"


    print("==============================================")
    print(" TODAS LAS PRUEBAS UNITARIAS PASARON")
    print("==============================================")


if __name__ == "__main__":
    ejecutar_pruebas_unitarias()