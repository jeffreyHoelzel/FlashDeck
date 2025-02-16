import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function EditDeckForm() {
  const { deckId } = useParams();
  const [deckName, setDeckName] = useState("");
  const [cards, setCards] = useState([]);
  const [message, setMessage] = useState("");

  const backendUrl = process.env.BACKEND_URL || "http://localhost:5000";

  // Fetch existing deck details
  useEffect(() => {
    const fetchDeck = async () => {
      try {
        const response = await fetch(`${backendUrl}/get_deck/${deckId}`);
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

  // Handle deck name change
  const handleDeckNameChange = (e) => setDeckName(e.target.value);

  // Handle card input changes
  const handleCardChange = (index, field, value) => {
    const updatedCards = [...cards];
    updatedCards[index][field] = value;
    setCards(updatedCards);
  };

  // Add a new flashcard
  const handleAddCard = () => {
    setCards([...cards, { question: "", answer: "" }]);
  };

  // Remove a flashcard
  const handleRemoveCard = (index) => {
    const updatedCards = cards.filter((_, i) => i !== index);
    setCards(updatedCards);
  };

  // Submit the updated deck
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${backendUrl}/edit_existing_deck/${deckId}`, {
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
    <div>
      <h2>Edit Deck</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={deckName}
          onChange={handleDeckNameChange}
          required
          placeholder="Deck Name"
        />

        <h3>Flashcards:</h3>
        {cards.map((card, index) => (
          <div key={index} style={{ marginBottom: "1rem" }}>
            <input
              type="text"
              placeholder={`Question ${index + 1}`}
              value={card.question}
              onChange={(e) => handleCardChange(index, "question", e.target.value)}
              required
            />
            <input
              type="text"
              placeholder={`Answer ${index + 1}`}
              value={card.answer}
              onChange={(e) => handleCardChange(index, "answer", e.target.value)}
              required
            />
            <button type="button" onClick={() => handleRemoveCard(index)}>
              Remove Card
            </button>
          </div>
        ))}

        <button type="button" onClick={handleAddCard}>
          Add Another Card
        </button>

        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
}

export default EditDeckForm;
