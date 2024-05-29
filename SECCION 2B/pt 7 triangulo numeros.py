#seccion:2B
#tema: loops
#punto 7
 
 # patron triangulo con numeros
filas = int(input("Introduce el número de filas: "))
numero = 1

for i in range(1, filas + 1):
    for j in range(i):
        print(numero, end=' ')
        numero += 1
    print()
