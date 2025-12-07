import React, { useState, useRef, useEffect } from 'react';

const QABot = ({ chapterContent = "" }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage = { id: Date.now(), text: inputValue, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // In a real implementation, this would call the backend QA API
      // Simulating API call with a timeout
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Mock response - in a real app this would come from the backend
      const botResponse = { 
        id: Date.now() + 1, 
        text: `This is a simulated response to: "${inputValue}". In a real implementation, this would connect to the AI Q&A backend to answer questions about the textbook content.`, 
        sender: 'bot' 
      };
      
      setMessages(prev => [...prev, botResponse]);
    } catch (error) {
      const errorMessage = { 
        id: Date.now() + 1, 
        text: 'Sorry, I encountered an error processing your question. Please try again.', 
        sender: 'bot' 
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div className={`qa-bot-container ${isExpanded ? 'expanded' : 'collapsed'}`}>
      <div className="qa-bot-header" onClick={toggleExpand}>
        <h3>📚 Textbook Assistant</h3>
        <span className="toggle-icon">{isExpanded ? '−' : '+'}</span>
      </div>
      
      {isExpanded && (
        <div className="qa-bot-content">
          <div className="messages-container">
            {messages.length === 0 ? (
              <div className="welcome-message">
                <p>Ask me anything about this chapter!</p>
                <p>I can help explain concepts, provide examples, or clarify any doubts.</p>
              </div>
            ) : (
              <div className="messages">
                {messages.map((msg) => (
                  <div key={msg.id} className={`message ${msg.sender}`}>
                    <div className="message-text">{msg.text}</div>
                  </div>
                ))}
                {isLoading && (
                  <div className="message bot">
                    <div className="message-text typing-indicator">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                )}
                <div ref={messagesEndRef} />
              </div>
            )}
          </div>
          
          <form onSubmit={handleSubmit} className="input-form">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask a question about this chapter..."
              disabled={isLoading}
            />
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Sending...' : '→'}
            </button>
          </form>
        </div>
      )}
      
      <style jsx>{`
        .qa-bot-container {
          border: 1px solid #ddd;
          border-radius: 8px;
          overflow: hidden;
          font-family: Arial, sans-serif;
          max-width: 100%;
          box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .qa-bot-header {
          background-color: #4CAF50;
          color: white;
          padding: 12px 16px;
          cursor: pointer;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        
        .qa-bot-header h3 {
          margin: 0;
          font-size: 16px;
        }
        
        .toggle-icon {
          font-size: 20px;
          font-weight: bold;
        }
        
        .qa-bot-content {
          background-color: #f9f9f9;
          padding: 16px;
        }
        
        .messages-container {
          max-height: 300px;
          overflow-y: auto;
          margin-bottom: 16px;
          border: 1px solid #eee;
          border-radius: 4px;
          padding: 12px;
          background-color: white;
        }
        
        .welcome-message {
          color: #666;
          font-style: italic;
          text-align: center;
          padding: 20px;
        }
        
        .message {
          margin-bottom: 12px;
          padding: 8px 12px;
          border-radius: 8px;
          max-width: 80%;
        }
        
        .user {
          background-color: #e3f2fd;
          margin-left: auto;
          text-align: right;
        }
        
        .bot {
          background-color: #f5f5f5;
          margin-right: auto;
        }
        
        .typing-indicator {
          display: flex;
          align-items: center;
        }
        
        .typing-indicator span {
          height: 8px;
          width: 8px;
          background-color: #999;
          border-radius: 50%;
          display: inline-block;
          margin: 0 2px;
          animation: typing 1.4s infinite ease-in-out;
        }
        
        .typing-indicator span:nth-child(2) {
          animation-delay: 0.2s;
        }
        
        .typing-indicator span:nth-child(3) {
          animation-delay: 0.4s;
        }
        
        @keyframes typing {
          0%, 60%, 100% { transform: translateY(0); }
          30% { transform: translateY(-5px); }
        }
        
        .input-form {
          display: flex;
          gap: 8px;
        }
        
        .input-form input {
          flex: 1;
          padding: 10px;
          border: 1px solid #ddd;
          border-radius: 4px;
          font-size: 14px;
        }
        
        .input-form button {
          padding: 10px 15px;
          background-color: #4CAF50;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }
        
        .input-form button:disabled {
          background-color: #cccccc;
          cursor: not-allowed;
        }
        
        .collapsed {
          height: 50px;
        }
        
        .expanded {
          min-height: 200px;
        }
      `}</style>
    </div>
  );
};

export default QABot;