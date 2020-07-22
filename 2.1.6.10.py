# 2.1.6.10

# Escenario
# La tarea es completar el código para poder evaluar la siguiente expresión: 1/((x+1/(x+1/(x+1/x))))

# El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios.
# Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario). Prueba tu código cuidadosamente.
# Datos de Prueba
# Entrada de muestra: 1 # Salida esperada: y = 0.6000000000000001
# Entrada de muestra: 10 # Salida esperada: y = 0.09901951266867294
# Entrada de muestra: 100 # Salida esperada: y = 0.009999000199950014
# Entrada de muestra: -5 # Salida esperada: y = -0.19258202567760344

x=0
while x==0:
    x=float(input("Digite el valor de x, distinto de 0: "))

y= 1/(x+1/(x+1/(x+1/x)))
print("El valor final es: ", y)

