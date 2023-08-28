from flask_socketio import Namespace, send, SocketIO, emit
from src.models import Movie, MovieSchema

test_movies = Movie(1, "test movie!!!")


class SocketSpace(Namespace):
    def on_connect(self):
        print("A user connected", flush=True)

    # client wants to send message to all clients
    def on_likedMovie(self, movie):
        print("client liked movie: ", movie, flush=True)
        self.sendFoundMatch()

    def sendFoundMatch(self):
        emit("foundMatch", broadcast=True)


sClient = SocketIO(cors_allowed_origins="*")
