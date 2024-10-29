
typeDeMatrice = int(input("Taille de la matrice (2 ou 3) : "))

#Cas d'une matrice de taille 2

def det2x2():
    a, b = list(input("Inserez la 1ère ligne sous la forme a b :").split())
    c, d = list(input("Inserez la 2ème ligne sous la forme c d :").split())
    print(int(a)*int(d) - int(b)*int(c))

#Cas d'une matrice de taille 3

def det3x3():
    a, b, c = list(input("Inserez la 1ère ligne sous la forme a b c : ").split())
    d, e, f = list(input("Inserez la 2ème ligne sous la forme d e f : ").split())
    g, h, i = list(input("Inserez la 3ème ligne sous la forme g h i : ").split())
    print((int(a)*int(e)*int(i) + int(d)*int(h)*int(c) 
           + int(b)*int(f)*int(g))-(int(g)*int(e)*int(c) 
           + int(d)*int(b)*int(i) + int(a)*int(h)*int(f)))


if typeDeMatrice == 2:
    print(det2x2())
elif typeDeMatrice == 3:
    print(det3x3())
else:
    print("Valeur de taille de matrice incorrecte")