

opcion=0
while True:
    
    print(""" 
        ¿ Que es lo que desea hacer?  

        1)Sumar los numeros
        2)Restar los numero
        3)Multiplicar los numeros
        4)Dividir los numeros
        5)Obtener el porcentaje
        6)Apagar la calculadora    
    
    """)
    
    opcion= int(input ("Elija una de las opciones: "))
    
    if opcion==1: 
        n1 = float ( input("ingrese el primer numero: ")) 
        n2 = float (input("ingrese el segundo numero: "))
        print("-----------")
        print("la SUMA de ", n1,"y", n2," es igual a:", n1+n2)
        print("-----------")
    elif opcion == 2:
        n1 = float ( input("ingrese el primer numero: ")) 
        n2 = float (input("ingrese el segundo numero: "))
        print("-----------")
        print ("la RESTA entre ",n1,"y",n2," es igual a =", n1-n2)
        print("-----------")
    elif opcion==3:
        n1 = float ( input("ingrese el numero que desea multiplicar:")) 
        n2 = float (input("ingrese por cuanto desea multiplicar:"))
        print("-----------")
        print ("la MULTIPLICACION entre ",n1,"y",n2," es igual a =", n1*n2)
        print("-----------")
    elif opcion==4:
        n1 = float ( input("ingrese el numero que quiere dividir: ")) 
        n2 = float (input("ingrese por cuanto desea dividir: " ))
        print("-----------")
        print ("la DIVISION entre ",n1,"y",n2," es igual a =", n1/n2)
        print("-----------")
    elif opcion==5:
        n1 = float ( input("Cual es el procentaje que quiere obtener: ")) 
        n2 = float (input("Ingrese el numero del cual desea obtenr el porcentaje: "))
        print("-----------")
        print ("El ",n1, "de", n2, " es igual a: ", (n1*100)/n2 )
        print("-----------")
    elif opcion==6:
        break
    else:
        print("-----------")
        print("la opcion elegida no es correcta")
        print("-----------")
        
    
    
    
    
    