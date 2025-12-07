import React, { useState, useEffect } from 'react';
import './TranslationToggle.css';

const TranslationToggle = () => {
  const [currentLanguage, setCurrentLanguage] = useState('en');
  const [availableLanguages, setAvailableLanguages] = useState([
    { code: 'en', name: 'English' },
    { code: 'ur-PK', name: 'Urdu' }
  ]);

  // Load user's preferred language from localStorage
  useEffect(() => {
    const savedLanguage = localStorage.getItem('preferredLanguage');
    if (savedLanguage && availableLanguages.some(lang => lang.code === savedLanguage)) {
      setCurrentLanguage(savedLanguage);
    } else {
      // Set default language (English)
      setCurrentLanguage('en');
    }
  }, []);

  // Save user's language preference
  const setLanguage = (languageCode) => {
    localStorage.setItem('preferredLanguage', languageCode);
    setCurrentLanguage(languageCode);
    
    // Apply the language to the content
    applyLanguage(languageCode);
  };

  // Apply the selected language to the content
  const applyLanguage = async (languageCode) => {
    try {
      // This would typically call an API to get translated content
      console.log(`Applying language: ${languageCode}`);
      
      // Example logic: update the content based on selected language
      // In a real implementation, this might fetch translated content from an API
      document.documentElement.lang = languageCode;
      
      // Update language attribute and notify the app
      window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: languageCode } }));
    } catch (error) {
      console.error('Error applying language:', error);
    }
  };

  return (
    <div className="translation-toggle-container">
      <div className="translation-dropdown">
        <select
          value={currentLanguage}
          onChange={(e) => setLanguage(e.target.value)}
          className="language-selector"
          aria-label="Select language"
        >
          {availableLanguages.map((language) => (
            <option key={language.code} value={language.code}>
              {language.name}
            </option>
          ))}
        </select>
        <span className="dropdown-icon">▼</span>
      </div>
    </div>
  );
};

export default TranslationToggle;