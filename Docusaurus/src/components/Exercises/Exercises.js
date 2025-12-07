import React, { useState } from 'react';

const Exercises = ({ exercises = [] }) => {
  const [currentExercise, setCurrentExercise] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [showFeedback, setShowFeedback] = useState(false);
  const [completed, setCompleted] = useState(false);

  // Default exercises if none provided
  const defaultExercises = [
    {
      id: 1,
      type: "multiple-choice",
      question: "What is the primary function of ROS (Robot Operating System)?",
      options: [
        "Real-time operating system for robots",
        "Middleware for robot software development",
        "Hardware controller for robotic systems",
        "Simulation environment for robots"
      ],
      correctAnswer: 1,
      explanation: "ROS is a middleware that provides services designed for a heterogeneous computer cluster, including hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, etc."
    },
    {
      id: 2,
      type: "true-false",
      question: "In ROS 2, nodes communicate with each other using topics, services, and actions.",
      correctAnswer: true,
      explanation: "This is correct. ROS 2 nodes use topics for asynchronous communication, services for synchronous request/response communication, and actions for goal-oriented communication."
    },
    {
      id: 3,
      type: "short-answer",
      question: "What does URDF stand for in the context of robotics?",
      correctAnswer: "Unified Robot Description Format",
      explanation: "URDF (Unified Robot Description Format) is an XML format for representing a robot model. URDF is not a complete description for a robot, as it only describes the physical and kinematic properties of a robot."
    }
  ];

  const exercisesToUse = exercises.length > 0 ? exercises : defaultExercises;
  const currentEx = exercisesToUse[currentExercise];

  const handleAnswerChange = (value) => {
    setUserAnswers({
      ...userAnswers,
      [currentEx.id]: value
    });
  };

  const handleSubmit = () => {
    setShowFeedback(true);
  };

  const handleNext = () => {
    if (currentExercise < exercisesToUse.length - 1) {
      setCurrentExercise(currentExercise + 1);
      setShowFeedback(false);
    } else {
      setCompleted(true);
    }
  };

  const handleReset = () => {
    setCurrentExercise(0);
    setUserAnswers({});
    setShowFeedback(false);
    setCompleted(false);
  };

  const getFeedback = () => {
    if (!showFeedback) return null;
    
    const userAnswer = userAnswers[currentEx.id];
    const isCorrect = currentEx.type === "multiple-choice" 
      ? userAnswer === currentEx.correctAnswer 
      : currentEx.type === "true-false"
        ? userAnswer === currentEx.correctAnswer
        : userAnswer && userAnswer.toLowerCase().includes(currentEx.correctAnswer.toLowerCase());
    
    return (
      <div className={`feedback ${isCorrect ? 'correct' : 'incorrect'}`}>
        <p><strong>{isCorrect ? '✓ Correct!' : '✗ Incorrect'}</strong></p>
        <p>{currentEx.explanation}</p>
      </div>
    );
  };

  if (completed) {
    return (
      <div className="exercises-container">
        <div className="exercises-header">
          <h3>Exercise Completed!</h3>
        </div>
        <div className="exercises-content">
          <p>Congratulations! You've completed all exercises for this chapter.</p>
          <p>You scored {exercisesToUse.filter((ex, idx) => {
            const userAnswer = userAnswers[ex.id];
            return ex.type === "multiple-choice" 
              ? userAnswer === ex.correctAnswer 
              : ex.type === "true-false"
                ? userAnswer === ex.correctAnswer
                : userAnswer && userAnswer.toLowerCase().includes(ex.correctAnswer.toLowerCase());
          }).length} out of {exercisesToUse.length} correct.</p>
          <button onClick={handleReset}>Restart Exercises</button>
        </div>
        
        <style jsx>{`
          .exercises-container {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
          }
          
          .exercises-header h3 {
            color: #4CAF50;
            margin-top: 0;
          }
          
          .exercises-content {
            text-align: center;
          }
          
          button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 16px;
          }
          
          button:hover {
            background-color: #45a049;
          }
        `}</style>
      </div>
    );
  }

  return (
    <div className="exercises-container">
      <div className="exercises-header">
        <h3>Chapter Exercises</h3>
        <div className="exercise-progress">
          Exercise {currentExercise + 1} of {exercisesToUse.length}
        </div>
      </div>
      
      <div className="exercises-content">
        <div className="exercise-question">
          <h4>{currentEx.question}</h4>
          
          {currentEx.type === "multiple-choice" && (
            <div className="options">
              {currentEx.options.map((option, idx) => (
                <div key={idx} className="option">
                  <input
                    type="radio"
                    id={`option-${idx}`}
                    name={`exercise-${currentEx.id}`}
                    value={idx}
                    checked={userAnswers[currentEx.id] == idx}
                    onChange={() => handleAnswerChange(idx)}
                  />
                  <label htmlFor={`option-${idx}`}>{option}</label>
                </div>
              ))}
            </div>
          )}
          
          {currentEx.type === "true-false" && (
            <div className="options">
              <div className="option">
                <input
                  type="radio"
                  id="true"
                  name={`exercise-${currentEx.id}`}
                  value="true"
                  checked={userAnswers[currentEx.id] === true}
                  onChange={() => handleAnswerChange(true)}
                />
                <label htmlFor="true">True</label>
              </div>
              <div className="option">
                <input
                  type="radio"
                  id="false"
                  name={`exercise-${currentEx.id}`}
                  value="false"
                  checked={userAnswers[currentEx.id] === false}
                  onChange={() => handleAnswerChange(false)}
                />
                <label htmlFor="false">False</label>
              </div>
            </div>
          )}
          
          {currentEx.type === "short-answer" && (
            <div className="answer-input">
              <textarea
                value={userAnswers[currentEx.id] || ''}
                onChange={(e) => handleAnswerChange(e.target.value)}
                placeholder="Type your answer here..."
                rows="3"
              />
            </div>
          )}
        </div>
        
        {getFeedback()}
        
        <div className="exercise-actions">
          {!showFeedback ? (
            <button onClick={handleSubmit} disabled={userAnswers[currentEx.id] === undefined}>
              Submit Answer
            </button>
          ) : (
            <button onClick={handleNext}>
              {currentExercise < exercisesToUse.length - 1 ? 'Next Question' : 'Finish'}
            </button>
          )}
        </div>
      </div>
      
      <style jsx>{`
        .exercises-container {
          border: 1px solid #ddd;
          border-radius: 8px;
          padding: 16px;
          font-family: Arial, sans-serif;
          background-color: #f9f9f9;
        }
        
        .exercises-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 16px;
        }
        
        .exercises-header h3 {
          margin: 0;
          color: #333;
        }
        
        .exercise-progress {
          font-size: 14px;
          color: #666;
        }
        
        .exercises-content {
          display: flex;
          flex-direction: column;
          gap: 16px;
        }
        
        .exercise-question h4 {
          margin-top: 0;
        }
        
        .options {
          display: flex;
          flex-direction: column;
          gap: 8px;
        }
        
        .option {
          display: flex;
          align-items: center;
          gap: 8px;
        }
        
        .answer-input textarea {
          width: 100%;
          padding: 8px;
          border: 1px solid #ddd;
          border-radius: 4px;
          font-size: 14px;
        }
        
        .feedback {
          padding: 12px;
          border-radius: 4px;
          margin-top: 12px;
        }
        
        .feedback.correct {
          background-color: #e8f5e9;
          border: 1px solid #4CAF50;
          color: #2e7d32;
        }
        
        .feedback.incorrect {
          background-color: #ffebee;
          border: 1px solid #f44336;
          color: #c62828;
        }
        
        .exercise-actions {
          display: flex;
          justify-content: center;
        }
        
        button {
          background-color: #4CAF50;
          color: white;
          padding: 10px 20px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }
        
        button:hover:not(:disabled) {
          background-color: #45a049;
        }
        
        button:disabled {
          background-color: #cccccc;
          cursor: not-allowed;
        }
        
        label {
          cursor: pointer;
        }
      `}</style>
    </div>
  );
};

export default Exercises;