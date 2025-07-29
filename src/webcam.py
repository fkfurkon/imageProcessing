import cv2

def get_webcam_feed():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open webcam.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        yield frame
    
    cap.release()