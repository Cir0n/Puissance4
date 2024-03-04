import socket
import time
HOST_IP = "127.0.0.1"
HOST_PORT = 32000



print("Connexion au serveur IP : ", HOST_IP)
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print("Connecté au serveur")
        break



s.close()