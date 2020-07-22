#3.1.2.10
# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Digite una palabra: ")
userWord = userWord.upper()
vocales = {"A","E","I","O","U"}

for letter in userWord:
    # Complete the body of the for loop.
    imprimir = True
    for i in vocales:
        if letter == i:
            imprimir = False
            break
    if imprimir == False:
        continue
    else:
        print(letter)   


        

 
    


    
    
