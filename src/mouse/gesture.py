import math

class GestureDetector:
    """
    손 랜드마크를 기반으로 제스처를 판별하는 클래스
    """

    def __init__(self, click_threshold=0.05):
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
        검지(8)와 중지(12)가 가까우면 좌클릭
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

    def get_finger_status(self, hand):
        """
        손가락이 펴져 있는지 접혀 있는지 확인하는 함수
        """
        # 오른손만 사용
        fingers = []

        # 엄지: 랜드마크 4가 랜드마크 2의 오른쪽에 있으면 펼쳐진 상태
        if hand.landmark[4].x < hand.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # 나머지 손가락: 각 손가락의 팁 (8, 12, 16, 20)이 PIP (6, 10, 14, 18) 위에 있으면 펼쳐진 상태
        tips = [8, 12, 16, 20]
        pip_joints = [6, 10, 14, 18]

        for tip, pip in zip(tips, pip_joints):
            if hand.landmark[tip].y < hand.landmark[pip].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
    


    def recognize_gesture(self, fingers_status):
        if fingers_status == [0, 0, 0, 0, 1]:
            return 'fist'
        elif fingers_status == [0, 1, 0, 0, 0]:
            return 'point'
        elif fingers_status == [1, 1, 1, 1, 1]:
            return 'open'
        elif fingers_status == [0, 1, 1, 0, 0]:
            return 'peace'
        elif fingers_status == [1, 0, 0, 0, 0]:
            return 'standby'