
__version__ = "0.1.0"
__author__ = "CirilloSantos"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)    
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-*-*-*-*-*-*-*-*-*-*")    