import time
import os

"""
On test la commande rpicam-jpeg, qui permet de sauvegarder l'état actuel de la caméra en un jpg.
Ici, on crée 3 fichiers .jpg (test0, test1 et test2) a 5 secondes d'intervalle
"""

for i in range(3):
    os.system(f'rpicam-jpeg --output test{i}.jpg --timeout 10')
    
    time.sleep(5)