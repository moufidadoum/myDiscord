import socket
import threading

IP_ADDRESS = "0.0.0.0" # adresse IP pour écouter toutes les connexions
PORT = 1234 # port d'écoute pour le serveur

# Liste des connexions clients
clients = []

def broadcast(message, sender):
    """
    Fonction pour envoyer un message à tous les autres clients connectés
    """
    for client in clients:
        if client != sender:
            client.sendall(message.encode())

def handle_client(client):
    """
    Fonction pour gérer une connexion client
    """
    while True:
        try:
            # Recevoir les données du client
            data = client.recv(1024).decode()
            broadcast(data, client)
        except:
            # Si une erreur se produit, fermer la connexion et supprimer le client de la liste
            clients.remove(client)
            client.close()
            break

def start_server():
    """
    Fonction pour démarrer le serveur de chat
    """
    # Créer un socket pour le serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP_ADDRESS, PORT))
    server_socket.listen()

    print("Serveur démarré sur {}:{}".format(IP_ADDRESS, PORT))

    while True:
        # Attendre une nouvelle connexion
        client_socket, client_address = server_socket.accept()

        # Ajouter la connexion client à la liste
        clients.append(client_socket)

        # Lancer un nouveau thread pour gérer la connexion client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()