#seccion:3
#tema: listas
#punto 4

#dada una llista numeros hallar la mediana

lista_numeros = [5, 3, 8, 1, 9, 7, 4]
lista_ordenada = sorted(lista_numeros)

n = len(lista_ordenada)

mediana = lista_ordenada[n // 2]
print("La mediana es:", mediana)
