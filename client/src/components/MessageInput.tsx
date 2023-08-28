export default function MessageInput(props: MessageInputProps) {
  const { socket } = props;

  // sends a message to the server to send the message to all clients
  const handleButtonPress = (e: any) => {
    e.preventDefault();
    socket.emit("sendMessageToClients");
  };

  return (
    <div>
      <button type="button" onClick={(e) => handleButtonPress(e)}>
        Get Message
      </button>
    </div>
  );
}

interface MessageInputProps {
  socket: any;
}
