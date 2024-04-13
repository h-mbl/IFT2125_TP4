liste = [1, 2, 3 ,4,5,6]

resultat =  [{element} for element in liste]
longueur = len(liste)

def verifierPresence(ensemble):
    liste_de_listes = []
    liste_d_ensembles = [set(sous_liste) for sous_liste in liste_de_listes]
    for element in liste_d_ensembles:
        if len(ensemble.intersection(element)) > 1 :
            return False
    return True
def combinaison(elementI):
    combinaison = []
    for j in resultat:
        ensPartieJ = j - elementI
        nvEns = elementI.union(j)
        if len(nvEns) > 1 and nvEns not in general:
            ajouter = verifierPresence(nvEns)
            if ajouter : combinaison.append(nvEns)
    return combinaison
general = []
temporaire = resultat.copy()
ligne = 1
i = 0
while len(temporaire[0]) < len(resultat)-1 :
    tmp = combinaison(temporaire[0])
    temporaire.extend(tmp)
    general.extend(tmp)
    temporaire.pop(0)

print(general)