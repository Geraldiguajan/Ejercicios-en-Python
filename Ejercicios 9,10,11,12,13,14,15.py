# Calculadora basica 
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")
if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
     resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División entre cero no permitida"
else:
    resultado = "Operación no válida"
print(f"Resultado: {resultado}")

   
# Determinar un año bisiesto
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es bisiesto.")
else:
    print("No es bisiesto.")

# validar contraseñas 
contraseña_correcta = "172255"
contraseña = input("Introduce la contraseña: ")
if contraseña == contraseña_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
import random

# Juego de numeros 
numero_aleatorio = random.randint(1, 10)
adivinanza = int(input("Adivina el número entre 1 y 10: "))
if adivinanza == numero_aleatorio:
    print("¡Felicidades, acertaste!")
else:
    print(f"Intenta de nuevo. El número era {numero_aleatorio}.")

# calcular el signo zodiacal
dia = int(input("Introduce tu día de nacimiento: "))
mes = input("Introduce tu mes de nacimiento: ").lower()
if (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
    signo = "Aries"
elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
    signo = "Tauro"
elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20):
    signo = "Géminis"
elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22):
    signo = "Cáncer"
elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
    signo = "Leo"
elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22):
    signo = "Virgo"
elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22):
    signo = "Libra"
elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21):
    signo = "Escorpio"
elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21):
    signo = "Sagitario"
elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19):
    signo = "Capricornio"
elif (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18):
    signo = "Acuario"
elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20):
    signo = "Piscis"
else:
    signo = "Fecha no válida"
print(f"Tu signo es {signo}.")

# Sistema  de calificaciones 
calificacion = float(input("Introduce tu calificación: "))
if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif calificacion < 60:
    letra = "F"
else:
    letra = "Calificación no válida"

print(f"Tu calificación es {letra}.")

# Control de acceso 
usuario_correcto = "Geraldi"
contraseña_correcta = "1728"
intentos = 3
while intentos > 0:
    usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")
    
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print(f"Bienvenido, {usuario}.")
        break
    else:
        intentos -= 1
        print(f"Acceso denegado. Te quedan {intentos} intentos.")
else:
    print("Has sido bloqueado.")
