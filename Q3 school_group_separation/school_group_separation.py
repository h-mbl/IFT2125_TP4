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
    try:
        students = [int(x) for x in students]
        pairs = [int(x) for x in pairs]
    except: pass
    students_sets = [[element] for element in students]
    tmp_student = set(students)
    pairs = [set(sous_liste) for sous_liste in pairs]
    def verifierPresence(ensemble):
        for element in pairs :
            if len(ensemble.intersection(element)) > 1 :
                return False
        return True

    def combinaison(element):
        combinaison = []
        combinaison_set = []
        for i in range(len(element)):
            for j in range(i + 1, len(element)):
                elementI = element[i]
                elementI_set = set(elementI)
                elementJ = element[j]
                elementJ_set = set(elementJ)
                #ensPartieJ = elementJ - elementI
                nvEns = elementI + elementJ[len(elementJ)-1:]
                nvEns_set = set(nvEns)
                if len(nvEns) > 1 and nvEns_set not in resultat_set:
                    ajouter = verifierPresence(nvEns_set)
                    if ajouter:
                        combinaison.append(nvEns)
                        combinaison_set.append(nvEns_set)
        return combinaison,combinaison_set
    def combinaisonPremierePartie(element,debut):
        combinaison = []
        combinaison_set = []
        for i in range(len(element)):
            for j in range(debut, len(b)):
                elementI = element
                elementI_set = set(elementI)
                elementJ = b[j]
                elementJ_set = set(elementJ)
                # ensPartieJ = elementJ - elementI
                nvEns = elementI + elementJ[len(elementJ) - 1:]
                nvEns_set = set(nvEns)
                if len(nvEns) > 1 and nvEns_set not in resultat_set:
                    ajouter = verifierPresence(nvEns_set)
                    if ajouter:
                        combinaison.append(nvEns)
                        combinaison_set.append(nvEns_set)
        return combinaison, combinaison_set
    def recherche():
        for i in range(len(resultat_set) - 1):
            for j in range(i + 1, len(resultat_set)):
                if resultat_set[i].union(resultat_set[j]) == tmp_student and len(
                        resultat_set[i].intersection(resultat_set[j])) == 0:
                    return [resultat_set[i], resultat_set[j]]
        return "impossible"

    resultat = []
    resultat_set = []
    b = students_sets.copy()
    for z in range(len(b)):
        a = b[z]
        tmp, tmp_set = combinaisonPremierePartie(a,z+1)
        temporaire = tmp.copy()
        resultat.extend(tmp)
        resultat_set.extend(tmp_set)
        if len(temporaire) > 0 :
            while len(temporaire[0]) < len(students_sets) - 1:
                tmp_x = []
                x = temporaire[0]
                delete = temporaire.copy()
                for element in delete :
                    y = element
                    if x[:-1] == y[:-1] :
                        tmp_x.append(element)
                        temporaire.remove(element)
                    else : break
                a = 0
                tmp,tmp_set = combinaison(tmp_x)
                temporaire.extend(tmp)
                resultat.extend(tmp)
                resultat_set.extend(tmp_set)
                a = 0
                if len(temporaire) == 0 :
                    element_recherche = recherche()
                    if element_recherche != "impossible" :
                        a = 0
                        return element_recherche
                    break
        else: break

    if len(resultat) == 0: return [{"impossible"}]


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