# Herve Ng'isse (20204609)
# Qiwu Wen (20230961)

import sys
from collections import defaultdict


# Fonction pour lire le fichier d'input. Vous ne deviez pas avoir besoin de la modifier.
# Retourne la liste des noms d'étudiants (students) et la liste des paires qui ne peuvent
# doivent pas être mis dans le même groupe (pairs)
#
# Function to read the input file. You shouldn't have to modify it.
# Returns the list of student names (students) and the list of pairs of students that
# shouldn't be put in the same group (pairs)
def read(fileName):
    # lecture du fichier
    fileIn = open(fileName, "r")
    linesIn = fileIn.readlines()
    fileIn.close()

    nbStudents = int(linesIn[0])
    students = []
    if (nbStudents != 0):
        students = [s.strip() for s in linesIn[1:nbStudents + 1]]
    nbPairs = int(linesIn[nbStudents + 1])
    pairs = []
    if (nbPairs != 0):
        pairs = [s.strip().split() for s in linesIn[nbStudents + 2:nbStudents + nbPairs + 2]]

    return students, pairs


# Fonction qui écrit dans le fichier d'output.
# le paramètre content est un string
#
# Function that writes in the output file.
# The content parameter is a string
def write(fileName, content):
    Outputfile = open(fileName, "w")
    Outputfile.write(content)
    Outputfile.close()


def createGroups(students, pairs):

    tmp_student = set(students)
    pairs = [set(sous_liste) for sous_liste in pairs]

    ensemble1 = set()
    ensemble2 = set()

    def ensemble(element,elementEnsemble,position):
        if len(elementEnsemble.intersection(ensemble1)) == 0 and position == 1:
            ensemble1.add(element)
        elif len(elementEnsemble.intersection(ensemble2)) == 0 and position == 2:
            ensemble2.add(element)
        else :
            return 0

    def placerDansTableau(element, position):
        if position == 1:
            position = 2
        else:
            position = 1
        for x in element:
            if cas[x][2] == 0:
                cas[x][2] = position

    def build_dangerous_pairs_dict():
        cas = defaultdict(lambda: [set(), 0, 0])
        for pair in pairs:
            student1, student2 = pair
            cas[student1][0].add(student2)
            cas[student2][0].add(student1)
        return cas

    # construire le dictionnaire des elements non-adjcents
    cas = build_dangerous_pairs_dict()

    if len(cas) == 0 : return "impossible"

    #choisir un element pour commencer
    tmp = students[0]

    # liste des elements qui ne peuvent pas etre dans un meme groupe que l'element choisit
    elementParcourir = cas[tmp][0].copy()

    # position , visite = 1
    cas[tmp][2] = 1
    cas[tmp][1] = 1

    # enlever l'element dans la liste des elements et dans le dictionnaire des elemennts non-adjcents
    tmp_student.discard(tmp)
    cas.pop(tmp)

    # placer l'elements dans l'ensemble
    ensemble(tmp,elementParcourir,1)

    # definir la position des ses elements dangereux
    placerDansTableau(elementParcourir,1)

    def traiter_element(element, elementParcourir, position=None):
        # definir la position
        cas[element][1] = 1
        if position is None:
            position = cas[element][2]
        else:
            cas[element][2] = position

        # enregistrer la liste des elements qui ne peuvent pas etre dans un meme groupe que l'element choisit
        tmp_elementParcourir = cas[element][0].copy()

        # enlever l'element dans la liste des elements et dans le dictionnaire des elemennts non-adjcents
        tmp_student.discard(element)
        cas.pop(element)

        # place l'element dans l'ensemble
        retour = ensemble(element, tmp_elementParcourir, position)

        # si l'element ne peut pas etre placer retourner None
        if retour is not None:
            return None

        # trouver l'element dans la liste des etudiant qui n'a pas encore ete parcourit
        delete = tmp_elementParcourir - tmp_student
        tmp_elementParcourir = tmp_elementParcourir - delete

        # on defini alors la position des elements et on le place dans la liste principale de l'iteration
        placerDansTableau(tmp_elementParcourir, position)
        elementParcourir = elementParcourir.union(tmp_elementParcourir)

        return elementParcourir

    while len(elementParcourir) > 0 or len(tmp_student) > 0:
        if len(elementParcourir) > 0 :
            # choisir un element pour commencer
            tmp = elementParcourir.pop()
            elementParcourir = traiter_element(tmp, elementParcourir)

        # si les pairs dangereux ne sont pas connexe
        # on applique que precedement
        elif len(tmp_student) > 0:
            tmp = tmp_student.pop()
            position = cas[tmp][2]
            if position == 0:
                cas[tmp][2] = 1
                position =  1
            elementParcourir  = traiter_element(tmp, elementParcourir, position)
        if elementParcourir is None:
            return "impossible"

    return ' '.join(ensemble1) + '\n' + ' '.join(ensemble2)

# Normalement, vous ne devriez pas avoir à modifier
# Normaly, you shouldn't need to modify
def main(args):
    input_file = args[0]
    output_file = args[1]
    students, pairs = read(input_file)
    output = createGroups(students, pairs)
    write(output_file, output)


# Ne pas changer
# Don't change
if __name__ == '__main__':
    main(sys.argv[1:])