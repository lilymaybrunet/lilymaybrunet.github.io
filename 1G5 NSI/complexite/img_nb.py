from PIL import Image
import time

img=Image.open("phare3.jpg")
largeur,hauteur=img.size
debut = time.time()
#début du traitement

from PIL import Image
img=Image.open("phare3.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        moyenne=(r+v+b)//3
        r = moyenne
        v = moyenne
        b = moyenne
        img.putpixel((x,y),(r,v,b))
img.show()

#fin du traitement
fin = time.time()
print("taille img \t durée de traitement")
print(largeur*hauteur,"\t",fin-debut)
img.show()