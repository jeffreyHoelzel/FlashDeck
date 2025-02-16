import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function DeckList() {
  const [decks, setDecks] = useState([]);
  const [message, setMessage] = useState("");

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
    <div>
      <h2>Select a Deck to Edit</h2>
      {message && <p>{message}</p>}
      <ul>
        {decks.map((deck) => (
          <li key={deck.id}>
            {deck.name} 
            <Link to={`/edit_deck/${deck.id}`}>
              <button>Edit</button>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DeckList;
