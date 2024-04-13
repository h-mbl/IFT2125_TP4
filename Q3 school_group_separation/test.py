
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


a = 0
general = []
for k in resultat:
        a = 0
        ligne = 1
   # while True:
        tmp = [k]
        i = 0
        k = ligne
        add = 0
       # while i < len(tmp):
        while ligne < len(resultat) -1 and len(tmp)>0 :
            elementI = tmp[i]
            tmp.remove(elementI)
            tmp_branche = []
            for j in range(k,len(resultat)):
                a= 0
                elementJ = resultat[j]
                ensPartieJ = elementJ - elementI
                nvEns = elementI.union(elementJ)
                tmp_branche.append(nvEns)
                add += 1
                a = 0
            general.extend(tmp_branche)
            a = 0
            #add += 1
            if len(tmp) == 0 and ligne < len(resultat)-1:
                if len(tmp) == 0 and len(tmp_branche) == 0:
                    tmp = general.copy()
                    tmp = tmp[len(tmp) - add:]
                    add = 0
                    ligne += 1
                    k = ligne
                else:
                    tmp = tmp_branche.copy()
                    ligne += 1
                    k = ligne
                    add = 0
            elif len(tmp) > 0 and ligne < len(resultat)-1 :
                k = ligne + 1
            else :
                k += 1
                i = 0
            #k += 1
        a = 0
        #if len(tmp) == 0: break
        #resultat = tmp.copy()


# Afficher le résultat
print(resultat)

"""
tmp_graphe = []
tmp_ligne = resultat
#premiere ligne :
if True :
    tmp = []
    for i in range(len(tmp_ligne)):
        tmp_branche = []
        for j in range(i + 1, len(resultat)):
            elementI = resultat[i]
            elementJ = resultat[j]
            tmp_branche.append(elementI + elementJ[len(elementJ) - 1:])
        a = 0
        tmp.append(tmp_branche)
    a = 0
    tmp_ligne = tmp.copy()
    tmp_graphe.append(tmp_ligne)
"""

