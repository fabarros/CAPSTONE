from datetime import *

# peso del protocolo 1
peso_protocolo_1 = 0.83

# peso de los tiempos maximos de espera
peso_tiempo_0 = 0.25
peso_tiempo_2 = 0.62
peso_tiempo_3 = 0.13

# tiempos laborales
tiempo_h1 = {"bloques": 52,"dias_sin_trabajar": 2}
tiempo_h2 = {"bloques": 52,"dias_sin_trabajar": 1}
tiempo_h3 = {"bloques": 52,"dias_sin_trabajar": 2}


# parámetros de poissons
lambda_poisson_h1 = {"grd1": 5,
                     "grd2": 5,
                     "grd3": 5,
                     "grd4": 5,
                     "grd5": 5,
                     "grd6": 5,
                     "grd7": 5,
                     "grd8": 5,
                     "grd9": 5,
                     "grd10": 5}

lambda_poisson_h2 = {"grd1": 5,
                     "grd2": 5,
                     "grd3": 5,
                     "grd4": 5,
                     "grd5": 5,
                     "grd6": 5,
                     "grd7": 5,
                     "grd8": 5,
                     "grd9": 5,
                     "grd10": 5}

lambda_poisson_h3 = {"grd1": 5,
                     "grd2": 5,
                     "grd3": 5,
                     "grd4": 5,
                     "grd5": 5,
                     "grd6": 5,
                     "grd7": 5,
                     "grd8": 5,
                     "grd9": 5,
                     "grd10": 5}

# enfermeras y sillones por hospital
recursos_h1 = {"sillones": 13, "enfermeras": 4}
recursos_h2 = {"sillones": 20, "enfermeras": 6}
recursos_h3 = {"sillones": 13, "enfermeras": 4}

# tiempos de espera y modulos necesarios
GRD1_1 = [(timedelta(days=0), 2), (timedelta(days=1), 2), (timedelta(days=1), 2), (timedelta(days=4), 4),
          (timedelta(days=1), 4), (timedelta(days=1), 4), (timedelta(days=6), 2), (timedelta(days=1), 2),
          (timedelta(days=1), 2), (timedelta(days=1), 2)]
GRD1_2 = [(timedelta(days=0), 5), (timedelta(days=3), 5), (timedelta(days=4), 4), (timedelta(days=3), 4),
          (timedelta(days=4), 3), (timedelta(days=3), 3)]
GRD2_1 = [(timedelta(days=0), 4), (timedelta(days=1), 4), (timedelta(days=1), 4), (timedelta(days=4), 6),
          (timedelta(days=1), 6), (timedelta(days=5), 6), (timedelta(days=3), 6)]
GRD2_2 = [(timedelta(days=0), 5), (timedelta(days=4), 5), (timedelta(days=4), 5), (timedelta(days=4), 5),
          (timedelta(days=4), 5), (timedelta(days=4), 5), (timedelta(days=4), 5), (timedelta(days=3), 5),
          (timedelta(days=3), 5), (timedelta(days=3), 5)]
GRD3_1 = [(timedelta(days=0), 4), (timedelta(days=1), 4), (timedelta(days=1), 4), (timedelta(days=1), 4),
          (timedelta(days=1), 4), (timedelta(days=8), 5), (timedelta(days=1), 5), (timedelta(days=1), 5),
          (timedelta(days=8), 5), (timedelta(days=1), 5), (timedelta(days=1), 5)]
GRD3_2 = [(timedelta(days=0), 7), (timedelta(days=1), 7), (timedelta(days=6), 7), (timedelta(days=1), 7),
          (timedelta(days=6), 10), (timedelta(days=1), 10), (timedelta(days=1), 10), (timedelta(days=8), 12),
          (timedelta(days=1), 12), (timedelta(days=8), 12), (timedelta(days=1), 12)]
GRD4_1 = [(timedelta(days=0), 12), (timedelta(days=1), 12), (timedelta(days=8), 12), (timedelta(days=8), 12),
          (timedelta(days=1), 12)]
GRD4_2 = [(timedelta(days=0), 8), (timedelta(days=1), 8), (timedelta(days=8), 12), (timedelta(days=1), 12),
          (timedelta(days=8), 14), (timedelta(days=1), 14)]
GRD5_1 = [(timedelta(days=0), 11), (timedelta(days=1), 11), (timedelta(days=1), 15),
          (timedelta(days=8), 10), (timedelta(days=1), 12), (timedelta(days=1), 12)]
GRD5_2 = [(timedelta(days=0), 8), (timedelta(days=1), 10), (timedelta(days=8), 8),
          (timedelta(days=1), 12), (timedelta(days=8), 6), (timedelta(days=1), 6),
          (timedelta(days=1), 6), (timedelta(days=1), 6), (timedelta(days=1), 6)]
GRD6_1 = [(timedelta(days=0), 16), (timedelta(days=4), 16), (timedelta(days=3), 16),
          (timedelta(days=4), 16), (timedelta(days=3), 20), (timedelta(days=1), 10),
          (timedelta(days=1), 8)]
GRD6_2 = [(timedelta(days=0), 20), (timedelta(days=2), 20), (timedelta(days=2), 20),
          (timedelta(days=2), 20), (timedelta(days=2), 20), (timedelta(days=2), 20)]
GRD7_1 = [(timedelta(days=0), 12), (timedelta(days=3), 8), (timedelta(days=3), 12),
          (timedelta(days=3), 8), (timedelta(days=3), 12), (timedelta(days=3), 8),
          (timedelta(days=3), 12), (timedelta(days=3), 8)]
GRD7_2 = [(timedelta(days=0), 15), (timedelta(days=3), 10), (timedelta(days=1), 10),
          (timedelta(days=8), 15), (timedelta(days=3), 15), (timedelta(days=3), 10),
          (timedelta(days=8), 15), (timedelta(days=2), 10), (timedelta(days=2), 10)]
GRD8_1 = [(timedelta(days=0), 22), (timedelta(days=1), 22), (timedelta(days=8), 22),
          (timedelta(days=1), 22), (timedelta(days=8), 22), (timedelta(days=3), 18)]
GRD8_2 = [(timedelta(days=0), 30), (timedelta(days=3), 10), (timedelta(days=3), 10),
          (timedelta(days=3), 15), (timedelta(days=3), 15), (timedelta(days=3), 15),
          (timedelta(days=2), 15)]
GRD9_1 = [(timedelta(days=0), 8), (timedelta(days=1), 10), (timedelta(days=8), 10), (timedelta(days=1), 8),
          (timedelta(days=8), 10), (timedelta(days=1), 8)]
GRD9_2 = [(timedelta(days=0), 15), (timedelta(days=1), 9), (timedelta(days=5), 9), (timedelta(days=3), 10),
          (timedelta(days=1), 10), (timedelta(days=5), 8), (timedelta(days=3), 20)]
GRD10_1 = [(timedelta(days=0), 12), (timedelta(days=1), 12), (timedelta(days=1), 12), (timedelta(days=5), 12),
           (timedelta(days=1), 12), (timedelta(days=1), 12), (timedelta(days=5), 12), (timedelta(days=1), 12),
           (timedelta(days=1), 12)]
GRD10_2 = [(timedelta(days=0), 16), (timedelta(days=4), 20), (timedelta(days=4), 12), (timedelta(days=4), 12),
           (timedelta(days=4), 12), (timedelta(days=4), 20), (timedelta(days=4), 10)]
