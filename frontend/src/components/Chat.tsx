import React, { useState, useRef, useEffect } from 'react';
import './Chat.css';

interface Message {
  role: 'user' | 'assistant' | 'system' | 'tool';
  content: string;
}

interface ChatResponse {
  conversation_id: number;
  response: string;
  tool_calls: any[];
}

export const Chat: React.FC = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [conversationId, setConversationId] = useState<number | null>(() => {
    const saved = localStorage.getItem('chat_conversation_id');
    return saved ? parseInt(saved, 10) : null;
  });
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (conversationId) {
        localStorage.setItem('chat_conversation_id', conversationId.toString());
    }
  }, [conversationId]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      // Using 'test_user' as the default user_id for development
      const response = await fetch(`${apiUrl}/api/test_user/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: input,
          conversation_id: conversationId
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data: ChatResponse = await response.json();
      
      // Update conversation ID if it's new
      if (conversationId === null && data.conversation_id) {
        setConversationId(data.conversation_id);
      }

      const assistantMessage: Message = { 
        role: 'assistant', 
        content: data.response 
      };
      
      setMessages(prev => [...prev, assistantMessage]);

    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, { role: 'assistant', content: "Error: Could not reach the server." }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-container">
      <header className="chat-header">
        <h1>AI Todo Assistant</h1>
      </header>
      <div className="messages-area">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.role}`}>
            <div className="message-content">
              {msg.role === 'assistant' ? '🤖 ' : '👤 '}
              {msg.content}
            </div>
          </div>
        ))}
        {isLoading && <div className="message assistant"><div className="message-content">Thinking...</div></div>}
        <div ref={messagesEndRef} />
      </div>
      <div className="input-area">
        {input.trim().length > 0 && <div className="text-blinker"></div>}
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Type a command (e.g., 'Add buy milk')"
          disabled={isLoading}
        />
        <button onClick={sendMessage} disabled={isLoading}>Send</button>
      </div>
      <div className="chat-footer">
        <div className="ticker-text">Phase III: Todo AI Chatbot</div>
      </div>
    </div>
  );
};