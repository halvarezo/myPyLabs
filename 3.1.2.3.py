#3.1.2.3
secret_number = 777

numero = int(input("Digite el numero secreto: "))

while numero != secret_number:
    print(
        """
        +================================+
        | Welcome to my game, muggle!    |
        | Enter an integer number        |
        | and guess what number I've     |
        | picked for you.                |
        | So, what is the secret number? |
        +================================+
    """)
    numero = int(input("Digite el numero secreto: "))
print ("777, ¡lo hiciste Muggle!")