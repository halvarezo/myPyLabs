# 5.1.9.18

# Escenario
# Ya sabes como funiona el método split(). Ahora queremos que lo pruebes.

# Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

# Debe aceptar únicamente un argumento: una cadena.
# Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
# Si la cadena está vacía, la función debería devolver una lista vacía.
# Su nombre debe ser misplit().
# Usa la plantilla en el editor. Prueba tu código con cuidado.

def misplit(strng):

    try:
        if type(strng) != str:
            raise TypeError
        lista=[]
        strng=strng.strip(" ")
        strng=strng + " "
        k=0
        for espacios in range(0, strng.count(" ")+1):
            j=strng.find(" ", k)
            lista.append(strng[k:j])
            # lista.remove('')
            k=j+1
        lista.remove('')
        return lista
    except TypeError:
        print("El argumento debe ser una cadena")
        return -1
    except:
        return -2


#print(misplit())
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))