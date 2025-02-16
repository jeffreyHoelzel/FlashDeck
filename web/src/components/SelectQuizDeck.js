import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/quiz.css";

function SelectQuizDeck() {
  const [decks, setDecks] = useState([]);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const backendUrl = process.env.BACKEND_URL || "http://localhost:5000";

  useEffect(() => {
    const fetchDecks = async () => {
      try {
        const response = await fetch(`${backendUrl}/get_all_decks`);
        if (response.ok) {
          const data = await response.json();
          setDecks(data.decks);
        } else {
          setMessage("Error loading decks.");
        }
      } catch (error) {
        setMessage("Failed to connect to backend.");
      }
    };

    fetchDecks();
  }, []);

  return (
    <div className="quiz-deck-container">
      <h2>Select a Deck for Your Quiz</h2>
      {message && <p className="result-message">{message}</p>}
      <ul>
        {decks.map((deck) => (
          <li key={deck.id}>
            {deck.name}
            <button onClick={() => navigate(`/quiz/${deck.id}`)} style={{ marginLeft: "10px" }}>
              Start Quiz
            </button>
          </li>
        ))}
      </ul>
      <button className="send-home" onClick={() => navigate("/")}>Back to Home</button>
    </div>
  );
}

export default SelectQuizDeck;
