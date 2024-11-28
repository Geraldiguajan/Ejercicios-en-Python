# Factoria de un numero 
numero = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")


# Numeros primos 
print("Números primos entre 1 y 50:")
for numero in range(2, 51):
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, end=", ")


# Sumar digitos 
numero = int(input("Introduce un número entero: "))
suma = 0
for digito in str(abs(numero)):  
    suma += int(digito)
print(f"La suma de los dígitos de {numero} es: {suma}")

# invertir un numero 
numero = int(input("Introduce un número entero: "))
invertido = int(str(abs(numero))[::-1]) 
if numero < 0: 
    invertido = -invertido
print(f"El número invertido es: {invertido}")


# Promedio de calificaciones 
calificaciones = []
while True:
    calificacion = float(input("Introduce una calificación (o -1 para terminar): "))
    if calificacion == -1:
        break
    calificaciones.append(calificacion)
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")


