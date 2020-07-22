#5.1.6.4-2
# Escenario
# Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado.

# La función debe:

# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado.

def readint(min, max):
    while True:
        try:
            prompt = int(input ("Ingresa un numero de -10 a 10: "))
            assert prompt >= min and prompt <= max
            return prompt
        except ValueError:
            print("Error: entrada incorrecta")
        except AssertionError:
            print("Error: el valor no está dentro del rango")
#
v = readint(-10, 10)
print("El número es: ", v)

# if not isinstance(v, (int, float, long, complex) ):
#     raise TypeError, "i debe ser numérico"