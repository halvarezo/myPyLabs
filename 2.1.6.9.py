# 2.1.6.9

# Escenario
# La tarea es completar el código para evaluar y mostrar el resultado de cuatro operaciones aritméticas básicas.

# El resultado debe ser mostrado en consola.

# Quizá no podrás proteger el código de un usuario que intente dividir entre cero. Por ahora, no hay que preocuparse por ello.

# Prueba tu código - ¿Produce los resultados esperados?

# ingresa un valor flotante para la variable a aquí
a=float(input("Ingresa un valor flotante para la variable a aquí: "))

# ingresa un valor flotante para la variable b aquí
b=0
while b == 0:
    b=float(input("Ingresa un valor flotante para la variable b aquí distinto de 0: "))


# muestra el resultado de la suma aquí 
print(a+b)
# muestra el resultado de la resta aquí
print(a-b)
# muestra el resultado de la multiplicación aquí
print(a*b)
# muestra el resultado de la división aquí
print(a/b)

print("\n¡Eso es todo, amigos!")