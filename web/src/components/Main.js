import React from "react";

const Main = () => {
  const directCreateDeck = () => {
    window.location.href = "/create_new_deck";
  }

  const directEditDeck = () => {
    window.location.href = "/edit_existing_deck";
  }

  const directQuiz = () => {
    window.location.href = "/quiz_deck";
  }

  return (
    <main>
      <div className="main-container">
        <h1>FlashDeck</h1>
        <p>Free online flash card and deck maker.</p>
      </div>
      <div className="options-container">
        <div className="option">
          <button onClick={directCreateDeck}>Create Deck</button>
        </div>
        <div className="option">
          <button onClick={directEditDeck}>Edit Deck</button>
        </div>
        <div className="option">
          <button onClick={directQuiz}>Start Quiz</button>
        </div>
      </div>
    </main>
  );
}

export default Main;
