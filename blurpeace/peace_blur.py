import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def is_peace(landmark):
    """
    cek apakah jari membentuk pose peace, logikanya: jari telunjuk (8) dan tengah (12) lurus ke atas (nilai Y kecil), 
    sedangkan jari manis (16) dan kelingking (20) ditekuk (nilai Y besar).
    """
    index_up = landmark[8].y < landmark[6].y
    middle_up = landmark[12].y < landmark[10].y
    ring_down = landmark[16].y > landmark[14].y
    pinky_down = landmark[20].y > landmark[18].y
    
    if index_up and middle_up and ring_down and pinky_down:
        return True
    return False
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak dapat dibuka")
    exit()

print("Program berjalan...")
print("Tunjukkan gesture PEACE")
print("Tekan ESC untuk keluar")

while True:
    success, frame = cap.read()
    if not success:
        print("Gagal membaca kamera")
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    peace_detected = False
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if is_peace(hand_landmarks.landmark):
                peace_detected = True
                break
    if peace_detected:
        frame = cv2.GaussianBlur(frame, (31, 31), 0)
        cv2.putText(frame, "PEACE DETECTED", (30, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow("Peace Blur Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()