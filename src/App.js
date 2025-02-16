import "./App.css"

import React, { useEffect, useState } from "react";

import axios from "axios";

function App() {
  const [sentence, setSentence] = useState("");
  const [message, setMessage] = useState("");
  const [sentences, setSentences] = useState({});
  const [leaderboard, setLeaderboard] = useState([]);

  const handleSubmit = async () => {
  try {
    // Log the request data being sent
    console.log("Sending data:", { sentence });

    const response = await axios.post("http://127.0.0.1:5000/sentence", {
      sentence: sentence,
    });

    console.log("Response:", response); // Log the full response object

    setMessage(response.data.message);
    setSentences(response.data.sentences);
    setSentence(""); // Clear input field
  } catch (error) {
    console.error("Error:", error.response ? error.response.data : error.message);
    setMessage(error.response?.data?.message || "An error occurred");
  }
};
  const fetchLeaderboard = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/leaderboard", {
        params: { limit: 5 }, // Get top 5
      });

      setLeaderboard(response.data.leaderboard);
    } catch (error) {
      console.error("Error fetching leaderboard:", error);
    }
  };

  useEffect(() => {
    fetchLeaderboard(); // Fetch leaderboard when component mounts
  }, []);
  
  return (
    <div className="container">
      <h1>Unique Sentence Checker</h1>
      <input
        type="text"
        className="input-box"
        value={sentence}
        onChange={(e) => setSentence(e.target.value)}
        placeholder="Enter a sentence"
      />
      <button
        onClick={async () => {
          await handleSubmit(); 
          fetchLeaderboard();
        }}
      >
        Submit
      </button>
      <p>{message}</p>
      <h2>Top Sentences</h2>
      {leaderboard.map(([sentence, count], index) => (
        <li key={index}>
          "{sentence}" - {count} times
        </li>
      ))}
    </div>
  );
}

export default App;
