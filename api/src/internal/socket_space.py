from flask_socketio import Namespace, emit, SocketIO
import time


class SocketSpace(Namespace):
    def on_connect(self):
        print("Will be sneding thingy soon", flush=True)
        time.sleep(10)
        self.notifyPeople()

    def notifyPeople(self):
        emit("balls", {"data": "hello world!"})

    def on_disconnect(self):
        pass

    def on_myevent(self, data):
        # emit("my_response", data)
        print("Testing: ", type(data), flush=True)
        print("hello: ", data, flush=True)


sClient = SocketIO(cors_allowed_origins="*")
