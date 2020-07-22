# 2.1.4.7 
# Escenario
# A continuación una historia:

# Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

# Tu tarea es:

# Crear las variables: juan, maria, y adan.
# Asignar valores a las variables. El valor debe de ser igual al numero de manzanas que cada quien tenía.
# Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
# Después se debe crear una nueva variable llamada totalManzanas y se debe igualar a la suma de las tres variables anteriores.
# Imprime el valor almacenado en totalManzanas en la consola.
# Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Numero Total de Manzanas:" y totalManzanas.

juan = 3
maria = 5
adan = 6
totalManzanas = juan + maria + adan
print("juan= " + str(juan), "maria= " + str(maria), "adan= " + str(adan), sep=",")
print("Total Manzanas= ", totalManzanas)
print("Total Manzanas de otra forma= ", juan+maria+adan)
