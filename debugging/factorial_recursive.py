#!/usr/bin/env python3
import sys

def factorial(n):
    """
    Function description:
    Calcule le factoriel d'un nombre entier n de manière récursive.

    Parameters:
    n (int): Un nombre entier non négatif dont on souhaite calculer le factoriel.

    Returns:
    int: Le factoriel de n, qui est le produit de tous les entiers positifs jusqu'à n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)