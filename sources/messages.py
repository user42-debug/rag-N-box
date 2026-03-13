
import time
import serial

SERIAL_PORT = "COM5"
BAUD = 9600  # adapte si ton module est à 9600

ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)

class Message:
    def __init__(self):
        self.SERIAL_PORT = "COM5"
        self.BAUD = 9600
        self.ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)

def send_at(cmd, wait=0.5):
    ser.write((cmd + "\r\n").encode())
    time.sleep(wait)
    resp = ser.read_all().decode(errors="ignore")
    print(f">>> {cmd}")
    print(resp.strip())
    return resp

if __name__ == "__main__":
    time.sleep(2)  # temps que le module démarre si besoin
    #send_at("AT")
    #send_at("AT+CMGF=1")      # numéro de la SIM
    
    #send_at("AT+CSQ")       # qualité du signal
    #send_at("AT+CREG?")     # enregistrement réseau
    # Exemple APN générique (remplace ton_APN):
    #Wsend_at('AT+CGDCONT=1,"IP","ton_APN"')
#numero=input()
#message=input()
def send_message(numéro,message):
    
    time.sleep(0.1)
    send_at("AT")
    #time.sleep(0.1)
    send_at("AT+CMGF=1")
    #time.sleep(0.1)
    send_at('AT+CMGS="0769157193"')
    time.sleep(0.1)
    ser.write(b"ca va alexandre?")
    #time.sleep(0.1)
    send_at("\x1A")
send_message(0,"")