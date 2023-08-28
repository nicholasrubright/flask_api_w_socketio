from flask_socketio import Namespace, SocketIO, emit, join_room, leave_room
from src.models import Movie, MovieSchema

test_movies = Movie(1, "test movie!!!")


class SocketSpace(Namespace):
    def on_joinRoom(self, data):
        print("Client joined room: ", data, flush=True)
        clientId = data["id"]
        room = data["room"]
        join_room(room)

    def on_leaveRoom(self, data):
        clientId = data["id"]
        room = data["room"]
        leave_room(room)

    # client wants to send message to all clients
    def on_likedMovie(self, data):
        room_id = data["room"]
        clientId = data["id"]
        movie = data["movie"]
        self.sendFoundMatch(room_id, clientId, movie)

    def sendFoundMatch(self, room_id, clientId, movie):
        emit("foundMatch", to=room_id)


sClient = SocketIO(cors_allowed_origins="*")
