# Créé par lilymay.brunet, le 09/05/2023 en Python 3.7

def recherche(caractere,chaine):
   nb_occurences=0
   for n in range(len(chaine)):
       if caractere==chaine[n]:
          nb_occurences+=1
   return nb_occurences

print(recherche('e', "sciences")) #2
print(recherche('i', "mississippi")) #4
print(recherche('a', "mississippi"))#0