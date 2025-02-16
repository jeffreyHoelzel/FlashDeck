import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

function Quiz() {
  const { deckId } = useParams(); // Get the deck ID from the URL
  const [flashcards, setFlashcards] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const backendUrl = process.env.BACKEND_URL || "http://localhost:5000";

  // Fetch flashcards when the component loads
  useEffect(() => {
    const fetchFlashcards = async () => {
      try {
        const response = await fetch(`${backendUrl}/quiz_deck/${deckId}`);
        if (response.ok) {
          const data = await response.json();
          setFlashcards(data.flashcards);
        } else {
          setMessage("Error loading quiz.");
        }
      } catch (error) {
        setMessage("Failed to connect to backend.");
      }
    };

    fetchFlashcards();
  }, [deckId]);

  // Handle flipping card
  const handleFlip = () => setShowAnswer(!showAnswer);

  // Handle navigating to the next card
  const handleNext = () => {
    setShowAnswer(false);
    setCurrentIndex((prevIndex) => (prevIndex + 1) % flashcards.length);
  };

  // Handle navigating to the previous card
  const handlePrev = () => {
    setShowAnswer(false);
    setCurrentIndex((prevIndex) => (prevIndex - 1 + flashcards.length) % flashcards.length);
  };

  // Restart Quiz
  const handleRestart = () => {
    setCurrentIndex(0);
    setShowAnswer(false);
  };

  // Go back to deck selection
  const handleGoBack = () => navigate("/select_quiz");

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>Quiz Mode</h2>
      {message && <p>{message}</p>}
      
      {flashcards.length > 0 ? (
        <div>
          <h3>Flashcard {currentIndex + 1} of {flashcards.length}</h3>

          {/* Flashcard display */}
          <div 
            onClick={handleFlip} 
            style={{
              cursor: "pointer",
              padding: "40px",
              border: "2px solid black",
              borderRadius: "10px",
              textAlign: "center",
              width: "300px",
              margin: "20px auto",
              backgroundColor: "#f9f9f9",
              fontSize: "1.2rem",
              color: "black"
            }}
          >
            {showAnswer ? flashcards[currentIndex].answer : flashcards[currentIndex].question}
          </div>

          {/* Navigation Buttons */}
          <button onClick={handlePrev} disabled={currentIndex === 0} style={{ marginRight: "10px" }}>
            Previous
          </button>
          <button onClick={handleNext} style={{ marginRight: "10px" }}>
            Next
          </button>

          <button onClick={handleRestart} style={{ marginRight: "10px" }}>
            Restart Quiz
          </button>

          <button onClick={handleGoBack}>
            Go Back
          </button>
        </div>
      ) : (
        <p>No flashcards available.</p>
      )}
    </div>
  );
}

export default Quiz;
