import React, { useState, useEffect } from 'react';

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/download')
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data); // Correct place to log the data
      });
  }, []);

  return (
    <div>
      home
      {data.map((item, index) => (
        <div key={index}>{item}</div> // Rendering each item in the data array
      ))}
    </div>
  );
}
