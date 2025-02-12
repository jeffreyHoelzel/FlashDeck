import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const backendUrl = process.env.BACKEND_URL || "http://localhost:5000";

    fetch(`${backendUrl}`)
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => setMessage("Error connecting to backend", err));
  }, []);

  return (
    <h1>{message}</h1>
  )
}

export default App;
