import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import SentimentChart from './components/SentimentChart';
import './App.css';


const App = () => {
  const [sentimentData, setSentimentData] = useState(null);

  const handleUploadSuccess = (data) => {
    setSentimentData(data);
  };

  return (
    <div className="App">
      <h1>Sentiment Analysis Portal</h1>
      <FileUpload onUploadSuccess={handleUploadSuccess} />
      {sentimentData && <SentimentChart data={sentimentData} />}
    </div>
  );
};

export default App;
