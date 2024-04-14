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



def createGroups(students, dangerous_pairs):
    dangerous_pairs = [set(pair) for pair in dangerous_pairs]
    sys.setrecursionlimit(1000000)

    def backtrack(group1, group2, remaining):
        if not remaining:
            return group1, group2

        student = remaining.pop()

        for group, other_group in ((group1, group2), (group2, group1)):
            if not any(student in pair & set(group) for pair in dangerous_pairs):
                group.add(student)
                result = backtrack(group, other_group, remaining)
                if result is not None:
                    return result
                group.remove(student)

        remaining.add(student)
        return None

    group1, group2 = backtrack(set(), set(), set(students))
    if group1 is None:
        return "Impossible"
    return group1, group2


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