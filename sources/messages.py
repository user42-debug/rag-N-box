
import time
import serial

SERIAL_PORT = "COM5"
BAUD = 9600 

ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)

class Message:
    def __init__(self, port):
        self.SERIAL_PORT = port
        self.BAUD = 9600
        self.ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)

    def send_at(self, cmd, wait=0.5):
        self.ser.write((cmd + "\r\n").encode())
        time.sleep(wait)
        resp = ser.read_all().decode(errors="ignore")
        print(f">>> {cmd}")
        print(resp.strip())
        return resp


    def send_message(self, numero,message):
        
        time.sleep(0.1)
        self.send_at("AT")
        time.sleep(0.1)
        self.send_at("AT+CMGF=1")
        time.sleep(0.1)
        self.send_at(f'AT+CMGS="{numero}"')
        time.sleep(0.1)
        self.ser.write(message.encode()
        time.sleep(0.1)
        self.send_at("\x1A")
