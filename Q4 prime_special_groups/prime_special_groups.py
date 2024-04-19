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

    # TODO : Compléter ici/Complete here...
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

   # primes = listPrimes(10 ** 4)
    answer = 0
    primes_100 = listPrimes(675)
    graphe = {2: set(), 3: {7, 137, 11, 271, 17, 541, 31, 673, 37, 557, 59, 191, 449, 67, 73, 331, 467, 607, 229, 613, 359, 617, 109, 499, 373}, 5: set(), 7: {97, 541, 547, 673, 229, 487, 523, 109, 433, 19, 283, 61, 127}, 11: {353, 503, 587, 239, 113, 23, 251}, 13: {577, 103, 331, 523, 367, 241, 337, 19, 61, 127}, 17: {257, 449, 389, 491, 239, 431, 83, 383}, 19: {97, 577, 163, 79, 433, 181, 571, 31}, 23: {89, 311, 509, 47}, 29: {167, 71, 137, 401, 179, 599, 569, 347, 383}, 31: {139, 181, 151}, 37: {67, 199, 79, 463, 277, 313, 607}, 41: {593, 257, 227}, 43: {97, 613, 103, 271, 499, 223}, 47: {419, 293, 521, 269, 149, 251}, 53: {353, 419, 197, 269, 653, 113, 401}, 59: {419, 197, 167}, 61: {487, 409, 331, 151}, 67: {547, 139, 619, 601, 157}, 71: {257, 389, 263, 233, 443, 317}, 73: {547, 643, 277, 571, 607}, 79: {193, 613, 397, 367, 241, 631}, 83: {449, 227, 563, 311, 443}, 89: {293, 137, 521, 107, 431, 443}, 97: {241, 373, 379, 157}, 101: {641, 197, 359, 107, 467, 149, 383}, 103: {307, 421}, 107: {449}, 109: {673, 199, 139, 661, 313}, 113: {131, 227, 167, 647, 233, 149, 383}, 127: {163, 331, 271, 241, 373, 601, 157, 607}, 131: {449, 641, 617, 479}, 137: {353, 197, 359, 491, 587, 239, 659, 191}, 139: {547, 457, 619, 367, 661}, 149: {563, 251, 173, 491}, 151: {163, 397, 433, 499, 631, 607}, 157: {229, 277, 571, 181}, 163: {193, 613, 367, 307, 409}, 167: {641, 521, 491, 269, 443}, 173: {293, 431, 659, 347, 191}, 179: {593, 317, 269, 383}, 181: {193, 421, 199, 619, 397, 499, 283, 607}, 191: {227, 461, 599, 281, 251}, 193: {577, 433, 373, 601, 283, 541}, 197: {569, 641, 347, 311}, 199: {379, 673, 211, 373}, 211: {271, 499, 373, 313, 283, 349, 571}, 223: {337, 277, 547, 229}, 227: {593, 281}, 229: {547, 613, 433, 499, 373, 631}, 233: {617, 347, 251, 239}, 239: {641, 263, 461, 347, 509}, 241: {601, 313, 421, 271}, 251: {347, 491, 431}, 257: {293, 263}, 263: {443, 293, 647}, 269: {389, 617, 461, 431, 317}, 271: {409}, 277: {331, 499}, 281: {557, 419, 509, 653}, 283: {487, 397, 463, 601, 541}, 293: {617, 467, 311}, 307: {577, 523, 631, 367}, 311: {653, 359}, 313: {619}, 317: {353, 419, 503}, 331: {577, 349}, 337: {349, 397, 607}, 347: {401, 443}, 349: {409, 499, 373}, 353: {443, 359}, 359: {563, 509, 599}, 367: {457, 613}, 373: {661}, 379: {397}, 383: {419}, 389: set(), 397: {673, 547}, 401: {593}, 409: set(), 419: {449, 443, 563, 599}, 421: {433, 643, 661, 607}, 431: {479}, 433: {571}, 439: {601, 613, 541, 661}, 443: set(), 449: {563, 557}, 457: {673, 643}, 461: {569, 653, 479}, 463: {523, 643, 613}, 467: {617, 641, 587}, 479: {593, 569, 599}, 487: {601}, 491: {593, 653}, 499: {673}, 503: {563, 653, 647}, 509: {647}, 521: {641, 659, 557}, 523: {577, 541}, 541: {571, 661}, 547: {577, 643, 661}, 557: set(), 563: {587}, 569: {659}, 571: set(), 577: {613}, 587: {617}, 593: {647}, 599: set(), 601: set(), 607: {619}, 613: {673, 661}, 617: {647}, 619: set(), 631: set(), 641: set(), 643: set(), 647: set(), 653: {659}, 659: set(), 661: set(), 673: set()}
    print(find_clique(graphe,primes_100,[]))


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
            print(prime,prime2)
            ens.add(prime2)
    return ens

def paireSpeciale(a,b):
    return combEstPrime(a,b) and combEstPrime(b,a)

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
        graphe[prime] = primPaires(primes,prime)
    return graphe

def find_clique(graphe,primes,result):
    """parcours DFS pour trouver 4 cliques"""
    for key in graphe:
        curr = graphe[key]
        for elem in curr:
            elemEns = primPaires(primes,elem)
            if len(elemEns & curr) >= 2:
                for elem3 in elemEns:
                    elem3Ens = primPaires(primes,elem3)
                    if len(elemEns & curr & elem3Ens) >= 1:
                        for elem4 in elem3Ens:
                            subResult = [key,elem,elem3,elem4]
                            result.append(subResult)
    print(result)


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
    tabA = [2,3,5,7,11]
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