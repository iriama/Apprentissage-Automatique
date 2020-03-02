# -*- coding: utf-8 -*-
import sys
from core import predict

print('--- Classifieur Mer vs Ailleurs : TEAM LES PURISTES (mode image)')
print('les images deveront etre placees dans le dossier "images"')

if (len(sys.argv) == 2):
    img_name = sys.argv[1]
else:
    img_name = input('nom de l\'image (exemple: "ocean.jpeg"): ')
    

predict('./images/' + img_name, 1, 'Mer')