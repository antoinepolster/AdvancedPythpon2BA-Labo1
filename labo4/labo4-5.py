import socket
import threading

s = socket.socket() #création du socket 
serverAddress = ('0.0.0.0', 3000) #définir l'adresse sur laquelle se connecter et le port 
s.bind(serverAddress) #se lier à l'adresse 

def serveur():
    address = input("Votre addres IP : ")
    s.listent() # écoute pour voir si il y a un message 
    print('Le client avec comme addresse IP ' + address +' est connecté')
    while True:
        client, address = s.accept() #le code s'arrête jusqu'à une conection
        message_Duclient = client.recv(2048).decode() #convertit le binaire en txt
        print(message_Duclient)
        message_perso = input(">>").encode() #encode notre msg en binaire
        client.send(message_perso) #envoi de notre msg

thread2 =threading.Thread(target = serveur)
thread2.start()
s.connect(serverAddress) #attribuer la valeur de 'client' au socket
while True:
    msg_client = input(">>").encode() #convertit en binaire
    s.send(msg_client) #envoie le msg du client
    reponse = s.recv(2048).decode()
    print(reponse)
