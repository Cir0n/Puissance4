import socket
import time

HOST_IP = ""
HOST_PORT = 32000
MAX_DATA_SIZE = 1024



def connect(ip):
    HOST_IP = ip.get()
    print(f"Connexion au server {HOST_IP}, port {HOST_PORT}")
    while True :
        try :
            s = socket.socket()
            s.connect((HOST_IP, HOST_PORT))
        except ConnectionRefusedError :
            print("ERREUR : impossible de se connecter au serveur, Reconnexion...")
            time.sleep(4)
        else :
            print("Connecté au server")
            break
    while True :
        Data_recues = s.recv(MAX_DATA_SIZE)
        if not Data_recues :
            break
        print(f"Message : {Data_recues.decode()}")
        texte_envoyer = input("Vous : ")
        s.sendall(texte_envoyer.encode())


    s.close()