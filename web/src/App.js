import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Main from "./components/Main";
import Footer from "./components/Footer";

import "./styles/home.css";

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
    <Router>
      <div>
        <Header />
        <Routes>
          <Route path="/" element={<Main />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  )
}

export default App;
