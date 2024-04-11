
liste = [1, 2, 3 ,4,5,6,7]

resultat =  [{element} for element in liste]
longueur = len(liste)

def verifierPresence(ensemble):
    liste_de_listes = [[1,2]]
    liste_d_ensembles = [set(sous_liste) for sous_liste in liste_de_listes]
    for element in liste_d_ensembles:
        if len(ensemble.intersection(element)) > 1 :
            return False
    return True

for k in resultat:
    a = 0
    while True:
        tmp = [k]
        a = 0
        for i in tmp:
            for j in resultat:
                a= 0
                ensPartieJ = j - i
                nvEns = i.union(j)
                if i != j and nvEns not in tmp and ensPartieJ not in i :
                    ajouter = verifierPresence(nvEns)
                    if ajouter :
                        tmp.append(nvEns)
            a = 0
        a = 0
        if len(tmp) == 0: break
        resultat = tmp.copy()


# Afficher le résultat
print(resultat)