#1
nombre = input("Ingresa tu nombre: ")
print("Ahora estás en la matrix, " + nombre)

#2
numero_decimal = float(input("Ingresa un número con decimales: "))
numero_entero = int(input("Ingresa un número entero: "))
suma = numero_decimal + numero_entero
print("El resultado de la suma es", suma)

#3
# Pedimos al usuario que ingrese los dos primeros números
numero_1 = float(input("Ingresa un primer número: "))
numero_2 = float(input("Ingresa un segundo número: "))

# Realizamos la suma de los dos números y la almacenamos en una variable
suma = numero_1 + numero_2

# Mostramos el resultado de la suma en pantalla
print("La suma de los dos números es:", suma)

# Pedimos al usuario que ingrese un tercer número
numero_3 = float(input("Ingresa un tercer número: "))

# Realizamos la multiplicación del tercer número por la suma de los dos primeros y la almacenamos en una variable
resultado = numero_3 * suma

# Mostramos el resultado de la multiplicación en pantalla
print("El resultado de la multiplicación es:", resultado)

#4
# Pedimos al usuario que ingrese los kilómetros recorridos y la cantidad de litros de combustible consumidos
kilometros_recorridos = float(input("Ingresa la cantidad de kilómetros recorridos por la motocicleta: "))
litros_combustible = float(input("Ingresa la cantidad de litros de combustible consumidos por la motocicleta: "))

# Calculamos el consumo de combustible por kilómetro y lo almacenamos en una variable
consumo_combustible = litros_combustible / kilometros_recorridos

# Mostramos el resultado del consumo de combustible por kilómetro en pantalla
print("El consumo de combustible por kilómetro es:", consumo_combustible)

#5
# Pedimos al usuario que ingrese la temperatura en Fahrenheit
fahrenheit = float(input("Ingrese una temperatura en grados Fahrenheit: "))

# Convertimos la temperatura a grados Celsius utilizando la fórmula de conversión
celsius = (5/9) * (fahrenheit - 32)

# Mostramos el resultado de la conversión en pantalla
print("La temperatura en grados Celsius es:", celsius)

#6
# Pedimos al usuario que ingrese tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calculamos el promedio de los tres números
promedio = (numero1 + numero2 + numero3) / 3

# Mostramos el resultado del promedio en pantalla
print("El promedio de los tres números es:", promedio)

#7
# Pedimos al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Restamos el 15% al número ingresado
resultado = numero - (numero * 0.15)

# Mostramos el resultado final en pantalla
print("El resultado de restarle el 15% al número ingresado es:", resultado)

#8
# Pedimos al usuario que ingrese dos palabras
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Concatenamos las dos palabras con un espacio entre ellas
concatenacion = palabra1 + " " + palabra2

# Mostramos el resultado de la concatenación en pantalla
print("La concatenación de las dos palabras es:", concatenacion)

#9
# Pedimos al usuario que ingrese un texto
texto = input("Ingrese un texto: ")

# Mostramos en pantalla la primera letra del texto
print("La primera letra del texto es:", texto[0])

# Solicitamos al usuario que ingrese un número menor a la cantidad de caracteres del texto
indice = int(input("Ingrese un número entre 0 y " + str(len(texto)-1) + ": "))

# Mostramos en pantalla el carácter del texto ubicado en la posición dada por el número ingresado
print("El carácter en la posición", indice, "es:", texto[indice])

#10
cantidad_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))
ha_visto_mas_de_3 = cantidad_shows > 3
print("Has visto más de 3 shows: ", ha_visto_mas_de_3)

#11
fecha = int(input("Ingrese una fecha en formato DDMMAAAA: "))
dia = fecha // 1000000
mes = (fecha // 10000) % 100
anio = fecha % 10000
print("La fecha ingresada es:", "{:02d} / {:02d} / {:04d}".format(dia, mes, anio))

#12
# Solicitar al usuario el ingreso de un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si el número es par o no
if numero % 2 == 0:
    es_par = True
else:
    es_par = False

# Imprimir el valor de verdad
if es_par:
    print("El número es par.")
else:
    print("El número es impar.")

#13
cadena = input("Ingrese una cadena de texto: ")
cantidad_caracteres = len(cadena)
es_par = cantidad_caracteres % 2 == 0
print(es_par)

#14
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if len(palabra1) < len(palabra2):
  print(True)
else:
  print(False)

#15
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print(True)
else:
    print(False)
