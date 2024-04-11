#Nom, matricule
#Nom, matricule

import sys

#Fonction pour lire le fichier d'input. Vous ne deviez pas avoir besoin de la modifier.
#Retourne la liste des noms d'étudiants (students) et la liste des paires qui ne peuvent
#doivent pas être mis dans le même groupe (pairs)
#
#Function to read the input file. You shouldn't have to modify it.
#Returns the list of student names (students) and the list of pairs of students that
#shouldn't be put in the same group (pairs)
def read(fileName):
    # lecture du fichier
    fileIn = open(fileName,"r")
    linesIn = fileIn.readlines()
    fileIn.close()

    nbStudents = int(linesIn[0])
    students = []
    if(nbStudents != 0):
        students = [s.strip() for s in linesIn[1:nbStudents+1]]
    nbPairs = int(linesIn[nbStudents+1])
    pairs = []
    if(nbPairs != 0):
        pairs = [s.strip().split() for s in linesIn[nbStudents+2:nbStudents+nbPairs+2]]

    return students, pairs


#Fonction qui écrit dans le fichier d'output. 
#le paramètre content est un string
#
#Function that writes in the output file.
#The content parameter is a string
def write(fileName, content):
    with open(fileName, "w") as outputFile:
        for ensemble in content:
            ligne = ' '.join(sorted(ensemble))
            outputFile.write(ligne + "\n")

#Fonction principale à compléter.
#students : liste des noms des étudiants
#pairs : liste des paires d'étudiants à ne pas grouper ensemble
# chaque paire est sous format de liste [x, y]
#Valeur de retour : string contenant la réponse. Si c'est impossible, retourner "impossible"
#                   Sinon, retourner en un string les deux lignes représentant les
#                   les deux groupes d'étudants (les étudiants sont séparés par des
#                   espaces et les deux lignes séparées par un \n)
#
#Function to complete
#students : list of student names
#pairs : list of pairs of students that shouldn't be grouped together.
#        each pair is given as a list [x, y]
#Return value : string with the output. If it is impossible, return "impossible".
#               otherwise, return in a single string both ouput lines that contain
#               two groups (students are separated by spaces and the two lines by a \n)
def createGroups(students, pairs):
    longueur =len(students)
    students_sets = [{element} for element in students]
    def verifierPresence(ensemble):
        liste_d_ensembles = [set(sous_liste) for sous_liste in pairs]
        for element in liste_d_ensembles:
            if len(ensemble.intersection(element)) > 1:
                return False
        return True


    resultat = []

    for k in students_sets :
        compteur = 0
        while compteur <= longueur:
            tmp = [k]
            for i in tmp :
                for j in students_sets:
                    ensPartieJ = j - i
                    nvEns = i.union(j)
                    if i != j and nvEns not in tmp and nvEns not in resultat and ensPartieJ not in i and len(nvEns) > 1 :
                        ajouter = verifierPresence(nvEns)
                        if ajouter:
                            tmp.append(nvEns)
                            resultat.append(nvEns)
            compteur += 1

    students = set(students)
    if len(resultat) == 0: return [{"impossible"}]
    # on cherche le 2 groupe
    # on sait que resultat ne peut jamais etre egale a 1
    for i in range(len(resultat) - 1):
        for j in range(i + 1, len(resultat)):
            if resultat[i].union(resultat[j]) == students and len(resultat[i].intersection(resultat[j])) == 0:
                return [resultat[i], resultat[j]]
    return [{"impossible"}]

#Normalement, vous ne devriez pas avoir à modifier
#Normaly, you shouldn't need to modify
def main(args):
    input_file = args[0]
    output_file = args[1]
    students, pairs = read(input_file)
    output = createGroups(students, pairs)
    write(output_file, output)
            

#Ne pas changer
#Don't change
if __name__ == '__main__':
    main(sys.argv[1:])