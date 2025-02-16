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

  const handleDeckDelete = async (deckId) => {
    try {
      const response = await fetch(`${backendUrl}/delete_deck/${deckId}`, {
        method: "DELETE",        
      });

      if (response.ok) {
        setDecks(decks.filter((deck) => deck.id !== deckId));
      } else {
        setMessage("Failed to delete deck.")
      }
    } catch (error) {
      setMessage("Failed to connect to backend.")
    }
  }

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
            <button type="button" onClick={() => handleDeckDelete(deck.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DeckList;
