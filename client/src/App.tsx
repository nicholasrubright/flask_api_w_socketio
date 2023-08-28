import { useEffect, useState } from "react";
import { io, Socket } from "socket.io-client";
import Movies from "./components/Movies";

export default function App() {
  const [socket, setSocket] = useState<Socket | null>(null);

  useEffect((): any => {
    const newSocket = io("http://localhost:8080");
    setSocket(newSocket);
    return () => newSocket.close();
  }, [setSocket]);

  return (
    <div>
      <h1>Test Chat App</h1>
      {socket ? (
        <div>
          <Movies socket={socket} />
        </div>
      ) : (
        <div>Not Connected</div>
      )}
    </div>
  );
}
