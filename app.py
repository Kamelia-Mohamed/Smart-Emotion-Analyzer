from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from deepface import DeepFace

app = Flask(__name__)
CORS(app)

# 1. A simple route to test if the server is working from the browser
@app.route('/', methods=['GET'])
def home():
    return "🚀 Flask Server is running! Ready to analyze emotions."

# 2. The main AI endpoint
@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    try:
        data = request.json
        if 'image' not in data:
            return jsonify({"error": "No image provided"}), 400
        
        image_data = data['image'].split(',')[1]
        
        np_arr = np.frombuffer(base64.b64decode(image_data), np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        
        return jsonify({"emotion": dominant_emotion}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Flask API is running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)