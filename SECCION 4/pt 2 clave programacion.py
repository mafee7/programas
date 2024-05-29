#seccion:4
#tema:diccionarios
#punto 2

 # Verificar si la clave 'Programacion' está presente en el diccionario anidado
diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}}


for nombre in diccionario:
    if 'Programacion' in diccionario[nombre]:
        print(nombre)
