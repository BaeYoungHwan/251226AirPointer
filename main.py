import cv2

# 카메라 입력 관리
from src.camera.webcam import Webcam

# MediaPipe 손 인식
from src.hand.detector import HandDetector

# 마우스 실제 제어
from src.mouse.controller import MouseController

# 제스처 판별 로직
from src.mouse.gesture import GestureDetector

# 설정값
from src.config import INDEX_FINGER_TIP


def main():
    """
    프로그램의 전체 흐름을 제어하는 메인 함수
    - 각 모듈을 생성
    - 프레임 루프 실행
    - 손 인식 → 마우스 이동 → 제스처 처리
    """

    # =========================
    # 1️⃣ 객체 생성
    # =========================

    # 웹캠 객체 (카메라 프레임 제공)
    webcam = Webcam()

    # 손 인식기 (MediaPipe)
    hand_detector = HandDetector()

    # 마우스 컨트롤러 (OS 마우스 제어)
    mouse = MouseController()

    # 제스처 감지기 (클릭 등 상태 판별)
    gesture = GestureDetector()

    # =========================
    # 2️⃣ 메인 루프
    # =========================
    while True:
        # -------------------------
        # 카메라 프레임 읽기
        # -------------------------
        success, frame = webcam.read()
        if not success:
            break

        # 좌우 반전 (거울처럼 보이게)
        frame = cv2.flip(frame, 1)

        # -------------------------
        # 손 인식 처리
        # -------------------------
        result = hand_detector.process(frame)

        # 손이 하나라도 인식되었을 경우
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # 손 랜드마크를 화면에 그림 (디버깅/시각화용)
                hand_detector.draw(frame, hand_landmarks)

                # -------------------------
                # 검지 끝 랜드마크 추출
                # -------------------------
                index_tip = hand_landmarks.landmark[INDEX_FINGER_TIP]

                # -------------------------
                # 1️⃣ 디버깅용: 검지 끝에 초록 점 표시
                # -------------------------
                h, w, _ = frame.shape
                x = int(index_tip.x * w)
                y = int(index_tip.y * h)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

                # -------------------------
                # 2️⃣ 마우스 이동
                # -------------------------
                mouse.move(index_tip.x, index_tip.y)

                # -------------------------
                # 3️⃣ 제스처 처리 (좌클릭)
                # -------------------------
                if gesture.is_left_click(hand_landmarks):
                    mouse.left_click()
                
                
                fingerStatus = gesture.get_finger_status(hand=hand_landmarks)
                fingerGesture = gesture.recognize_gesture(fingers_status = fingerStatus)
                
                if (fingerGesture == 'standby'):
                    mouse.up_scroll()
                elif (fingerGesture == 'fist'):
                    mouse.down_scroll()

        # -------------------------
        # 화면 출력
        # -------------------------
        cv2.imshow("AirPointer", frame)

        # -------------------------
        # 종료 키 처리
        # ESC 또는 q 누르면 종료
        # -------------------------
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            break

    # =========================
    # 3️⃣ 자원 해제
    # =========================
    webcam.release()
    cv2.destroyAllWindows()


# =========================
# 프로그램 시작 지점
# =========================
if __name__ == "__main__":
    main()
