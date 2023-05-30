# Créé par lilymay.brunet, le 09/05/2023 en Python 3.7
def correspond(mot,mots_a_trous):
    for n in range(mot,mots_a_trous):
        if mot==mot_a_trous:

           return false
        else:

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) #True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) #False
print(correspond('STOP', 'S*')) #False
p0