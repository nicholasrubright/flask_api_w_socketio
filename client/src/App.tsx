import { useEffect } from "react";
import { io } from "socket.io-client";

export default function App() {
  const socket = io("http://localhost:8080");

  const notifyRoom = (e: any) => {
    socket.emit("notifyroom", { context_id: "999" });
  };

  useEffect(() => {
    socket.connect();

    function onBallsEvent(data: any) {
      console.log("I GOT THE DATA FROM BALLS!!!: ", data);
    }

    socket.on("notifyroom", (data) => console.log("thingy: ", data));

    socket.on("balls", onBallsEvent);
  }, [socket]);

  return (
    <div>
      <h1>Hello WOrld!!</h1>
      <button type="button" onClick={(e) => notifyRoom(e)}>
        Notify Room
      </button>
    </div>
  );
}
