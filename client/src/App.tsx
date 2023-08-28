import { useEffect, useState } from "react";
import { io } from "socket.io-client";
import Messages from "./components/Messages";
import MessageInput from "./components/MessageInput";

export default function App() {
  const [socket, setSocket] = useState<any>(null);

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
          <Messages socket={socket} />
          <MessageInput socket={socket} />
        </div>
      ) : (
        <div>Not Connected</div>
      )}
    </div>
  );
}
