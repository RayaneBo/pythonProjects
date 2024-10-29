
from asyncio.windows_events import NULL


nombreVentes = int(input("Combien de produits vendus ? : "))
prixDeVente = float(input("A quel prix ? : "))
coutDeProduction = float(input("Quel est le coût de production par article ? : "))
coutDeLivraison = float(input("Quel le coùt de livraison par article (facultatif) ? : "))

if coutDeLivraison is NULL:
    coutDeLivraison = 0
    

print((nombreVentes*prixDeVente)-
      (nombreVentes*coutDeProduction)
      -(nombreVentes*coutDeLivraison))

