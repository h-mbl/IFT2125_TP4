# Nom, Matricule
# Nom, Matricule

import sys
global m,n

def read_problem(MyGraph, input_file="input.txt"):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    # TODO: Compléter ici/Complete here
    # traiter les lignes du fichier pour le problème
    # process the file lines for the problem
    premiereLigne = True
    for ligne in lines:
        if premiereLigne:
            premiereLigne = False
            ligne = ligne.strip()
            m = ligne[0]
            n = ligne[2]
            continue
        ligne_entiers = []  # Initialiser une liste vide pour les entiers de cette ligne
        ligne = ligne.strip()
        nombres = [int(caractere) for caractere in ligne] # Séparer la ligne en nombres, en se basant sur la virgule

        # Convertir chaque nombre en entier et l'ajouter à la liste des entiers de la ligne
        for nombre in nombres:
            entier = int(nombre)  # Conversion de la chaîne en entier
            ligne_entiers.append(entier)  # Ajout de l'entier à la liste de la ligne

        # Ajout de la liste des entiers de cette ligne à la matrice
        MyGraph.append(ligne_entiers)

    return MyGraph
    


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    matrice = []

    # TODO : Compléter ici/Complete here...
    matrice = read_problem(matrice,input_file)


    def coordonneespuits(matrice):
        coordonneespuits = {}
        listeCoordonnees = []
        # je dois creer un cadre
        nombreColonne = len(matrice[0])
        nombreLigne = len(matrice)
        for j in range(nombreLigne):
            for i in range(nombreColonne):
                if matrice[j][i] == 1:
                    coordonneespuits[(j, i)] = 0
                    listeCoordonnees.append((j,i))
        return coordonneespuits, listeCoordonnees

    def explorer_adjacents(cell, coordonneespuits, listeCoordonnees, visited):

        # Vérifiez si la cellule est dans listeCoordonnees et sa valeur est 1
        if cell in listeCoordonnees and coordonneespuits[cell] == 0:
            visited.append(cell)
            # Changez la valeur de la cellule dans coordonneespuits
            coordonneespuits[cell] = 1 # Remplacez nouvelle_valeur par la valeur que vous souhaitez
                # Déterminez les cellules adjacentes
            # Supposons que cell est un tuple (x, y)
            j, i = cell
            cellules_adjacentes = [(j - 1, i), (j + 1, i), (j, i - 1), (j, i + 1)]

            # Pour chaque cellule adjacente, répétez le processus
            for adj in cellules_adjacentes:
                explorer_adjacents(adj, coordonneespuits, listeCoordonnees, visited)

    coordonneespuits,listeCoordonnees = coordonneespuits(matrice)
    listeParcours  =[]
    # Augmenter la limite de profondeur de récursion
    sys.setrecursionlimit(1000000)
    for element in listeCoordonnees :
        # donc on a deja visite la coordonnee
        if coordonneespuits[element] == 1:
            continue
        else :
            visited = []
            explorer_adjacents(element,coordonneespuits,listeCoordonnees,visited)
        listeParcours.append(visited)
    try :
        answer = max(len(sous_liste) for sous_liste in listeParcours)
    except :
        answer = 0

    # answering
    write(output_file, str(answer))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])