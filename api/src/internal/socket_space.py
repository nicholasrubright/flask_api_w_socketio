from flask_socketio import Namespace, send, SocketIO, join_room, leave_room
from src.models import Movie, MovieSchema

test_movies = Movie(1, "test movie!!!")



class SocketSpace(Namespace):

    def on_join(self, session):
        context_id = session['context_id']
        print("joined room")
        join_room(context_id)

    def on_notifyroom(self, session):
        context_id = session['context_id']
        movie_json = MovieSchema().dump(test_movies, many=False)
        send(movie_json, json=True, room=context_id)


sClient = SocketIO(cors_allowed_origins="*")
