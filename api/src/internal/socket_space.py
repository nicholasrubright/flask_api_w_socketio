from flask_socketio import Namespace, send, SocketIO, emit
from src.models import Movie, MovieSchema

test_movies = Movie(1, "test movie!!!")


class SocketSpace(Namespace):
    # client wants to send message to all clients
    def on_sendMessageToClients(self):
        print("Client wants to send message to all clients", flush=True)
        self.sendMessage()

    def sendMessage(self):
        emit("message", "balls")


sClient = SocketIO(cors_allowed_origins="*")
