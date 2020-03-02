# -*- coding: utf-8 -*-

import os
import sys
from core import predict
from timeit import default_timer as timer


print('--- Classifieur Mer vs Ailleurs : TEAM LES PURISTES (mode dossier)')

if (len(sys.argv) == 2):
    folder_name = sys.argv[1]
else:
    folder_name = input('nom du dossier (exemple: "images"): ')

preds = list()

start = timer()

for img_name in os.listdir(folder_name):
        try:
            preds.append([img_name, predict('./' + folder_name + '/' + img_name, 1, 'Mer')])
        except IOError:
            print ('Erreur sur ouverture du fichier ')

end = timer()

print("--------- RAPPORT")

total_mer = 0

for elem in preds:
    is_mer = elem[1] >= 0.5
    
    if is_mer:
        total_mer += 1
    
    
    print('> "%s" : %s (%0.2f)' % (elem[0], ('Mer' if is_mer else 'Ailleurs'), elem[1]))
    
print('Total "Mer" : %d/%d' % (total_mer, len(preds)))
print('Temps d\'execution total (IO inclus) : %0.4f ms' % (end - start))
print("--------- FIN RAPPORT")