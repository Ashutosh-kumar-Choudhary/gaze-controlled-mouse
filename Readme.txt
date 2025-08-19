# Eye-Controlled Mouse 

An **AI-powered hands-free mouse system** that allows users to control their computer cursor using **eye movements** and perform clicks by **blinking**.  
Built with **Python, OpenCV, MediaPipe, and PyAutoGUI**.

---

##  Features
- Real-time **eye tracking** using MediaPipe FaceMesh.
- Cursor movement controlled by **eye gaze**.
- **Blink detection** for simulating mouse clicks.
- Audio feedback ("CLICKED") using text-to-speech.
- Enhances **accessibility** for users with physical disabilities.

---

## Tech Stack
- **Python 3.x**
- [OpenCV](https://opencv.org/) – Computer vision
- [MediaPipe](https://developers.google.com/mediapipe) – Facial landmark detection
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) – Mouse automation
- [pyttsx3](https://pypi.org/project/pyttsx3/) – Text-to-speech feedback

---

##  How It Works
1. Captures live video from the webcam.
2. Detects facial landmarks using **MediaPipe FaceMesh**.
3. Maps **eye landmark coordinates** to screen coordinates for cursor control.
4. Detects a **blink** → simulates a mouse click → provides audio feedback.

---

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/eye-controlled-mouse.git
cd eye-controlled-mouse

Requirements**
opencv-python
mediapipe
pyautogui
pyttsx3


Future Improvements**

Double-blink for right click.

Eye gestures for scrolling and drag-and-drop.

Calibration system for different lighting conditions.

Multi-face support for group experiments.

