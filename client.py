import socket
import time

HOST_IP = ""
HOST_PORT = 32000
MAX_DATA_SIZE = 1024
pos_joue = '-1'
data_recue = None

def connect(ip):
    """

    :param IP de l'host
    :return false
    """
    global data_recue
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
    continu = True
    while continu:
        while True:
            data_recue = s.recv(MAX_DATA_SIZE)
            if not data_recue:
                continu = False
                break
            print(f"Message : {data_recue.decode()}")
            break
        data_recue = None
        while True:
            global pos_joue
            pos_joue = '-1'
            if envoie_pos_joue_client:
                time.sleep(0.05)  # Limitation d'envoi des données à 20tps
                if pos_joue != '-1':
                    s.sendall(pos_joue.encode())
                    pos_joue = '-1'
                    break
    s.close()

def envoie_pos_joue_client(col):
    """
    :paramètre colonne sur laquelle le joueur à jouer
    Fonction qui permet de récupérer et convertir en string (afin de l'envoyer) la colonne jouer
    """
    global pos_joue
    pos_joue = str(col)

def get_data_client():
    """
    Récupère les données reçues
    """
    global data_recue
    return data_recue