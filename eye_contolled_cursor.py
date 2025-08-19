import cv2
import mediapipe as mp
import pyautogui
import pyttsx3

# -------------------------------
# Eye Controlled Mouse
# -------------------------------
# Controls the computer mouse using eye movements and blinks
# Cursor moves with eye gaze, and blink acts as a mouse click
# -------------------------------

# Initialize text-to-speech engine
speech_engine = pyttsx3.init()

# Capture video from the default camera
video_capture = cv2.VideoCapture(0)

# MediaPipe FaceMesh for landmark detection
face_detector = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get the screen resolution
screen_width, screen_height = pyautogui.size()

while True:
    # Read a frame from the webcam
    ret, video_frame = video_capture.read()
    if not ret:
        break

    # Flip the frame horizontally (mirror effect)
    video_frame = cv2.flip(video_frame, 1)

    # Convert BGR to RGB for processing
    rgb_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB)

    # Detect facial landmarks
    face_output = face_detector.process(rgb_frame)
    landmark_points = face_output.multi_face_landmarks

    # Frame dimensions
    frame_height, frame_width, _ = video_frame.shape

    if landmark_points:
        # Get landmarks of the first detected face
        facial_landmarks = landmark_points[0].landmark

        # -------------------------------
        # Cursor Movement (Eye Landmarks)
        # -------------------------------
        for index, landmark in enumerate(facial_landmarks[474:478]):
            landmark_x = int(landmark.x * frame_width)
            landmark_y = int(landmark.y * frame_height)

            # Draw points on the frame for visualization
            cv2.circle(video_frame, (landmark_x, landmark_y), 3, (0, 255, 0), -1)

            # Move mouse when the correct landmark is tracked
            if index == 1:  # Landmark index 1 is stable for tracking
                screen_x = screen_width * landmark.x
                screen_y = screen_height * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # -------------------------------
        # Blink Detection (Left Eye)
        # -------------------------------
        left_eye = [facial_landmarks[145], facial_landmarks[159]]

        for landmark in left_eye:
            landmark_x = int(landmark.x * frame_width)
            landmark_y = int(landmark.y * frame_height)
            cv2.circle(video_frame, (landmark_x, landmark_y), 3, (0, 255, 255), -1)

        # Check eye closure (blink)
        if (left_eye[0].y - left_eye[1].y) < 0.007:
            pyautogui.click()
            speech_engine.say("CLICKED")
            speech_engine.runAndWait()

    # -------------------------------
    # Display Output Window
    # -------------------------------
    cv2.imshow('Eye Controlled Mouse', video_frame)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
