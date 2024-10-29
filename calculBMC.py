
poids = input("Quel est votre poids en kg ? : ")
taille = input("Quelle est votre taille en mètres ? : ")
age = input("Quel est votre âge en années ? : ")
genre = input("Quel est votre genre (H ou F) ? : ")

#Femmes : métabolisme basal = 9,740 x Poids (en kg) + 172,9 x Taille (en mètres)
#         – 4,737 x Âge (en années)  + 667,051

def femme():
    print((9.740 * int(poids))+(172.9 * float(taille))-(4.737 * int(age))+667.051)

#Hommes : Métabolisme Basal = 13,707 x Poids (kg) + 492,3 x Taille (mètres)
#          – 6,673 x Âge (années) + 77,607

def homme():
    print((13.707 * int(poids))+(492.3 * float(taille))-(6.673 * int(age))+77.607)



if genre == "H" or genre == "h":
    print(homme())
elif genre == "F" or genre == "f":
    print(femme())
else:
    print("Insérez un genre valable (H ou F) ")
