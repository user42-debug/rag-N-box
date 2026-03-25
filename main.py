from sources.capteur import Capteur
from sources.camera import Picture
#from sources.classification import Classifier
from sources.messages import Message
import os
import time

number = "0752084890"

text = [
    "A nutria",
    "An animal",
    "An empty cage",
    "A cat",
    "A rabbit",
    "A dog",
    "A mouse",
    "A rat"
]

capteur = Capteur(4)
#classifier = Classifier()
message = Message("/dev/ttyUSB3")

last = False

while True:
    if capteur:
        
        if not last:
            print("aimant")
            pic = Picture()
            is_rag = True #classifier.predict(pic)
            if is_rag:
                message.send_message(number, "animal detecté")
            else:
                message.send_message(number, "autre animal detecté")
        last = True
    else:
        last = False

    time.sleep(2)
