#CONTARA CUANTAS PALABRAS HAY EN LA ORACION INGRESADA
print("--- BIENVENIDO AL CONTADOR DE PALABRAS ---")
frase=input("Ingrese su frase o pensamiento: ")

separador=" "

lista=frase.split(separador)

contador=0


if frase == "":
        print("No se ingreso la frase")
        
else:
    for palabra in lista:
        palabra
        contador += 1
    print("La frase o pensamiento que ingresaste cuenta con ", contador, " palabras")    




