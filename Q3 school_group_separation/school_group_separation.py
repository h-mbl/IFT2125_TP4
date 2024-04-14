# Nom, matricule
# Nom, matricule

import sys


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
    with open(fileName, "w") as outputFile:
        for ensemble in content:
            ligne = ' '.join(sorted(ensemble))
            outputFile.write(ligne + "\n")



def createGroups(students, pairs):

    tmp_student = set(students)
    pairs = [set(sous_liste) for sous_liste in pairs]

    ensemble1 = set()
    ensemble2 = set()

    cas = {}

    def ensemble(element,position):
        if len(cas[element][0].intersection(ensemble1)) == 0 and position == 1:
            ensemble1.add(element)
        elif len(cas[element][0].intersection(ensemble2)) == 0 and position == 2:
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

    def creationDictionnaire():
        for element in students:
            tmp = set()
            for ensemble in pairs:
                if len(ensemble.intersection({element})) > 0:
                    reponse = ensemble - {element}
                    tmp.add(reponse.pop())
            # ensemble, visited, ensemble
            if len(tmp) > 0:
                cas[element] = [tmp, 0, 0]
            else :
                ensemble1.add(element)
                tmp_student.discard(element)


    creationDictionnaire()
    if len(cas) == 0 : return [{"impossible"}]
    tmp = students[0]
    elementParcourir = cas[tmp][0].copy()
    cas[tmp][2] = 1
    cas[tmp][1] = 1
    tmp_student.discard(tmp)


    ensemble(tmp,1)

    placerDansTableau(elementParcourir,1)

    while len(elementParcourir) > 0 or len(tmp_student) > 0:
        if len(elementParcourir) > 0 :
            tmp = elementParcourir.pop()
            cas[tmp][1] = 1
            tmp_student.discard(tmp)
            retour = ensemble(tmp,cas[tmp][2])
            if retour != None : return [{"impossible"}]
            tmp_elementParcourir = cas[tmp][0].copy()
            delete = tmp_elementParcourir.copy()
            for element in delete:
                if element not in tmp_student:
                    tmp_elementParcourir.discard(element)
            placerDansTableau(tmp_elementParcourir,cas[tmp][2])
            elementParcourir = elementParcourir.union(tmp_elementParcourir)
        elif len(tmp_student) > 0:
            tmp = tmp_student.pop()
            cas[tmp][1] = 1
            if cas[tmp][2] == 0:
                cas[tmp][2] = 1
            retour = ensemble(tmp, cas[tmp][2])
            if retour != None: return [{"impossible"}]
            tmp_elementParcourir = cas[tmp][0].copy()
            delete = tmp_elementParcourir.copy()
            for element in delete:
                if element not in tmp_student:
                    tmp_elementParcourir.discard(element)
            placerDansTableau(tmp_elementParcourir, cas[tmp][2])
            elementParcourir = elementParcourir.union(tmp_elementParcourir)


    if len(ensemble2.intersection(ensemble1)) > 0 or len(ensemble1.union(ensemble2)) != len(students):
        return [{"impossible"}]
    else :
        return ensemble1, ensemble2

# Normalement, vous ne devriez pas avoir à modifier
# Normaly, you shouldn't need to modify
def main(args):
    input_file = args[0]
    output_file = args[1]
    students, pairs = read(input_file)
    output = createGroups(students, pairs)
    a = 0
    write(output_file, output)


# Ne pas changer
# Don't change
if __name__ == '__main__':
    main(sys.argv[1:])