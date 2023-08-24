import { useEffect } from "react";
import { io } from "socket.io-client";

export default function App() {
  useEffect(() => {
    const socket = io("http://localhost:8080");
    socket.connect();

    function onBallsEvent(data: any) {
      console.log("I GOT THE DATA FROM BALLS!!!: ", data);
    }

    socket.on("balls", onBallsEvent);
  }, []);

  return (
    <div>
      <h1>Hello WOrld!!</h1>
    </div>
  );
}
