# 🧠 Smart Emotion Analyzer

An interactive Full-Stack AI web application that captures user facial expressions via a webcam and analyzes emotions in real time using DeepFace and Flask.

## 🚀 Features

- **Real-Time Video Streaming:** Captures high-quality snapshots directly from the user's browser using `react-webcam`.
- **AI-Powered Emotion Detection:** Utilizes Python and DeepFace to accurately predict human emotions (Happy, Sad, Angry, Neutral, etc.).
- **Modern UI:** Built with React and structured for a seamless, responsive user experience.
- **Production Architecture:** Frontend hosted on Vercel, connected securely to a Python Flask backend API.

## 🛠️ Tech Stack

- **Frontend:** React, JavaScript, HTML5, CSS3, Vercel
- **Backend:** Python, Flask, Gunicorn, Flask-CORS
- **AI / Computer Vision:** DeepFace, OpenCV
- **Version Control:** Git, GitHub

## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/Kamelia-Mohamed/Smart-Emotion-Analyzer.git](https://github.com/Kamelia-Mohamed/Smart-Emotion-Analyzer.git)
   ```

## ⚙️ How to Run Locally

### 1. Set up the backend:

```bash
cd Smart-Emotion-Analyzer
python -m venv venv
venv\Scripts\activate  # (On Windows) أو source venv/bin/activate (On Mac/Linux)
pip install -r requirements.txt
python app.py

```

2. Run the frontend:

cd emotion-ui
npm install
npm run dev
