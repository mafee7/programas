#seccion: 2A
#tema. condicionales
#punto 9

#programa que determina el tipo de caracter
caracter = input("Ingrese un carácter: ")

if "A" <= caracter <= "Z" or "a" <= caracter <= "z":
    print("El carácter es una letra.", caracter)

if "0" <= caracter <= "9":
    print("El carácter es un dígito.", caracter)

else:
    print("El carácter es un carácter especial.", caracter)
