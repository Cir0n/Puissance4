import socket
import subprocess
import time

def creer_serveur():
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


    while True :
        global pos_joue
        pos_joue = '-1'
        if envoie_pos_joue:
            if pos_joue != '-1':
                connection_socket.sendall(pos_joue.encode())
                pos_joue = '-1'
                data_recue = connection_socket.recv(MAX_DATA_SIZE)
                if not data_recue:
                    break
                print(f"Message : {data_recue.decode()}")

    s.close()
    connection_socket.close()

def envoie_pos_joue(col):
    global pos_joue
    pos_joue = str(col)
