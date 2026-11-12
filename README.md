# 🩸 BT×DS 기반 저혈당 쇼크 예측 및 실시간 대응 시스템

> 생체 데이터(Bio-Technology)와 데이터 과학(Data Science)을 결합한 저혈당 위험 조기 감지 및 대응 시스템

## 📌 프로젝트 개요

본 프로젝트는 당뇨병 환자 및 고위험군에서 발생할 수 있는 급격한 저혈당 위험을 사전에 예측하고, 골든타임 내에 대응할 수 있도록 설계된 시계열 예측 시스템입니다.

비침습형 생체 센서를 통해 수집된 다중 신호를 정제하고 분석하며, LSTM 기반 딥러닝 모델을 활용해 저혈당 발생 전 위험 징후를 조기에 탐지합니다.

## ⚙️ 시스템 아키텍처

### 1) 데이터 수집 (BT)
- 비침습형 생체 센서 기반 실시간 측정
- 혈당, 심박수, 피부 전도도, 가속도 데이터 수집

### 2) 데이터 전처리 (DS)
- 노이즈 제거 및 신호 정규화
- 움직임 기반 잡음 보정
- Sliding Window 기반 시계열 데이터 구성

### 3) 핵심 특징 추출
- 혈당 변동률 및 기울기
- 심박수 변동성(HRV)
- 피부 전기 활동 변화량

### 4) 예측 및 대응
- LSTM 기반 시계열 예측 모델
- 저혈당 위험 점수 계산
- 임계치 기반 경고 및 실시간 시각화

## 🧠 기대 효과

- 저혈당이 발생하기 전에 조기 경고 가능
- 실시간 모니터링을 통한 대응 시간 단축
- 환자별 패턴 기반 개인화 예측 가능
- 디지털 헬스 및 의료 AI 연구 확장 가능성

## 🧪 기술 스택

- Language: Python 3.x
- Data Processing: Pandas, NumPy, SciPy
- Deep Learning: PyTorch, TensorFlow / Keras
- Visualization: Matplotlib, Streamlit

## 📁 프로젝트 구조 예시

```text
project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── preprocessing/
│   ├── filtering.py
│   ├── sliding_window.py
│   └── feature_engineering.py
├── models/
│   ├── lstm_model.py
│   ├── train.py
│   └── evaluate.py
├── dashboard/
│   └── app.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 실행 방법

```bash
git clone <repository-url>
cd <repository-name>
pip install -r requirements.txt
python main.py
```

## 📌 참고

본 프로젝트는 연구 및 프로토타입 개발 관점에서 설계되며,
의료·응급 대응 시스템으로 직접 적용하기 전에는 데이터 검증, 사용자 동의, 윤리적 검토가 반드시 필요합니다.

## 🌐 GitHub Pages

이 저장소의 정적 프로젝트 소개 페이지는 GitHub Pages로 배포할 수 있습니다.

배포 후 링크 형식:
`https://h12d284-a11y.github.io/hellooo/`
