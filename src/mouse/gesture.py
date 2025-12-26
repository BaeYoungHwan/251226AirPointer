import math

class GestureDetector:
    """
    손 랜드마크를 기반으로 제스처를 판별하는 클래스
    """

    def __init__(self, click_threshold=0.03):
        # 손가락 거리 임계값 (작을수록 민감)
        self.click_threshold = click_threshold

        # 클릭 중복 방지를 위한 상태값
        self.prev_click = False

    def _distance(self, p1, p2):
        """
        두 랜드마크 사이 거리 계산
        MediaPipe 좌표는 비율이므로 그대로 사용
        """
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    def is_left_click(self, hand_landmarks):
        """
        엄지(4)와 검지(8)가 가까우면 좌클릭
        """
        index = hand_landmarks.landmark[8]
        center = hand_landmarks.landmark[12]

        dist = self._distance(center, index)

        # 현재 클릭 상태
        click_now = dist < self.click_threshold

        # 이전 프레임에는 아니고, 지금만 참이면 "클릭 발생"
        if click_now and not self.prev_click:
            self.prev_click = True
            return True

        # 손이 다시 떨어지면 상태 초기화
        if not click_now:
            self.prev_click = False

        return False
