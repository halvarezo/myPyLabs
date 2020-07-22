#5.1.10.6

# Escenario
# Seguramente has visto un display de siete segmentos.
# Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. Si aún no sabes 
# lo qué es, consulta la siguiente liga en Wikipedia artículo.
# Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.
# Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

#   # ### ### # # ### ### ### ### ### ### 
#   #   #   # # # #   #     # # # # # # # 
#   # ### ### ### ### ###   # ### ### # # 
#   # #     #   #   # # #   # # #   # # # 
#   # ### ###   # ### ###   # ### ### ###

# Nota: el número 8 muestra todas las luces LED encendidas.
# Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.
# Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.

def convertir(strng):
    try:
        if strng.isdigit():
            lista=list(strng)

        else:
            raise TypeError
            
    except:
        print("No es el tipo")

#   # ### ### # # ### ### ### ### ### ### 
#   #   #   # # # #   #     # # # # # # # 
#   # ### ### ### ### ###   # ### ### # # 
#   # #     #   #   # # #   # # #   # # # 
#   # ### ###   # ### ###   # ### ### ###
   
numeros=['''#
#
# 
# 
# ''', '''###
  #
###
#
###''']

print(numeros)



strng=str(input("Digite un número para ser mostrado en el display: "))
convertir(strng)