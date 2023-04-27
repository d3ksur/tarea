#1
num1 = int(input("Introduzca el primer número entero: "))
num2 = int(input("Introduzca el segundo número entero: "))

if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Los números son iguales")

#2
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
num3 = float(input("Introduzca el tercer número: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Dos de los números son iguales.")
else:
    print("Los tres números son distintos.")

#3
edad = int(input("¿Cuál es tu edad? "))

if edad < 18:
    print("Lo siento, eres menor de edad y no puedes acceder a la fiesta.")
else:
    print("Bienvenido/a a la fiesta de BigBayData.com. ¡Disfruta de la noche!")

#4
a = float(input("Introduzca el primer número: "))
b = float(input("Introduzca el segundo número: "))

print("Seleccione una operación: ")
print("1 - Suma")
print("2 - Multiplicación")
print("3 - Resta")
print("4 - División")

operacion = int(input("Introduzca el número correspondiente a la operación que desea realizar: "))

if operacion == 1:
    resultado = a + b
    print("El resultado de la suma de", a, "y", b, "es:", resultado)
elif operacion == 2:
    resultado = a * b
    print("El resultado de la multiplicación de", a, "y", b, "es:", resultado)
elif operacion == 3:
    resultado = a - b
    print("El resultado de la resta de", a, "y", b, "es:", resultado)
elif operacion == 4:
    resultado = a / b
    print("El resultado de la división de", a, "y", b, "es:", resultado)
else:
    print("La opción seleccionada no es válida.")

#5
precio_final_de_compra = float(input("Introduzca el precio final de compra: "))
puntos = int(input("Introduzca la cantidad de puntos del cliente: "))

if puntos < 100:
    descuento = precio_final_de_compra * 0.1
elif puntos < 150:
    descuento = precio_final_de_compra * 0.12
elif puntos < 200:
    descuento = precio_final_de_compra * 0.15
else:
    descuento = precio_final_de_compra * 0.2

precio_con_descuento = precio_final_de_compra - descuento

print("El precio final de compra es:", precio_final_de_compra)
print("El descuento aplicado es:", descuento)
print("El precio con descuento es:", precio_con_descuento)

#6
precio_factura = float(input("Introduzca el precio de la factura: "))
es_restaurante = input("¿Es una factura de un restaurante? (Sí/No): ")

if es_restaurante == "Sí":
    iva = 0.1
else:
    iva = 0.21

precio_final = precio_factura * (1 + iva)

print("El precio final con IVA aplicado es:", precio_final)

#7
password = "contraseña123"

entrada = input("Introduzca la contraseña: ")

if entrada == password:
    print("Bienvenid@...")
else:
    print("Ordenador bloqueado. Contraseña incorrecta.")

#8
tarifa_anual = 500
edad = int(input("Introduzca su edad: "))
trabajando = input("¿Está trabajando? (Sí/No): ")

if trabajando == "Sí":
    if edad >= 18:
        precio = tarifa_anual
    else:
        precio = tarifa_anual * 0.95
else:
    if edad >= 18:
        precio = tarifa_anual * 0.75
    else:
        precio = tarifa_anual * 0.5

print("El precio de la tarifa es:", precio)

#9
dia = input("Introduce un día de la semana: ")

if dia == "lunes":
    print("¡Feliz comienzo de semana!")
elif dia == "viernes":
    print("¡Por fin llegó el viernes!")
elif dia == "sábado" or dia == "domingo":
    print("¡Buen fin de semana!")
else:
    print("Ese día no es válido.")

#10
num = int(input("Ingresa un número entero: "))

if num >= 0:
    print("El valor absoluto de", num, "es", num)
else:
    abs_num = -num
    print("El valor absoluto de", num, "es", abs_num)

#11
candidato = input("¿Por quién desea votar? (A: Partido Rojo, B: Partido Verde, C: Partido Azul): ")

if candidato == "A":
    print("Usted ha votado por el Partido Rojo")
elif candidato == "B":
    print("Usted ha votado por el Partido Verde")
elif candidato == "C":
    print("Usted ha votado por el Partido Azul")
else:
    print("Opción errónea")

#12
letra = input("Ingresa una letra: ")
if len(letra) == 1:
    if letra.lower() in "aeiou":
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar el dato")
