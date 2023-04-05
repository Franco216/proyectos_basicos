print( "-- BIENVENIDO A PAR O IMPAR --")

print("-- Ahora te pediremos que ingreses un numero que este comprendido de 1 a 1000 --")

num=int(input("ingrese el numero: "))
print("__________________________________________________________________")


if num < 0 or num >1000:
    print("el numero que ingreso no esta dentro del parametro establecido")
elif num%2==0:
    print("el numero es PAR")
else:
    print("el numero es IMPAR")