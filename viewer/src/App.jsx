import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState("waiting...")

  useEffect(() => {
    fetch("http://127.0.0.1:8000/ping")
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("backend unreachable"))
  }, [])

  return (
    <div style={{ fontFamily: "sans-serif", padding: 20 }}>
      <h1>Evolution Simulator Viewer</h1>
      <p>Backend says: {message}</p>
    </div>
  )
}

export default App
