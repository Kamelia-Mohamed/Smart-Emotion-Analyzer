import cv2
from deepface import DeepFace

cap = None

for i in range(5):
    temp_cap = cv2.VideoCapture(i, cv2.CAP_MSMF)
    if temp_cap.isOpened():
        ret, frame = temp_cap.read()
        if ret:
            print(f"✅ Camera successfully connected at index: {i}")
            cap = temp_cap
            break
        else:
            temp_cap.release()

if not cap or not cap.isOpened():
    print("❌ Still no camera found.")
else:
    print("⏳ AI Model is ready. Analyzing every 15 frames for better stability...")
    
    # 1. Variables to control the speed and stabilize the output
    frame_counter = 0
    current_emotion = "Detecting..."
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break
            
        frame = cv2.flip(frame, 1)
        frame_counter += 1
        
        # 2. Only analyze the frame if the counter is a multiple of 15
        if frame_counter % 15 == 0:
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                # Update the emotion only every 15th frame
                current_emotion = result[0]['dominant_emotion']
            except Exception:
                pass
                
        # 3. Always display the last detected emotion
        cv2.putText(frame, f"Emotion: {current_emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
        cv2.imshow('Emotion Analyzer', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()