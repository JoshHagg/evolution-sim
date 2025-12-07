import { useEffect, useState } from "react";
import Viewer from "./Viewer";

function App() {
  const [message, setMessage] = useState("waiting...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/ping")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("backend unreachable"));
  }, []);

  return (
    <div
      style={{ fontFamily: "sans-serif", width: "100vw", height: "100vh", margin: 0, padding: 0, display: "flex", flexDirection: "column",}}
    >{/* Header */}
    <div style={{ padding: 10, background: "#222", color: "white" }}>
      <h1 style={{ margin: 0 }}>Evolution Simulator Viewer</h1>
      <p style={{ margin: 0 }}>Backend says: {message}</p>
    </div>

    {/* Viewer takes ALL remaining space */}
    <div style={{ flexGrow: 1, minHeight: 0 }}>
      <Viewer />
    </div>
    </div>
  );
}

export default App;
