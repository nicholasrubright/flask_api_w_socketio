import { io } from "socket.io-client";

export default function App() {
  const socket = io("http://localhost:8080");

  socket.on("connect", () => {
    socket.emit("my event", { data: "Im connected!" });
  });

  return (
    <div>
      <h1>Hello WOrld!!</h1>
    </div>
  );
}
