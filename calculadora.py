#### Output
import math
print("calculadora.py")
print("Operadores")
print("=========================================")
y = int(input("Introducir el primer numero: "))
x = int(input("Intruducir el segundo valor: "))
print("=========================================")

print("Selecciona una operaciòn:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Logaritmo")


instruccion = int(input("Con que operador quieres (?) "))

if instruccion >= 7:
    print("Valor no vàlido.")
else:
    print("Puedes seguir usando el programa. ")

if instruccion==1:
    y + x
    print("El valor de la operaciòn es: ", y+x)

if instruccion==2:
    y-x
    print("El valor de la operaciòn es: ", y-x)

if instruccion==3:
    y*x
    print("El valor de la operaciòn es: ", y*x)

if instruccion==4:
    y/x
    print("El valor de la operaciòn es: ", y/x)

if instruccion==5:
    y ** x
    print("El valor de la operaciòn es: ", y ** x)

if instruccion==6:
    print("El valor de la operaciòn es: ", math.log(y,x))
