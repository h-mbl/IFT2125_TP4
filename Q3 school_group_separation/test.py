# Nom, matricule
# Nom, matricule

import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

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
    def build_groups(dangerous_dict):
        visited = set()
        group1 = []
        group2 = []

        def dfs(node, group, other_group):
            visited.add(node)
            group.append(node)
            for neighbor in dangerous_dict[node]:
                if neighbor not in visited:
                    dfs(neighbor, other_group, group)

        for node in dangerous_dict:
            if node not in visited:
                dfs(node, group1, group2)

        return group1, group2 , visited
    def build_dangerous_pairs_dict(dangerous_pairs):
        dangerous_dict = defaultdict(list)
        for pair in dangerous_pairs:
            child1, child2 = pair
            dangerous_dict[child1].append(child2)
            dangerous_dict[child2].append(child1)
        return dangerous_dict


    dangerous_dict = build_dangerous_pairs_dict(pairs)
    groupe1 , groupe2 , visited  = build_groups(dangerous_dict)
    tmp_student = set(students)
    elementSeul = tmp_student - visited
    if len(elementSeul) == 0:
        groupe1.extend(list(elementSeul))
    groupe1 = set(groupe1)
    groupe2 = set(groupe2)
    if len(groupe1.intersection(groupe2)) > 0 or len(groupe1.union(groupe2)) != len(students):
        return [{"impossible"}]
    else:
        return groupe1, groupe2
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