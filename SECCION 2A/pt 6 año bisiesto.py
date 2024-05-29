#secion: 2A
#tema: condicionales
#punto 6

#programa para verificar si un año es bisiesto o no
año = int(input("Ingrese un año: "))

es_bisiesto = False

if año % 4 == 0:
    if año % 100 != 0 or año % 400 == 0:
        es_bisiesto = True

if es_bisiesto:
    print("El año es bisiesto.", es_bisiesto)
else:
    print("El año  no es bisiesto.", es_bisiesto)
