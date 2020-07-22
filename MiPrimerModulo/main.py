# main.py

from sys import path

path.append('C:\\Users\\halvarez\\Desktop\\Mi Estudio de Python\\MiPrimerModulo\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))