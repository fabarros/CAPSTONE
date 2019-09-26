from random import random
from parametros import peso_tiempo_0, peso_tiempo_2, peso_tiempo_3


class Paciente:
    id = 1

    def __init__(self, protocolo):
        self.protocolo = protocolo
        self.cancer = protocolo
        self.id = Paciente.id
        Paciente.id += 1
        self.privado = False
        i = random()
        if 0 < i < peso_tiempo_0:
            self.tiempo_espera = 0
        elif peso_tiempo_0 < i < peso_tiempo_0 + peso_tiempo_2:
            self.tiempo_espera = 2
        elif peso_tiempo_0 + peso_tiempo_2 < i < peso_tiempo_0 + peso_tiempo_2 + peso_tiempo_3:
            self.tiempo_espera = 3

    def __repr__(self):
        ret = "Paciente  " + str(self.id)
        return ret


class Enfermera:
    id = 1

    def __init__(self):
        self.id = Enfermera.id
        Enfermera.id += 1
        self.pacientes_actuales = []

    def __repr__(self):
        ret = "Enfermera  " + str(self.id)
        return ret


class Sillon:
    id = 1

    def __init__(self):
        self.id = Sillon.id
        Sillon.id += 1

    def __repr__(self):
        ret = "Sillon  " + str(self.id)
        return ret
