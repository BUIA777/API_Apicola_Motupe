class SensorColmena:

    def __init__(self, apiario, temperatura, humedad):

        self.apiario = str(apiario)
        self.temperatura = float(temperatura)
        self.humedad = float(humedad)

        self.estado_microclima = self.evaluar_microclima()

    def evaluar_microclima(self):

        if self.temperatura < 32.0:
            return "ALERTA: ENFRIAMIENTO DE CRIA"

        elif 32.0 <= self.temperatura <= 36.0:
            return "MICROCLIMA OPTIMO"

        else:
            return "ALERTA: ESTRES TERMICO"

    def convertir_a_diccionario(self):

        return {
            "apiario": self.apiario,
            "temperatura": self.temperatura,
            "humedad": self.humedad,
            "estado": self.estado_microclima
        }