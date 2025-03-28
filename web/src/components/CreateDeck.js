import React, { useState } from "react";
import "../styles/createdeck.css";

function CreateDeckForm() {
  const [deckName, setDeckName] = useState("");
  const [cards, setCards] = useState([{ question: "", answer: "" }]);
  const [message, setMessage] = useState("");

  const handleDeckNameChange = (e) => setDeckName(e.target.value);

  const handleCardChange = (index, field, value) => {
    const updatedCards = [...cards];
    updatedCards[index][field] = value;
    setCards(updatedCards);
  };

  const handleAddCard = () => setCards([...cards, { question: "", answer: "" }]);

  const handleRemoveCard = (index) => {
    const updatedCards = cards.filter((_, i) => i !== index);
    setCards(updatedCards);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const backendUrl = process.env.REACT_APP_API_GATEWAY_URL || "http://localhost:8000";
    const url = `${backendUrl}/api/deck/create_new_deck`;

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: deckName, cards }),
      });

      if (response.ok) {
        const data = await response.json();
        setMessage(`Deck created successfully!`);
        setDeckName("");
        setCards([{ question: "", answer: "" }]);
      } else {
        const errorData = await response.json();
        setMessage(`Error: ${errorData.error}`);
      }
    } catch (error) {
      setMessage("An error occurred while creating the deck.");
    }
  };

  return (
    <div className="form-container">
      <h2>Create a New Deck</h2>
      <form onSubmit={handleSubmit}>
        <input
          className="deck-name-input"
          type="text"
          placeholder="Enter deck name"
          value={deckName}
          onChange={handleDeckNameChange}
          required
        />

        <h3>Flashcards:</h3>
        {cards.map((card, index) => (
          <div key={index} className="card-info-container">
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

        <button type="submit">Create Deck</button>
      </form>

      {message && <p className="result-message">{message}</p>}
    </div>
  );
}

export default CreateDeckForm;
