# 3.1.4.6 

# Escenario
# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.

# Tu tarea es:

# Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (paso 1).
# Escribir una línea de código que elimine el último elemento de la lista (paso 2).
# Escribir una línea de código que imprima la longitud de la lista existente (paso 3).

listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.

listaSombrero[int(round(len(listaSombrero)/2))]=int(input("Digite un número para reemplazar el del medio: "))
print("La lista con el número del medio cambiado es: ", listaSombrero)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

del listaSombrero[len(listaSombrero)-1]
print("La lista sin el último número es: ", listaSombrero)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la nueva lista es: ", len(listaSombrero))
print(listaSombrero)