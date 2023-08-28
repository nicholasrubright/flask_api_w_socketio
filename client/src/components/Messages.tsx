import { useEffect, useState } from "react";

export default function Messages(props: MessagesProps) {
  const { socket } = props;

  const [message, setMessage] = useState<string>("");

  useEffect((): any => {
    const messageListender = (message: any) => {
      const msg = JSON.stringify(message);
      setMessage(msg);
    };

    socket.on("message", messageListender);

    return () => {
      socket.off("message", messageListender);
    };
  }, [socket]);

  return (
    <div>
      <h1>Messages</h1>
      <p>{message}</p>
    </div>
  );
}

interface MessagesProps {
  socket: any;
}
