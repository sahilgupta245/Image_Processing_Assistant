import cv2
import mediapipe as mp
import pyautogui
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Set up the hand detection model
hands = mp_hands.Hands(
    max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5
)

def map_gesture_to_mouse_action(hand_landmarks):
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

    # Define gesture thresholds (adjust as needed)
    click_threshold = 0.1
    scroll_threshold = 0.2

    # Cursor movement
    x = int(index_tip.x * width)
    y = int(index_tip.y * height)
    pyautogui.moveTo(x, y)

    # Left click
    if index_tip.y < middle_tip.y - click_threshold:
        pyautogui.click()

    # Scroll
    if index_tip.x - middle_tip.x > scroll_threshold:
        pyautogui.scroll(5)  # Scroll up
    elif index_tip.x - middle_tip.x < -scroll_threshold:
        pyautogui.scroll(-5)  # Scroll down

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("Ignoring empty camera frame.")
        continue

    width, height, _ = frame.shape

    # Flip the frame horizontally for a more natural experience
    frame = cv2.flip(frame, 1)

    # Process the frame with MediaPipe
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            map_gesture_to_mouse_action(hand_landmarks)
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow('Hand Mouse Control', frame)

    if cv2.waitKey(5) & 0xFF == 27:  # Exit on 'Esc' key
        break

cap.release()
