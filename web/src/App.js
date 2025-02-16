import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Main from "./components/Main";
import Footer from "./components/Footer";

import "./styles/home.css";
import CreateDeckForm from "./components/CreateDeck";
import EditDeckForm from "./components/EditDeck";
import DeckList from "./components/DeckList";
import Quiz from "./components/Quiz";
import SelectQuizDeck from "./components/SelectQuizDeck";

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
          <Route path="/create_new_deck" element={<CreateDeckForm />} />
          <Route path="/edit_existing_deck" element={<DeckList />} />
          <Route path="/edit_deck/:deckId" element={<EditDeckForm />} />  
          <Route path="/quiz_deck" element={<SelectQuizDeck />} />
          <Route path="/quiz/:deckId" element={<Quiz />} />        
        </Routes>
        <Footer />
      </div>
    </Router>
  )
}

export default App;
