import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function App() {
  const [data, setData] = useState([]);
  const [url, setUrl] = useState('');
  const [results, setResults] = useState(null);

  useEffect(() => {
    fetch('/download')
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data); // Correct place to log the data
      });
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/download', {
        url,
      });
      console.log(response.data);
      setResults(response.data.results);
    } catch (error) {
      console.error('Error fetching data:', error);
      setResults(['Error fetching data']);
    }
  };

  return (
    <>
      <form id="submit-field" onSubmit={handleSubmit}>
        <label>
          <input
            id="url-field"
            type="text"
            placeholder="ENTER URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
        </label>
        <button id="submit-btn" type="submit">
          Submit
        </button>
      </form>
    </>
  );
}
