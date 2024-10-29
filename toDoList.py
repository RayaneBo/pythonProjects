taches = {
    1: "Faire les courses",
    2: "Aller à la salle",
    3: "Chercher un travail"
}

print(taches)

choix = int(input("Voulez-vous ajouter(1) ou supprimer(2) une tâche : "))

if choix == 1:
    ajout = input("Quelle tâche souhaitez-vous ajouter ? : ")
    taches[4]=ajout
    print(taches)
elif choix == 2 :
    print(taches)
    supp = int(input("Quelle tâche souhaitez-vous supprimer ? : "))
    del taches[supp]
    print(taches)
else:
    print("Ce numéro de tâche n'existe pas")