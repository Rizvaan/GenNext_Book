import React, { useState, useEffect } from 'react';
import './PersonalizationButton.css';

const PersonalizationButton = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [userProfile, setUserProfile] = useState({
    softwareExperience: 'intermediate',
    hardwareExperience: 'basic',
    roboticsExposure: 'none',
    preferredLanguage: 'en',
    learningPace: 'moderate'
  });

  // Load user profile from localStorage or API
  useEffect(() => {
    const savedProfile = localStorage.getItem('userProfile');
    if (savedProfile) {
      setUserProfile(JSON.parse(savedProfile));
    }
  }, []);

  // Save user profile to localStorage
  const saveProfile = (updatedProfile) => {
    localStorage.setItem('userProfile', JSON.stringify(updatedProfile));
    setUserProfile(updatedProfile);
  };

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  const handleProfileChange = (field, value) => {
    const updatedProfile = { ...userProfile, [field]: value };
    saveProfile(updatedProfile);
  };

  // Apply personalization to content based on user profile
  const applyPersonalization = (content) => {
    // This would typically involve calling an API or updating content based on profile
    console.log('Applying personalization for:', userProfile);
    return content; // Placeholder - would be transformed based on user profile
  };

  return (
    <div className="personalization-container">
      <button 
        className="personalization-btn" 
        onClick={toggleDropdown}
        aria-label="Personalize content"
      >
        <span className="icon">👤</span>
        Personalize
      </button>
      
      {isOpen && (
        <div className="personalization-dropdown">
          <div className="personalization-form">
            <div className="form-group">
              <label htmlFor="software-exp">Software Experience:</label>
              <select
                id="software-exp"
                value={userProfile.softwareExperience}
                onChange={(e) => handleProfileChange('softwareExperience', e.target.value)}
              >
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>
            
            <div className="form-group">
              <label htmlFor="hardware-exp">Hardware Experience:</label>
              <select
                id="hardware-exp"
                value={userProfile.hardwareExperience}
                onChange={(e) => handleProfileChange('hardwareExperience', e.target.value)}
              >
                <option value="none">None</option>
                <option value="basic">Basic</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>
            
            <div className="form-group">
              <label htmlFor="robotics-exp">Robotics Exposure:</label>
              <select
                id="robotics-exp"
                value={userProfile.roboticsExposure}
                onChange={(e) => handleProfileChange('roboticsExposure', e.target.value)}
              >
                <option value="none">None</option>
                <option value="basic">Basic</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>
            
            <div className="form-group">
              <label htmlFor="learning-pace">Learning Pace:</label>
              <select
                id="learning-pace"
                value={userProfile.learningPace}
                onChange={(e) => handleProfileChange('learningPace', e.target.value)}
              >
                <option value="slow">Slow</option>
                <option value="moderate">Moderate</option>
                <option value="fast">Fast</option>
              </select>
            </div>
            
            <button 
              className="apply-btn" 
              onClick={toggleDropdown}
            >
              Apply
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default PersonalizationButton;