import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  async function handleSend() {
    if (!message.trim()) return;
    const text = message.trim();
    setMessages((prev) => [...prev, {
      text : message,
      sender: "user"
    }]);
    setMessage("");
    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: text }),
      });
      if (!response.ok) {
        throw new Error("Request Failed!");
      };
      const data = await response.json();
      setMessages((prev) => [...prev, { text: data.response, sender: "assistant" }]);
    } catch {
      setMessages((prev) => [...prev, { text: "Backend connection failed", sender: "assistant" }]);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>Student AI Assistant</h1>
        <p>Your academic assistant</p>
      </header>
      <main className="chat-container">
        <div className="messages">
          {messages.length === 0 && (
            <p className="welcome">
              Hello! How can I help you with your studies?
            </p>
          )}
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") handleSend();
            }}
          />
          <button onClick={handleSend}>
            Send
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;
