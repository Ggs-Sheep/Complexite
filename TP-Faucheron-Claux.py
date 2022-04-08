#TP Complexité Faucheron Alcide et Claux Clarence

import time
import plotly.express as px
import pandas as pd

liste_n = []
liste_occurences = []
liste_temps_execution = []

def afficher_courbe(name):
    df = pd.DataFrame(dict(
        n = liste_n,
        ms = liste_temps_execution
    ))
    fig = px.line(df, x="n", y="ms", title="Temps d'execution en fontoin du temps pour algo " + name) 
    #fig.show()
    fig.write_html("/Users/alcidefaucheron/Documents/Cours/Compléxité algorythmique/TP/"+name+".html")

def get_data_hanoi(n):
    for index in range(1, n):
        liste_n.append(index)

        debut = time.time()
        liste_occurences.append(hanoi(index))
        fin = time.time()

        temps_execution = fin - debut
        liste_temps_execution.append(temps_execution*1000)
        
        print("Pour n = ", index, " | temps d'exécution = ", round(temps_execution*1000, 3), "ms", " (précisément : ", temps_execution, "s)")

def hanoi_tour(n, A, B, C, occurence):

    if n == 1:
        return occurence
    return hanoi_tour(n - 1, A, C, B, occurence + 1) + hanoi_tour(n - 1, C, B, A, occurence + 1)


def hanoi(n):
    return hanoi_tour(n, 'A', 'B', 'C', 0)


def main_exo_1():
    n = int(input("Entrez la valeur de n : "))
    print("\nDebut de Hanoi\n")
    get_data_hanoi(n)
    afficher_courbe("hanoi")


def suite_interative(n):
    res = []
    for i in range(n + 1):
        if i == 0 or i == 1:
            res.append(1)
        else:
            res.append(res[i - 1] + res[i - 2])

    return res[-1]


def suite_recursive(n):

    if n == 0 or n == 1:
        return 1
    else:
        return suite_recursive(n - 1) + suite_recursive(n - 2)


def get_data_suite(n, fonction):

    for index in range(1, n):
        liste_n.append(index)

        debut = time.time()
        fonction(index)
        fin = time.time()

        temps_execution = fin - debut
        liste_temps_execution.append(temps_execution*1000)
        #print(index)
        
        print("Pour n = ", index, " | temps d'exécution = ", round(temps_execution*1000, 3), "ms", " (précisément : ", temps_execution*1000, "ms)")


def main_exo_2():

    n = int(input("Entrez la valeur de n : "))

    get_data_suite(n, suite_recursive)
    #get_data_suite(n, suite_interative)
    afficher_courbe("suite")


def creation_tableau_entiers(n):
    tableau = []

    for i in range(1, n):
        tableau.append(i)
    
    del(tableau[0])    
    return tableau


def eratosthene_crible(tableau, n):

    for i in range(2, n):
        if(tableau[i] != 1):
            for j in range(i + 1, n):
                if(tableau[j] % tableau[i] == 0):
                    tableau[j] = 1             

    return tableau


def main_exo_3():
    
    for n in ([5, 10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 10000, 15000, 20000, 40000]):

        tableau = creation_tableau_entiers(n)
        debut = time.time()

        eratosthene_crible(tableau, len(tableau))

        fin = time.time()

        temps_execution = fin - debut
        liste_n.append(n)
        liste_temps_execution.append(temps_execution)
        print(temps_execution)

        print(n)

    afficher_courbe("eratosthene_crible")


if __name__ == "__main__":
    main_exo_1()
    #main_exo_2()
    #main_exo_3()
