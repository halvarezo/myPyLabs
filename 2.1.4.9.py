# 2.1.4.9

# Escenario
# Millas y kilómetros son unidades de longitud o distancia.

# Teniendo en mente que 1 equivale aproximadamente a 1.61 kilómetros, complemente el programa en el editor para que convierta de:

# Millas a kilómetros.
# Kilómetros a millas.
# No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con los datos que han sido provistos en el código fuente.

distancia = float(input("Digite la distancia a convertir en mi o km= "))

while True:
    unidades = input ("Digite las unidades (mi o km): ")
    if unidades == "km":
        distancia=distancia/1.61
        print("La distancia en km es: ", distancia)
        break
    if unidades == "mi":
        distancia=distancia*1.61
        print("La distancia en km es: ", distancia)
        break



    