import React, { useState, useEffect } from 'react';

const PersonalizationButton = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [userProfile, setUserProfile] = useState({
    skill_level: 'beginner',
    background: '',
    learning_preferences: '',
    preferred_language: 'en'
  });

  // Load user profile from localStorage or API
  useEffect(() => {
    const savedProfile = localStorage.getItem('userProfile');
    if (savedProfile) {
      setUserProfile(JSON.parse(savedProfile));
    }
  }, []);

  const handleSaveProfile = () => {
    // Save to localStorage (in a real app, this would be sent to an API)
    localStorage.setItem('userProfile', JSON.stringify(userProfile));
    setIsModalOpen(false);
    // Refresh the page or update content based on new profile
    window.location.reload();
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserProfile(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="personalization-container">
      <button 
        className="personalization-btn"
        onClick={() => setIsModalOpen(true)}
        title="Personalize your learning experience"
      >
        🎯 Personalize
      </button>

      {isModalOpen && (
        <div className="personalization-modal">
          <div className="modal-content">
            <h3>Personalize Your Learning</h3>
            <button 
              className="close-btn" 
              onClick={() => setIsModalOpen(false)}
            >
              &times;
            </button>
            
            <div className="form-group">
              <label htmlFor="skill_level">Skill Level:</label>
              <select
                id="skill_level"
                name="skill_level"
                value={userProfile.skill_level}
                onChange={handleChange}
              >
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>
            
            <div className="form-group">
              <label htmlFor="background">Background:</label>
              <select
                id="background"
                name="background"
                value={userProfile.background}
                onChange={handleChange}
              >
                <option value="">Select your background</option>
                <option value="software_engineer">Software Engineer</option>
                <option value="mechanical_engineer">Mechanical Engineer</option>
                <option value="electrical_engineer">Electrical Engineer</option>
                <option value="student">Student</option>
                <option value="hobbyist">Hobbyist</option>
                <option value="other">Other</option>
              </select>
            </div>
            
            <div className="form-group">
              <label htmlFor="learning_preferences">Learning Preferences:</label>
              <textarea
                id="learning_preferences"
                name="learning_preferences"
                value={userProfile.learning_preferences}
                onChange={handleChange}
                placeholder="e.g., Visual learner, Prefer hands-on examples..."
                rows="3"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="preferred_language">Preferred Language:</label>
              <select
                id="preferred_language"
                name="preferred_language"
                value={userProfile.preferred_language}
                onChange={handleChange}
              >
                <option value="en">English</option>
                <option value="ur">Urdu</option>
              </select>
            </div>
            
            <button 
              className="save-btn" 
              onClick={handleSaveProfile}
            >
              Save Preferences
            </button>
          </div>
        </div>
      )}
      
      <style jsx>{`
        .personalization-container {
          position: relative;
          display: inline-block;
        }
        
        .personalization-btn {
          background-color: #4CAF50;
          color: white;
          padding: 8px 16px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 14px;
        }
        
        .personalization-btn:hover {
          background-color: #45a049;
        }
        
        .personalization-modal {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background-color: rgba(0, 0, 0, 0.5);
          display: flex;
          justify-content: center;
          align-items: center;
          z-index: 1000;
        }
        
        .modal-content {
          background-color: white;
          padding: 20px;
          border-radius: 8px;
          width: 90%;
          max-width: 500px;
          position: relative;
          max-height: 90vh;
          overflow-y: auto;
        }
        
        .close-btn {
          position: absolute;
          top: 10px;
          right: 15px;
          font-size: 24px;
          background: none;
          border: none;
          cursor: pointer;
        }
        
        h3 {
          margin-top: 0;
          margin-bottom: 20px;
        }
        
        .form-group {
          margin-bottom: 15px;
        }
        
        label {
          display: block;
          margin-bottom: 5px;
          font-weight: bold;
        }
        
        select, textarea {
          width: 100%;
          padding: 8px;
          border: 1px solid #ccc;
          border-radius: 4px;
          box-sizing: border-box;
        }
        
        .save-btn {
          background-color: #4CAF50;
          color: white;
          padding: 10px 20px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          width: 100%;
        }
        
        .save-btn:hover {
          background-color: #45a049;
        }
      `}</style>
    </div>
  );
};

export default PersonalizationButton;