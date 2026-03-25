
import time
import serial

class Message:
    def __init__(self, port):
        self.SERIAL_PORT = port
        self.BAUD = 9600
        self.ser = serial.Serial(self.SERIAL_PORT, self.BAUD, timeout=1)

    def send_at(self, cmd, wait=0.5):
        """
        Envoie une requete 
        """
        self.ser.write((cmd + "\r\n").encode())
        time.sleep(wait)
        resp = self.ser.read_all().decode(errors="ignore")
        print(f">>> {cmd}")
        print(resp.strip())
        return resp


    def send_message(self, numero, message):
        """
        Envoie un message
        numero : le numéro de telephone du receveur (string)
        message : le message envoyé (string)
        """
        
        time.sleep(1)                          # attente obligatoire entre les requêtes
        self.send_at("AT")                     # vérification fonctionement du module. si renvoie pas ok : module défaillant
        time.sleep(1)
        self.send_at("AT+CMGF=1")              # passe en mode texte
        time.sleep(1)
        self.send_at('AT+CSCS="GSM"')
        time.sleep(1)
        self.send_at('AT+CMGL="ALL"')          # reçoit tous les messages
        time.sleep(1)
        self.send_at(f'AT+CMGS="{numero}"')    # set le numéro à qui envoyer
        time.sleep(1)
        self.ser.write(message.encode())       # envoie le message
        time.sleep(1)
        self.send_at("\x1A")                   # crtl+Z
