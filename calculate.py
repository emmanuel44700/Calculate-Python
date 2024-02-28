def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division par zéro impossible"

def calculatrice():
    print("Bienvenue dans la calculatrice Python !")
    print("Choisissez une opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Entrez votre choix (1/2/3/4): ")

    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))

    if choix == '1':
        print("Résultat:", addition(num1, num2))
    elif choix == '2':
        print("Résultat:", soustraction(num1, num2))
    elif choix == '3':
        print("Résultat:", multiplication(num1, num2))
    elif choix == '4':
        print("Résultat:", division(num1, num2))
    else:
        print("Choix invalide")

calculatrice()
