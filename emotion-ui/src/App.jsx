import { useRef, useState, useCallback, useEffect } from 'react';
import Webcam from 'react-webcam';

function App() {
  const webcamRef = useRef(null);
  const [emotion, setEmotion] = useState("Waiting to start...");
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  // Function to capture the image and send it to Flask
  const captureAndAnalyze = useCallback(async () => {
    if (!webcamRef.current) return;
    
    // Take a screenshot from the webcam as a Base64 string
    const imageSrc = webcamRef.current.getScreenshot();
    if (!imageSrc) return;

    try {
      // Send the image to our Flask API
      const response = await fetch('https://fast-chefs-act.loca.lt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageSrc }),
      });

      const data = await response.json();
      
      if (data.emotion) {
        setEmotion(data.emotion);
      }
    } catch (error) {
      console.error("Error connecting to API:", error);
    }
  }, []);

  // Use an interval to analyze the face every 1 second if 'isAnalyzing' is true
  useEffect(() => {
    let interval;
    if (isAnalyzing) {
      setEmotion("Analyzing...");
      interval = setInterval(captureAndAnalyze, 1000);
    } else {
      clearInterval(interval);
      setEmotion("Paused");
    }
    // Cleanup the interval when the component unmounts or state changes
    return () => clearInterval(interval);
  }, [isAnalyzing, captureAndAnalyze]);

  return (
    <div style={{ textAlign: 'center', marginTop: '40px', fontFamily: 'Arial, sans-serif' }}>
      <h1>🧠 Smart Emotion Analyzer</h1>
      
      <div style={{ margin: '20px auto', width: 'fit-content', padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '10px' }}>
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={640}
          height={480}
          style={{ borderRadius: '8px' }}
        />
      </div>

      <h2 style={{ fontSize: '28px' }}>
        Detected Emotion: <span style={{ color: '#007bff', textTransform: 'capitalize' }}>{emotion}</span>
      </h2>

      <button 
        onClick={() => setIsAnalyzing(!isAnalyzing)}
        style={{
          padding: '12px 24px',
          fontSize: '18px',
          fontWeight: 'bold',
          cursor: 'pointer',
          backgroundColor: isAnalyzing ? '#dc3545' : '#28a745',
          color: 'white',
          border: 'none',
          borderRadius: '8px',
          marginTop: '10px'
        }}
      >
        {isAnalyzing ? "Stop Analysis 🛑" : "Start Analysis ▶️"}
      </button>
    </div>
  );
}

export default App;