import React, { useState } from "react";
import axios from "axios";

function App() {
  const [sentence, setSentence] = useState("");
  const [message, setMessage] = useState("");
  const [sentences, setSentences] = useState({});

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
  return (
    <div>
      <h1>Unique Sentence Checker</h1>
      <input
        type="text"
        value={sentence}
        onChange={(e) => setSentence(e.target.value)}
        placeholder="Enter a sentence"
      />
      <button onClick={handleSubmit}>Submit</button>
      <p>{message}</p>
      <h2>Stored Sentences</h2>
      <pre>{JSON.stringify(sentences, null, 2)}</pre>
    </div>
  );
}

export default App;
