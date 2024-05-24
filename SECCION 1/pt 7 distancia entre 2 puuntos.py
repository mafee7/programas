# seccion: 1
# tema: basicos
#punto 7
#Calcular la distancia D entre dos puntos (x1, y1) y (x2, y2) en el planocartesiano. F ́ormula: D = √(x2 − x1)2 + (y2 − y1)2
x1 = float(input("Ingrese la coordenada x del primer punto\n "))
y1 = float(input("Ingrese la coordenada y del primer punto\n "))
x2 = float(input("Ingrese la coordenada x del segundo punto\n "))
y2 = float(input("Ingrese la coordenada y del segundo punto\n "))
D = √(x2 − x1)**2 + (y2 − y1)**2
print("La distancia entre los dos puntos es:", D)