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


    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

   # primes = listPrimes(10 ** 4)
    answer = 0
    primes_100 = listPrimes(10000)
    # TODO : Determiner la limite pour faire passer les tests

    graphe = graphe_initialisation(primes_100)
    print(graphe)
    cliques = find_clique(graphe,[])
    print(cliques)
    result = []
    for clique in cliques:
        somme = 0
        for elem in clique:
            somme += elem
        result.append(somme)
    result.sort()
    print(result)
    answer = result[n-1]
    print(len(answer))

    print(answer)

    # answering
    write(output_file, str(answer))


def primPaires(primes, prime):
    """fonction qui retourne les primes specials d'un prime donne"""
    ens = set()
    i = primes.index(prime)
    primeGrand = primes[i+1:]
    for prime2 in primeGrand:
        if paireSpeciale(prime2,prime):
            ens.add(prime2)
    return ens

#la cache des paire speciales
special_pairs_cache = {}

def paireSpeciale(a,b):
    #return combEstPrime(a,b) and combEstPrime(b,a)
    if (a, b) in special_pairs_cache:
        return special_pairs_cache[(a, b)]
    result = combEstPrime(a, b) and combEstPrime(b, a)
    special_pairs_cache[(a, b)] = result
    special_pairs_cache[(b, a)] = result
    return result

def listPrimes(limite):
    primes = []
    for num in range(2, limite):
        if not millerRabinPrim(num):
            continue
        else: primes.append(num)
    return primes
def graphe_initialisation(primes):
    graphe = dict()
    for prime in primes:
        print(len(primes), primes.index(prime))
        graphe[prime] = primPaires(primes,prime)
    return graphe

def find_clique(graphe,result):
    """parcours DFS pour trouver 4 cliques"""
    for key in graphe:
        print(len(graphe),list(graphe.keys()).index(key))
        curr = graphe[key]
        for elem in curr:
            elemEns = graphe[elem]
            if len(elemEns & curr) >= 2:
                for elem3 in elemEns:
                    elem3Ens = graphe[elem3]
                    if len(elemEns & curr & elem3Ens) >= 1:
                        print(elem3Ens,1333)
                        for elem4 in elem3Ens:
                            if estEnsSpecial(key,elem,elem3,elem4):

                                subResult = [key,elem,elem3,elem4]


                                result.append(subResult)


    return result

def estEnsSpecial(a,b,c,d):
    tab = [a,b,c,d]
    for i in range(len(tab)):
        for j in range(i + 1, len(tab)):
            if not paireSpeciale(tab[i], tab[j]):
                return False
    return True
def combinerInts(a , b):

    return int(str(a) + str(b))

def combEstPrime(a,b):
    return millerRabinPrim(combinerInts(a,b))

def bTest(a, n):
    s = 0
    t = n - 1
    while(t % 2 == 1):
        s += 1
        t = t//2


    x = pow(a,t) % n


    if x == 1 or x == n - 1:
        return True

    for i in range(1,s):

        x = pow(x,2) % n
        if x == n - 1:
            return True
    return False

def millerRabinPrim(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    tabA = [2,3,5,7]
    if n < 10**24:
        for a in tabA:
            if a > n-2: continue
            if not bTest(a, n):
                return False #algo faux-biaise
        return True
    a = random.randint(2,n-2)
    return bTest(a, n)


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])