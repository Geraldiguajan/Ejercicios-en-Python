# Saludo personalizado 
def saludo_personalizado(nombre):
    return f"Hola, {nombre}!"
nombre = input("Introduce tu nombre: ")
print(saludo_personalizado(nombre))

# Suma de dos numeros 
def sumar(n1, n2):
    return n1 + n2
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print(f"La suma es: {sumar(num1, num2)}")

# Numero par o impar 
def es_par(numero):
    return numero % 2 == 0
numero = int(input("Introduce un número: "))
if es_par(numero):
    print("El número es true.")
else:
    print("El número es false.")


# Calcular el cuadrado 
def calcular_cuadrado(numero):
    return numero ** 2
numero = float(input("Introduce un número: "))
print(f"El cuadrado de {numero} es: {calcular_cuadrado(numero)}")


# Calcular el area de un circulo
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2
radio = float(input("Introduce el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}")
