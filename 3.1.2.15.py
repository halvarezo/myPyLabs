#3.1.2.15
# Problema:
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

c0 = 0
while c0 <= 0:
    c0 = int(round(float(input("Digite un numero entero distinto de 0: "))))

pasos = 0
while c0 != 1:
    pasos += 1
    if c0 ==1:
        break
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3*c0 + 1
    print(int(c0))
print("Los pasos fueron", pasos)



