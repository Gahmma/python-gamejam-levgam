import socket
import threading

class MUDServer:

    def __init__(self, port):
        self.port = port
        self.clients = []

    def listen(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", self.port))
        server.listen(5)

        while True:
            client, address = server.accept()
            threading.Thread(target=self.handle_client, args=(client, address)).start()

    def handle_client(self, client, address):
        client.send("Welcome to the MUD!\n")

        while True:
            message = client.recv(1024).decode("utf-8")

            if message == "quit":
                break

            elif message.startswith("look"):
                self.describe_room(client, message)

            elif message.startswith("say"):
                self.say_in_room(client, message)

            else:
                client.send("I don't understand that command.\n")

        client.close()

    def describe_room(self, client, message):
        room_name = message.split()[1]

        for room in self.rooms:
            if room.name == room_name:
                client.send(room.description + "\n")
                break

    def say_in_room(self, client, message):
        room_name = message.split()[1]
        message = message[len(room_name) + 1:]

        for player in self.clients:
            if player.room == room_name:
                player.send("{} says: {}".format(client.name, message))

    def add_room(self, room):
        self.rooms.append(room)

    def add_client(self, client):
        self.clients.append(client)

if __name__ == "__main__":
    port = 8000

    mud_server = MUDServer(port)
    mud_server.listen()