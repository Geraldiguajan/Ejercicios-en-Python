# Descuento en una tienda
monto = float(input("Introduce el monto total de la compra: $"))
if monto > 100:
    monto_final = monto * 0.8  # Aplicar un descuento del 20%
else:
    monto_final = monto
print(f"Monto final: ${monto_final:.2f}")

# Edad para votar
edad = int(input("\nIntroduce tu edad: "))
if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")

# Mayor de tres números
num1 = float(input("\nIntroduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
mayor = max(num1, num2, num3)
print(f"El número mayor es {mayor}.")

# Clasificar la edad del usuario
edad = int(input("\nIntroduce tu edad nuevamente para clasificarla: "))
if 0 <= edad <= 12:
    print("Eres niño.")
elif 13 <= edad <= 17:
    print("Eres adolescente.")
elif edad >= 18:
    print("Eres adulto.")
else:
    print("Edad no válida.")