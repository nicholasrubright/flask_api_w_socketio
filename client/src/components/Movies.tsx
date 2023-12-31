import { Socket } from "socket.io-client";
import { useEffect, useState } from "react";

const movie_data = [
  {
    id: 1,
    title: "Awesome movie",
  },
  {
    id: 2,
    title: "bad movie",
  },
  {
    id: 3,
    title: "another movie",
  },
  {
    id: 4,
    title: "super cool movie",
  },
];

interface Movie {
  id: number;
  title: string;
}

export default function Movies(props: MoviesProps) {
  const { socket } = props;

  const [clientId, setClientId] = useState<string>("");

  useEffect(() => {
    setClientId(Math.random().toString());
  }, [socket]);

  const [room, setRoom] = useState<string>("");

  const handleEnterRoom = (e: any) => {
    socket.emit("joinRoom", {
      id: clientId,
      room: room,
    });
  };

  const [hasDuo, setHasDuo] = useState<boolean>(false);

  const [hasMatch, setHasMatch] = useState<boolean>(false);

  useEffect(() => {
    const matchListener = () => {
      setHasMatch(true);
    };

    socket.on("foundMatch", matchListener);

    const duoJoinedListener = () => {
      setHasDuo(true);
    };

    socket.on("duoJoined", duoJoinedListener);

    return () => {
      socket.off("foundMatch", matchListener);
      socket.off("duoJoined", duoJoinedListener);
    };
  }, [socket]);

  // where in the movie list is the user
  const [currentIndex, setCurrentIndex] = useState<number>(0);

  const [movies, setMovies] = useState<Movie[]>(movie_data);

  const handleDislike = (e: any) => {
    e.preventDefault();
    setCurrentIndex(currentIndex + 1);
  };

  const handleLike = (e: any) => {
    e.preventDefault();

    socket.emit("likedMovie", {
      room: room,
      id: clientId,
      movie: JSON.stringify(movies[currentIndex]),
    });
    setCurrentIndex(currentIndex + 1);
    console.log("Movie has been liked!!");
  };

  return (
    <div>
      <h1>Movies</h1>
      <div>
        <input type="text" onChange={(e) => setRoom(e.target.value)} />
        <button type="button" onClick={(e) => handleEnterRoom(e)}>
          Join Room
        </button>
      </div>
      {hasMatch && <h1>THERE WAS A MATCH!!</h1>}
      {room !== "" && !hasDuo && (
        <div>
          <h1>Waiting for Friend...</h1>
        </div>
      )}
      {room !== "" && hasDuo && (
        <div>
          <div>
            <h4>Title: {movies[currentIndex].title}</h4>
          </div>
          <div>
            <button type="button" onClick={(e) => handleLike(e)}>
              Like
            </button>
            <button type="button" onClick={(e) => handleDislike(e)}>
              Dislike
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

interface MoviesProps {
  socket: Socket;
}
