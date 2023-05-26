#1
def saludar():
    print("¡Hola amiga!")

saludar()

#2
def saludar(nombre):
    print("¡Hola " + nombre + "!")

saludar("Pedro")

#3
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)
    return total

factura1 = calcular_total_factura(100)  # Se aplica el 21% de IVA por defecto
factura2 = calcular_total_factura(200, 10)  # Se aplica un 10% de IVA

print("Factura 1:", factura1)
print("Factura 2:", factura2)

#4
import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

# Ejemplo de uso
radio = 3
altura = 5

area = calcular_area_circulo(radio)
volumen = calcular_volumen_cilindro(radio, altura)

print("Área del círculo:", area)
print("Volumen del cilindro:", volumen)

#5
def calcular_cuadrados(muestra):
    cuadrados = []
    for numero in muestra:
        cuadrado = numero ** 2
        cuadrados.append(cuadrado)
    return cuadrados

muestra = [1, 2, 3, 4, 5]
cuadrados = calcular_cuadrados(muestra)
print("Cuadrados:", cuadrados)
