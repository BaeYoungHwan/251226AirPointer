import pyautogui
from src.config import SMOOTHING_FACTOR


class MouseController:
    """
    손 좌표를 이용해 마우스를 제어
    + 떨림 보정 포함
    """

    def __init__(self):
        # 모니터 해상도
        self.screen_w, self.screen_h = pyautogui.size()

        # pyautogui 안전 장치
        pyautogui.FAILSAFE = True

        # -------------------------
        # 이전 프레임 마우스 위치
        # (초기값은 화면 중앙)
        # -------------------------
        self.prev_x = self.screen_w // 2
        self.prev_y = self.screen_h // 2

    def move(self, x_ratio, y_ratio):
        """
        MediaPipe 비율 좌표를 받아
        떨림 보정 후 마우스를 이동
        """

        # 목표 마우스 좌표 (손가락이 가리키는 위치)
        target_x = int(x_ratio * self.screen_w)
        target_y = int(y_ratio * self.screen_h)

        # -------------------------
        # 떨림 보정 (LERP)
        # -------------------------
        smooth_x = int(
            self.prev_x +
            (target_x - self.prev_x) * SMOOTHING_FACTOR
        )
        smooth_y = int(
            self.prev_y +
            (target_y - self.prev_y) * SMOOTHING_FACTOR
        )

        # 실제 마우스 이동
        pyautogui.moveTo(smooth_x, smooth_y)

        # 다음 프레임을 위해 현재 위치 저장
        self.prev_x = smooth_x
        self.prev_y = smooth_y

    def left_click(self):
        """
        좌클릭 실행
        """
        pyautogui.click()


    def down_scroll(self):
        """
        밑으로 내리기
        """
        pyautogui.scroll(-120)

    def up_scroll(self):
        """
        위로 올리기
        """

        pyautogui.scroll(120)
