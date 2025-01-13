import sys

def factorial(n):
    if n < 0:
        return "Erreur : le factoriel n'est pas défini pour les nombres négatifs."
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n à chaque itération
    return result

if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <nombre>")
else:
    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide.")