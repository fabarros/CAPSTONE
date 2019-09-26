class Motor_simulacion:
    def __init__(self, hospital1, hospital2, hospital3, protocolos):
        self.hospital1 = hospital1
        self.hospital2 = hospital2
        self.hospital3 = hospital3
        self.lista_hospitales = [self.hospital1, self.hospital2, self.hospital3 ]
        self.protocolos = protocolos
        self.costo = 0
        self.tiempo_simulacion = 0

    def run(self):
        while self.tiempo_simulacion mas chico que 1 año:
            for hospital in self.lista_hospitales:
                hospital.llegadas_semana()
                hospital.asignar_llegadas(self.tiempo_simulacion)
                self.tiempo_simulacion += timedelta(days = 7)