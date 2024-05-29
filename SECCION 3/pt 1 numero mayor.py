# seccion: 3
# tema: listas
#punto 1
lista1=[2,-5,8,3,9]
lista2=[3,2,1]
lista_nombres=["mafe","andres","ernesto","juan","nico"]
lista1[2]

numero_mayor= -10000
for elemento in lista1:
    print(elemento)
    #comparar cada elemento con el numero_mayor
    if elemeto>numero_mayor:
        numero_mayor= elemento
print("el numero mayor es:", numero_mayor)