# Herve Ng'isse (20204609)
# Qiwu Wen (20230961)

import sys

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
    input_file = args[0]
    output_file = args[1]

    matrice = []
    matrice = read_problem(matrice, input_file)

    def coordonneespuits(matrice):
        listeCoordonnees = set()
        nombreColonne = len(matrice[0])
        nombreLigne = len(matrice)
        for j in range(nombreLigne):
            for i in range(nombreColonne):
                if matrice[j][i] == 1:
                    listeCoordonnees.add((j, i))
        return listeCoordonnees

    def explorer_adjacents(cell, listeCoordonnees):
        visited = set()
        stack = [cell]

        while stack:
            j, i = stack.pop()
            if (j, i) in visited:
                continue
            visited.add((j, i))

            cellules_adjacentes = {(j - 1, i), (j + 1, i), (j, i - 1), (j, i + 1)}
            tmp = listeCoordonnees.intersection(cellules_adjacentes)
            stack.extend(tmp)
            listeCoordonnees -= tmp

        return visited

    listeCoordonnees = coordonneespuits(matrice)
    listeParcours = []

    while listeCoordonnees:
        element = listeCoordonnees.pop()
        visited = explorer_adjacents(element, listeCoordonnees)
        if visited:
            listeParcours.append(visited)

    a = 0
    answer = max(len(sous_ensemble) for sous_ensemble in listeParcours) if listeParcours else 0

    # answering
    write(output_file, str(answer))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])