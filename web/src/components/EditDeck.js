import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import "../styles/editdeck.css";

function EditDeckForm() {
  const { deckId } = useParams();
  const [deckName, setDeckName] = useState("");
  const [cards, setCards] = useState([]);
  const [message, setMessage] = useState("");

  const backendUrl = process.env.REACT_APP_API_GATEWAY_URL || "http://api-gateway:8000";

  useEffect(() => {
    const fetchDeck = async () => {
      try {
        const response = await fetch(`${backendUrl}/api/get_deck/${deckId}`);
        if (response.ok) {
          const data = await response.json();
          setDeckName(data.name);
          setCards(data.cards);
        } else {
          setMessage("Error loading deck.");
        }
      } catch (error) {
        setMessage("Failed to connect to backend.");
      }
    };

    fetchDeck();
  }, [deckId]);

  const handleDeckNameChange = (e) => setDeckName(e.target.value);

  const handleCardChange = (index, field, value) => {
    const updatedCards = [...cards];
    updatedCards[index][field] = value;
    setCards(updatedCards);
  };

  const handleAddCard = () => {
    setCards([...cards, { question: "", answer: "" }]);
  };

  const handleRemoveCard = (index) => {
    const updatedCards = cards.filter((_, i) => i !== index);
    setCards(updatedCards);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${backendUrl}/api/edit_existing_deck/${deckId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: deckName, cards }),
      });

      if (response.ok) {
        setMessage("Deck updated successfully!");
      } else {
        const errorData = await response.json();
        setMessage(`Error: ${errorData.error}`);
      }
    } catch (error) {
      setMessage("An error occurred while updating the deck.");
    }
  };

  return (
    <div className="edit-deck-container">
      <h2>Edit Deck</h2>
      {message && <p className="result-message">{message}</p>}
      <form onSubmit={handleSubmit}>
        <input
          className="edit-input"
          type="text"
          value={deckName}
          onChange={handleDeckNameChange}
          required
          placeholder="Deck Name"
        />

        <h3>Flashcards:</h3>
        {cards.map((card, index) => (
          <div className="second-input-container" key={index} style={{ marginBottom: "1rem" }}>
            <input
              className="edit-input"
              type="text"
              placeholder={`Question ${index + 1}`}
              value={card.question}
              onChange={(e) => handleCardChange(index, "question", e.target.value)}
              required
            />
            <input
              className="edit-input"
              type="text"
              placeholder={`Answer ${index + 1}`}
              value={card.answer}
              onChange={(e) => handleCardChange(index, "answer", e.target.value)}
              required
            />
            <button className="edit-button" type="button" onClick={() => handleRemoveCard(index)}>
              Remove Card
            </button>
          </div>
        ))}

        <button className="edit-button" type="button" onClick={handleAddCard}>
          Add Another Card
        </button>

        <button className="edit-button" type="submit">Save Changes</button>
      </form>
    </div>
  );
}

export default EditDeckForm;
