from flask_socketio import Namespace, SocketIO, emit, join_room, leave_room, rooms
from src.models import Movie, MovieSchema

test_movies = Movie(1, "test movie!!!")


class SocketSpace(Namespace):
    rooms_info = {}

    def addOneToRoom(self, room_id):
        if room_id in self.rooms_info:
            self.rooms_info[room_id]["count"] += 1
        else:
            self.rooms_info[room_id] = {"count": 1}

    def getCount(self, room_id):
        if room_id in self.rooms_info:
            return self.rooms_info[room_id]["count"]

        return 0

    def on_joinRoom(self, data):
        print("Client joined room: ", data, flush=True)
        clientId = data["id"]
        room = data["room"]
        join_room(room)
        self.addOneToRoom(room)
        if self.getCount(room) > 1:
            self.sendDuoJoined(room)

    def on_leaveRoom(self, data):
        clientId = data["id"]
        room = data["room"]
        leave_room(room)

    def sendDuoJoined(self, room_id):
        emit("duoJoined", to=room_id)

    # client wants to send message to all clients
    def on_likedMovie(self, data):
        room_id = data["room"]
        clientId = data["id"]
        movie = data["movie"]
        self.sendFoundMatch(room_id, clientId, movie)

    def sendFoundMatch(self, room_id, clientId, movie):
        emit("foundMatch", to=room_id)


sClient = SocketIO(cors_allowed_origins="*")
