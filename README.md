# 🖐 AirPointer  
**MediaPipe 기반 손 제스처 가상 마우스**

웹캠 하나로 손을 인식해  
**마우스 이동 · 클릭 · 스크롤**을 제스처로 제어하는 가상 마우스 프로젝트입니다.

MediaPipe Hands를 활용하여 실시간 손 랜드마크를 추적하고,  
Python으로 OS 마우스 이벤트를 제어합니다.

---

## 🎥 Demo Video


<video controls width="720">
<source src="docs/0102 airproject/0102 airpointer.mp4"  type="video/mp4">
Your browser does not support the video tag.
</video>


> 영상에는 손 이동에 따른 커서 이동, 클릭 제스처, 스크롤 제스처 동작이 포함되어 있습니다.

---

## 🛠 Development Environment

- **Language**: Python 3.11.9  
- **IDE**: VSCode  
- **OS**: Windows  

### Libraries
- MediaPipe  
- OpenCV  
- PyAutoGUI  

---

## 📁 Project Structure

AirPointer/<br/>
├─ main.py<br/> # 프로그램 실행 진입점
├─ src/<br/>
│ ├─ camera/<br/>
│ │ └─ webcam.py<br/> # 웹캠 프레임 처리
│ ├─ hand/<br/>
│ │ └─ detector.py<br/> # MediaPipe 손 인식
│ ├─ mouse/<br/>
│ │ ├─ controller.py<br/> # 마우스 이동 / 클릭 / 스크롤
│ │ └─ gesture.py<br/> # 제스처 판별 로직
│ └─ config.py<br/> # 공통 설정값
└─ docs/<br/>
└─ 0102 airproject<br/> # 시연 영상


---

## ✨ Features

### 🖱 Mouse Move
- 검지 끝(landmark 8)을 커서로 사용
- 떨림 보정(Smoothing) 적용
- 작동 영역(Active Area) 제한으로 미세 조작 가능

### 👆 Click
- 검지 + 중지 거리 기반 좌클릭
- 프레임 상태 관리로 중복 클릭 방지

### 🔄 Scroll
- 손가락 상태 기반 제스처 인식
- 펼친 손 → 스크롤 업
- 주먹 → 스크롤 다운

---

## 🧠 Key Techniques

- MediaPipe Hands (21 Landmarks)
- 손가락 상태 분석 (펴짐 / 접힘)
- 선형 보간(LERP) 기반 마우스 이동 보정
- Active Area 좌표 재정규화
- 제스처 상태 머신 설계

---

## ▶ How to Run

```bash
pip install mediapipe opencv-python pyautogui
python main.py

종료 방법

ESC 또는 Q 키 입력

📌 Notes

조명 환경에 따라 인식 정확도가 달라질 수 있습니다.

손은 카메라 중앙 영역에서 사용하는 것이 가장 안정적입니다.

config.py에서 보정 계수 및 작동 범위를 조절할 수 있습니다.

🚀 Future Improvements

드래그 & 드롭 제스처

제스처 안정화 (n 프레임 유지)

스크롤 속도 가속

작동 영역 시각화 UI

다중 모니터 지원

📄 License

This project is for learning and experimental purposes.

