import React, { useState, useEffect } from 'react';

const TranslationToggle = () => {
  const [currentLanguage, setCurrentLanguage] = useState('en');
  const [isTranslating, setIsTranslating] = useState(false);
  const [translationError, setTranslationError] = useState(null);

  // Check for saved language preference in localStorage
  useEffect(() => {
    const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
    setCurrentLanguage(savedLanguage);
  }, []);

  const toggleLanguage = async () => {
    setIsTranslating(true);
    setTranslationError(null);
    
    try {
      // In a real application, this would call the translation API
      // For this example, we'll just toggle between languages
      const newLanguage = currentLanguage === 'en' ? 'ur' : 'en';
      
      // Save the new language preference
      localStorage.setItem('preferredLanguage', newLanguage);
      setCurrentLanguage(newLanguage);
      
      // In a real app, we would fetch translated content here
      console.log(`Switching to ${newLanguage} content`);
      
      // Simulate API call delay
      await new Promise(resolve => setTimeout(resolve, 300));
      
      // In a real implementation, we would update the content here
      // This could involve re-rendering components with translated content
      document.dispatchEvent(new CustomEvent('languageChanged', { detail: { newLanguage } }));
    } catch (error) {
      setTranslationError('Failed to translate content. Please try again.');
      console.error('Translation error:', error);
    } finally {
      setIsTranslating(false);
    }
  };

  // In a real implementation, we would use actual translated text
  // For now, we'll just show the current language in the button
  const buttonText = currentLanguage === 'en' ? ' Urdu' : ' English';
  const currentLangDisplay = currentLanguage === 'en' ? 'EN' : 'UR';

  return (
    <div className="translation-toggle-container">
      <button 
        className={`translation-toggle-btn ${isTranslating ? 'loading' : ''}`}
        onClick={toggleLanguage}
        disabled={isTranslating}
        title={`Translate to ${buttonText}`}
      >
        {isTranslating ? (
          <span className="loading-text">Translating...</span>
        ) : (
          <span className="lang-indicator">
            <span className="current-lang">{currentLangDisplay}</span>
            <span className="switch-indicator">⇄</span>
            <span className="target-lang">{currentLanguage === 'en' ? 'UR' : 'EN'}</span>
          </span>
        )}
      </button>

      {translationError && (
        <div className="translation-error">
          {translationError}
        </div>
      )}

      <style jsx>{`
        .translation-toggle-container {
          display: inline-block;
          position: relative;
        }

        .translation-toggle-btn {
          background-color: #2196F3;
          color: white;
          padding: 8px 16px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 14px;
          display: flex;
          align-items: center;
          gap: 8px;
        }

        .translation-toggle-btn:hover:not(:disabled) {
          background-color: #0b7dda;
        }

        .translation-toggle-btn:disabled {
          opacity: 0.6;
          cursor: not-allowed;
        }

        .loading-text {
          display: flex;
          align-items: center;
        }

        .lang-indicator {
          display: flex;
          align-items: center;
          gap: 4px;
        }

        .switch-indicator {
          font-weight: bold;
        }

        .translation-error {
          color: #f44336;
          font-size: 12px;
          margin-top: 5px;
          padding: 5px;
          background-color: #ffebee;
          border-radius: 3px;
        }
      `}</style>
    </div>
  );
};

export default TranslationToggle;