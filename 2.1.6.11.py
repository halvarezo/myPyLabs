# 2.1.6.11

# Escenario
# La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. 
# Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado debe ser mostrado en la consola.
# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
# No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta 
# acorde a la entrada dada.
# Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

hora=25
while hora > 24 or hora < 0:
    hora = int(input("Hora de inicio (horas): "))
minutos=61
while minutos < 0 or minutos > 60:
    minutos = int(input("Minuto de inicio (minutos): "))
dura = -1
while dura < 0:
    dura = int(input("Duración del evento (minutos): "))

hora=hora + dura//60
minutos=minutos+dura%60

print("El tiempo final es: ")
print (hora, ":" , minutos)


