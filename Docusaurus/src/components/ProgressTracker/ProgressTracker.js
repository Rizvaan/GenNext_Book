import React, { useState, useEffect } from 'react';

const ProgressTracker = ({ moduleId, chapterId, userId }) => {
  const [progress, setProgress] = useState({
    moduleId: moduleId,
    chapterId: chapterId,
    completed: false,
    completionPercentage: 0,
    timeSpent: 0
  });
  const [isSaving, setIsSaving] = useState(false);

  // Simulate loading progress from an API
  useEffect(() => {
    // In a real app, this would fetch the user's progress from the backend
    const savedProgress = localStorage.getItem(`progress_${userId}_${chapterId}`);
    if (savedProgress) {
      setProgress(JSON.parse(savedProgress));
    }
  }, [userId, chapterId]);

  const updateProgress = (newPercentage) => {
    if (newPercentage < 0) newPercentage = 0;
    if (newPercentage > 100) newPercentage = 100;
    
    const updatedProgress = {
      ...progress,
      completionPercentage: newPercentage,
      completed: newPercentage === 100
    };
    
    setProgress(updatedProgress);
    
    // Save to localStorage (in a real app, this would go to the backend)
    localStorage.setItem(`progress_${userId}_${chapterId}`, JSON.stringify(updatedProgress));
  };

  const incrementProgress = (amount = 10) => {
    updateProgress(progress.completionPercentage + amount);
  };

  const toggleCompletion = () => {
    const newCompletion = !progress.completed;
    const newPercentage = newCompletion ? 100 : 0;
    
    updateProgress(newPercentage);
  };

  return (
    <div className="progress-tracker-container">
      <div className="progress-header">
        <h3>Your Progress</h3>
      </div>
      
      <div className="progress-content">
        <div className="progress-bar-container">
          <div className="progress-info">
            <span>Chapter Progress: {progress.completionPercentage}%</span>
            <span className={`completion-status ${progress.completed ? 'completed' : 'incomplete'}`}>
              {progress.completed ? '✓ Completed' : '○ In Progress'}
            </span>
          </div>
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${progress.completionPercentage}%` }}
            ></div>
          </div>
        </div>
        
        <div className="progress-actions">
          <button onClick={() => updateProgress(25)}>1/4 Done</button>
          <button onClick={() => updateProgress(50)}>1/2 Done</button>
          <button onClick={() => updateProgress(75)}>3/4 Done</button>
          <button onClick={toggleCompletion} className="complete-btn">
            {progress.completed ? 'Mark Incomplete' : 'Mark Complete'}
          </button>
        </div>
        
        <div className="progress-stats">
          <div className="stat">
            <strong>Time spent:</strong> {Math.floor(progress.timeSpent / 60)} min {progress.timeSpent % 60} sec
          </div>
          <div className="stat">
            <strong>Module:</strong> {moduleId}
          </div>
          <div className="stat">
            <strong>Chapter:</strong> {chapterId}
          </div>
        </div>
      </div>
      
      <style jsx>{`
        .progress-tracker-container {
          border: 1px solid #ddd;
          border-radius: 8px;
          padding: 16px;
          font-family: Arial, sans-serif;
          background-color: #f9f9f9;
          max-width: 100%;
        }
        
        .progress-header {
          margin-bottom: 16px;
        }
        
        .progress-header h3 {
          margin: 0;
          color: #333;
        }
        
        .progress-content {
          display: flex;
          flex-direction: column;
          gap: 16px;
        }
        
        .progress-bar-container {
          width: 100%;
        }
        
        .progress-info {
          display: flex;
          justify-content: space-between;
          margin-bottom: 8px;
          font-size: 14px;
        }
        
        .completion-status {
          font-weight: bold;
        }
        
        .completion-status.completed {
          color: #4CAF50;
        }
        
        .completion-status.incomplete {
          color: #FF9800;
        }
        
        .progress-bar {
          width: 100%;
          height: 20px;
          background-color: #e0e0e0;
          border-radius: 10px;
          overflow: hidden;
        }
        
        .progress-fill {
          height: 100%;
          background-color: #4CAF50;
          transition: width 0.3s ease;
        }
        
        .progress-actions {
          display: flex;
          flex-wrap: wrap;
          gap: 8px;
        }
        
        .progress-actions button {
          padding: 6px 12px;
          border: 1px solid #4CAF50;
          background-color: white;
          color: #4CAF50;
          border-radius: 4px;
          cursor: pointer;
          font-size: 12px;
        }
        
        .progress-actions button:hover {
          background-color: #e8f5e9;
        }
        
        .progress-actions button.complete-btn {
          background-color: #4CAF50;
          color: white;
        }
        
        .progress-actions button.complete-btn:hover {
          background-color: #45a049;
        }
        
        .progress-stats {
          display: flex;
          flex-direction: column;
          gap: 8px;
          font-size: 13px;
        }
        
        .stat {
          padding: 4px 0;
        }
      `}</style>
    </div>
  );
};

export default ProgressTracker;