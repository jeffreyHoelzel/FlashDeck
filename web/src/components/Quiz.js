import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import "../styles/quiz.css";

function Quiz() {
  const { deckId } = useParams();
  const [flashcards, setFlashcards] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const backendUrl = process.env.REACT_APP_API_GATEWAY_URL || "http://localhost:8000";

  useEffect(() => {
    const fetchFlashcards = async () => {
      try {
        const response = await fetch(`${backendUrl}/api/quiz/quiz_deck/${deckId}`);
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

  const handleFlip = () => setShowAnswer(!showAnswer);

  const handleNext = () => {
    setShowAnswer(false);
    setCurrentIndex((prevIndex) => (prevIndex + 1) % flashcards.length);
  };

  const handlePrev = () => {
    setShowAnswer(false);
    setCurrentIndex((prevIndex) => (prevIndex - 1 + flashcards.length) % flashcards.length);
  };

  const handleRestart = () => {
    setCurrentIndex(0);
    setShowAnswer(false);
  };

  const handleGoBack = () => navigate("/quiz_deck");

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>Quiz Mode</h2>
      {message && <p>{message}</p>}
      
      {flashcards.length > 0 ? (
        <div>
          <h3>Flashcard {currentIndex + 1} of {flashcards.length}</h3>

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

          <button className="selector" onClick={handlePrev} disabled={currentIndex === 0} style={{ marginRight: "10px" }}>
            Previous
          </button>
          <button className="selector" onClick={handleNext} style={{ marginRight: "10px" }}>
            Next
          </button>

          <button className="selector" onClick={handleRestart} style={{ marginRight: "10px" }}>
            Restart Quiz
          </button>

          <button className="selector" onClick={handleGoBack}>
            Go Back
          </button>
        </div>
      ) : (
        <p className="result-message">No flashcards available.</p>
      )}
    </div>
  );
}

export default Quiz;
