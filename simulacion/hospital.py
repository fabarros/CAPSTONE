from datetime import date, datetime, timedelta
from random import uniform, random, seed, randint, gauss
import numpy as np
import pandas as pd
import csv
import seaborn as sns
from matplotlib import pyplot as plt
from otras_clases import *
from parametros import *
from copy import copy


class Hospital:
    def __init__(self, recursos, tasas, tiempos):
        self.recursos = recursos
        self.tasas = tasas
        self.tiempos = tiempos
        self.calendario = None
        self.n_pacientes_atendidos = {"GRD1": 0, "GRD2": 0, "GRD3": 0, "GRD4": 0, "GRD5": 0, "GRD6": 0, "GRD7": 0,
                                      "GRD8": 0, "GRD9": 0, "GRD10": 0}
        self.n_pacientes_privado = {"GRD1": 0, "GRD2": 0, "GRD3": 0, "GRD4": 0, "GRD5": 0, "GRD6": 0, "GRD7": 0,
                                    "GRD8": 0, "GRD9": 0, "GRD10": 0}
        self.llegadas_durante_semana = []
        self.enfermeras = []
        self.sillones = []
        self.crear_calendario_recursos()

    @property
    # operacion matematica que retorna la tasa de ocupacion del hospital
    # guardar en una lista las tasas cada vez que se actualiza.
    def tasa_de_ocupacion(self):
        return None

    def crear_calendario_recursos(self):

        # Se crean las enfermeras del Hospital
        for e in range(self.recursos["enfermeras"]):
            enfermera = Enfermera()
            self.enfermeras.append(enfermera)

        # Se crean los sillones del Hospital
        for s in range(self.recursos["sillones"]):
            sillon = Sillon()
            self.sillones.append(sillon)

            # Se crean todas los bloques

        inicio = datetime(2020, 1, 1, 8, 0)  # comenzamos el calendario el 1 de enero del 2020 a las 8:00
        calendario = []  # creamos lista de calendario vacía
        asignacion = {}
        for i in range(1, 54):  # existen 53 semanas por año
            for j in range(1, 8 - self.tiempos["dias_sin_trabajar"]):  # existen 5 dias de trabajo por semana
                s = copy(self.sillones)
                e = copy(self.enfermeras)
                for k in range(self.tiempos["bloques"]): # existen 51 bloques de a 15 minutos por dia (hasta las 20:45-21:00 hrs)
                    asignacion[str(inicio)] = {"sillones_desocupados": s,
                                               "enfermeras_desocupadas": e}
                    inicio += timedelta(minutes=15)
                inicio += timedelta(days=1)
                inicio -= timedelta(minutes=self.tiempos["bloques"] * 15)
            inicio += timedelta(days=self.tiempos["dias_sin_trabajar"])

        for f in calendario:
            asignacion[str(f)] = {"sillones_desocupados": s.extend(self.sillones),
                                  "enfermeras_desocupadas": e.extend(self.enfermeras)}
        self.calendario = asignacion

    # se crea una lista con todos los pacientes que llegaron durante la semana
    # esto es el input para la funcion asignar_llegadas
    def llegadas_semana(self):
        n_GRD1 = np.random.poisson(self.tasas["grd1"], 1)[0]
        for p in range(n_GRD1):
            r = random()
            if 0 < r < peso_protocolo_1:  # CAMBIAR ESTOS PESOS
                paciente = Paciente(GRD1_1)
            else:
                paciente = Paciente(GRD1_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD2 = np.random.poisson(self.tasas["grd2"], 1)[0]
        for p in range(n_GRD2):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD2_1)
            else:
                paciente = Paciente(GRD2_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD3 = np.random.poisson(self.tasas["grd3"], 1)[0]
        for p in range(n_GRD3):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD3_1)
            else:
                paciente = Paciente(GRD3_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD4 = np.random.poisson(self.tasas["grd4"], 1)[0]
        for p in range(n_GRD4):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD4_1)
            else:
                paciente = Paciente(GRD4_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD5 = np.random.poisson(self.tasas["grd5"], 1)[0]
        for p in range(n_GRD5):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD5_1)
            else:
                paciente = Paciente(GRD5_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD6 = np.random.poisson(self.tasas["grd6"], 1)[0]
        for p in range(n_GRD6):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD6_1)
            else:
                paciente = Paciente(GRD6_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD7 = np.random.poisson(self.tasas["grd7"], 1)[0]
        for p in range(n_GRD7):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD7_1)
            else:
                paciente = Paciente(GRD7_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD8 = np.random.poisson(self.tasas["grd8"], 1)[0]
        for p in range(n_GRD8):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD8_1)
            else:
                paciente = Paciente(GRD8_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD9 = np.random.poisson(self.tasas["grd9"], 1)[0]
        for p in range(n_GRD9):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD9_1)
            else:
                paciente = Paciente(GRD9_2)
            self.llegadas_durante_semana.append(paciente)

        n_GRD10 = np.random.poisson(self.tasas["grd10"], 1)[0]
        for p in range(n_GRD10):
            r = random()
            if 0 < r < peso_protocolo_1:
                paciente = Paciente(GRD10_1)
            else:
                paciente = Paciente(GRD10_2)
            self.llegadas_durante_semana.append(paciente)

    # esto es un for que toma cada paciente que llego en la semana
    # y lo va asignando (se modifica su protocolo y el calendario del hospital)
    # para ordenar el self.llegadas_durante_semana usamos lista.sort(key=lambda x: x.tiempo_espera, reverse=False)
    def asignar_llegadas(self):
        self.llegadas_durante_semana.sort(key=lambda x: x.tiempo_espera, reverse=False)
        print(self.llegadas_durante_semana)


if __name__ == "__main__":
    h1 = Hospital(recursos_h2, lambda_poisson_h2, tiempo_h2)
    print("ESTOS SON LOS RECURSOS DEL HOSPITAL:")
    print("CALEDARIO:\n", h1.calendario, len(h1.calendario))
    print("ENFERMERAS:\n", h1.enfermeras, len(h1.enfermeras))
    print("SILLONES:\n", h1.sillones, len(h1.sillones))
    h1.llegadas_semana()
    print("PACIENTES EN LA SEMANA:\n", h1.llegadas_durante_semana, len(h1.llegadas_durante_semana))
    h1.asignar_llegadas()
