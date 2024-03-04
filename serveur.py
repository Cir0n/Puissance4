import socket
HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()                 #création socket d'écoute
s.bind((HOST_IP,HOST_PORT))          #ecoute sur le port 32000
s.listen()
print("attente de connexion sur ", HOST_IP, "port ", HOST_PORT)
connectionScoket, clientAddress = s.accept()   #fonction bloquante qui retourne des infos sur le client
print(f"connexion établie avec {clientAddress}")






