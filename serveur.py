import socket
import time
HOST_IP = "10.2.110.47"
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
    text_envoye = input("Vous : ")
    connection_socket.sendall(text_envoye.encode())
    data_recue = connection_socket.recv(MAX_DATA_SIZE)
    if not data_recue:
        break
    print(f"Message : {data_recue.decode()}")

s.close()
connection_socket.close()