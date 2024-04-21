#Nom, Matricule
#Nom, Matricule

import math
import random
import sys

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    n = int(args[0])
    output_file = args[1]

    limite = 10 ** 4
    primes = listPrimes(limite)
    graphe = construireGraphe(primes)
    cliques = trouverCliques(graphe)
    sommes = [sum(clique) for clique in cliques]
    sommes.sort()
    a = 100
    multiples_de_3 = [3 * i for i in range(1,a)]
    multiples_de_3 = [1,0] + multiples_de_3
    # Filtrer les éléments avec des indices divisibles par 2
    multiples_paires = [multiples_de_3[i] for i in range(len(multiples_de_3)) if i % 2 == 0]
    position =  multiples_paires[n-1] -1
    a = 0
    answer = sommes[position]
    write(output_file, str(answer))


def construireGraphe(primes):
    graphe = {p: set() for p in primes}
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p, q = primes[i], primes[j]
            if paireSpeciale(p, q):
                graphe[p].add(q)
                graphe[q].add(p)
    return graphe


def trouverCliques(graphe):
    cliques = []
    for p, curr in graphe.items():
        for q in curr:
            for r in curr:
                if r > q and r in graphe[q]:
                    for s in curr:
                        if s > r and s in graphe[q] and s in graphe[r]:
                            if estEnsSpecial(p, q, r, s):
                                clique = tuple(sorted([p, q, r, s]))
                                if clique not in cliques:
                                    cliques.append(clique)
    return cliques

def estEnsSpecial(p, q, r, s):
    return all(paireSpeciale(a, b) for a, b in [(p, q), (p, r), (p, s), (q, r), (q, s), (r, s)])


def paireSpeciale(p, q):
    return millerRabinPrim(int(str(p) + str(q))) and millerRabinPrim(int(str(q) + str(p)))


def listPrimes(limite):
    primes = []
    for num in range(2, limite):
        if millerRabinPrim(num):
            primes.append(num)
    return primes


def millerRabinPrim(n, k=20):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])