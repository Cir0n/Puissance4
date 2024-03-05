import socket
import subprocess
import time
pos_joue = '-1'
data_recue = None
def creer_serveur():
    global pos_joue
    global data_recue
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
                time.sleep(0.05)
                if pos_joue != '-1':
                    connection_socket.sendall(pos_joue.encode())
                    pos_joue = '-1'
                    break
        while True:
            data_recue = connection_socket.recv(MAX_DATA_SIZE)
            if not data_recue:
                continu = False
                break
            print(f"Message : {data_recue.decode()}")
            break
        data_recue = None
    s.close()
    connection_socket.close()

def envoie_pos_joue_serveur(col):
    global pos_joue
    pos_joue = str(col)

def get_data_serveur():
    global data_recue
    return data_recue