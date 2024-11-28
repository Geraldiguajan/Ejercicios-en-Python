# Mayor o Menor 
numero = float(input("Introduce un número mayor o menor : "))

if numero > 10:
    print("Es mayor que 10.")
elif numero < 10:
    print("Es menor que 10.")


#  número positivo o negativo 
numero = float(input("Introduce un número positivo o negativo: "))

if numero > 0:
    print("Es un número positivo.")
elif numero < 0:
    print("Es un número negativo.")


#  número par o impar
numero = int(input("Introduce un número par o impar : "))

if numero % 2 == 0:
    print("Es par.")
else:
    print("Es impar.")

# Aprobado o Reprobado 
calificacion = float(input("Introduce la calificación: "))

if calificacion >= 7:
    print("Aprobado.")
else:
    print("Reprobado.")
