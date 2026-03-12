from sources.capteur import Capteur
from sources.camera import Picture
from sources.classification import Classifier
import os
import time

text = [
    "A nutria",
    "An animal",
    "An empty cage",
    "A cat",
    "A rabbit",
    "A dog",
    "A mouse",
    "A rat",
]

capteur = Capteur(4)
classifier = Classifier()

last = False

while True:
    if capteur:
        last = True
        if not last:
            pic = Picture()
            is_rag = classifier.predict(pic)
    else:
        last = False
    
    time.sleep(2)