import mediapipe as mp
import cv2

class HandDetector:
    """
    MediaPipe Hands를 사용하여 손 랜드마크를 검출
    """

    def __init__(
        self,
        max_num_hands=1,
        detection_confidence=0.7,
        tracking_confidence=0.7
    ):
        # MediaPipe Hands 솔루션
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        # 손 관절을 그리기 위한 도구
        self.drawer = mp.solutions.drawing_utils

    def process(self, frame):
        """
        프레임에서 손 인식 수행
        :param frame: BGR 이미지(OpenCV)
        :return: 손 랜드마크 결과
        """
        # OpenCV는 BGR, MediaPipe는 RGB 사용
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw(self, frame, hand_landmarks):
        """
        손 랜드마크를 화면에 그림
        """
        self.drawer.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS
        )
