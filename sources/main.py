from sources.capteur import Capteur
from sources.camera import Picture
from sources.classification import Classifier
from sources.messages import Message
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
    "A rat",]

capteur = Capteur(4)
classifier = Classifier()
message = Message("/dev/ttyUSB2")

last = False

while True:
    if capteur:
        last = True
        if not last:
            pic = Picture()
            is_rag = classifier.predict(pic)
            if is_rag:
                message.send_message("0600000000", "ragondin detecté")
            else:
                message.send_message("0600000000", "autre animal detecté")
    else:
        last = False

    time.sleep(2)
