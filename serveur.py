import socket
import subprocess
import time

pos_joue = '-1'
data_recue = None
connection_socket = None

def creer_serveur():
    """
    Fonction qui crée le serveur, attend une connexion
    crée une boucle pour le jeu, attends jusqu'à ce que le serveur joue
    puis attends jusqu'à recevoir le coup de l'adversaire
    :return:
    """
    global pos_joue
    global data_recue
    global connection_socket
    hostname = subprocess.check_output("hostname", shell=True).decode()
    hostname = hostname[:-2]
    IP = socket.gethostbyname(hostname)
    HOST_IP = str(IP)
    HOST_PORT = 32000
    MAX_DATA_SIZE = 1024
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST_IP,HOST_PORT))
    s.listen()

    print(f"Attente de connection sur {HOST_IP}, port {HOST_PORT} ")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")

    continu = True
    while continu:
        while True:
            pos_joue = '-1'
            if envoie_pos_joue_serveur:
                time.sleep(0.05) # limitation d'envoi des données à 20tps
                if pos_joue != '-1':
                    connection_socket.sendall(pos_joue.encode())
                    pos_joue = '-1'
                    break
        while True:
            data_recue = connection_socket.recv(MAX_DATA_SIZE)
            if not data_recue:
                continu = False             # Fait un double break pour couper la connexion
                break
            print(f"Message : {data_recue.decode()}")
            time.sleep(0.05)
            break
        data_recue = None

    connection_socket.close()
    s.close()


def envoie_pos_joue_serveur(col):
    """
    :paramètre colonne sur laquelle le joueur à jouer
    Fonction qui permet de récupérer et convertir en string (afin de l'envoyer) la colonne jouer
    """
    global pos_joue
    pos_joue = str(col)

def get_data_serveur():
    """
    Récupère les données reçues
    """
    global data_recue
    return data_recue

def is_there_connection():
    """
    Vérifie s'il y a une connection sur le serveur
    """
    global connection_socket
    return connection_socket