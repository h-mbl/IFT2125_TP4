
liste = [1, 2, 3 ,4]

resultat =  [set(element) for element in liste]
longueur = len(liste)

def verifierPresence(ensemble):
    liste_de_listes = [[1,2]]
    liste_d_ensembles = [set(sous_liste) for sous_liste in liste_de_listes]
    for element in liste_d_ensembles:
        if len(ensemble.intersection(element)) > 1 :
            return False
    return True


while True:
    tmp = []
    for i in resultat:
        for j in resultat:
            ensI = set(i)
            ensJ = set(j)
            ensPartieJ = ensJ - ensI
            if ensI != ensJ and i + j[len(j)-1:] not in tmp and ensPartieJ not in ensI and len(i + j[len(j)-1:]) == len(set(i + j[len(j)-1:])):
                ajouter = verifierPresence(set(i + j[len(j)-1:]))
                if ajouter :
                    tmp.append(i + j[len(j)-1:] )
    if len(tmp) == 0: break
    resultat = tmp.copy()


# Afficher le résultat
print(resultat)