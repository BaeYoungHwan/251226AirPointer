import cv2

class Webcam:
    """
    웹캠을 열고 프레임을 제공하는 클래스
    """

    def __init__(self, camera_index=0):
        # 카메라 장치 열기 (0 = 기본 카메라)
        self.cap = cv2.VideoCapture(camera_index)

    def read(self):
        """
        카메라에서 한 프레임 읽기
        :return: success 여부, frame
        """
        return self.cap.read()

    def release(self):
        """
        카메라 자원 해제
        """
        self.cap.release()
