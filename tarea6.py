#1
palabra = input("Escriba una palabra: ")
for i in range(10):
    print(palabra)

#2
edad = float(input("Ingresa tu edad: "))
num = 0
while num < edad:
    num += 1
    print(num)

#3
numero = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if numero <= 0:
    print("El número debe ser positivo.")
else:
    impares = []
    for i in range(1, numero + 1, 2):
        impares.append(str(i))

    resultado = ", ".join(impares)
    print("Números impares: " + resultado)

#4
numero = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if numero <= 0:
    print("El número debe ser positivo.")
else:
    cuenta_regresiva = []
    for i in range(numero, -1, -1):
        cuenta_regresiva.append(str(i))

    resultado = ", ".join(cuenta_regresiva)
    print("Cuenta regresiva: " + resultado)

#5
contraseña = "contraseña"  # Contraseña correcta

while True:
    intento = input("Introduce la contraseña: ")
    if intento == contraseña:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Vuelve a intentarlo.")

#6
while True:
    entrada = input("Introduce algo (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
    else:
        print(entrada)