# imprimir números del 1 al 10
for numero in range(1, 11):
    print(numero, end=", ")

# suma de los 10 primeros numeros 
suma = 0
for numero in range(1, 11):
    suma += numero
print(f"La suma de los primeros 10 números es: {suma}")


# Tabla de multiplicar 
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    
# Contar numeros pares
print("Números pares entre 1 y 20:")
for numero in range(2, 21, 2):
    print(numero, end=", ")
          
# Contador regresivo
print("Contador regresivo:")
for numero in range(10, 0, -1):
    print(numero, end=", ")
