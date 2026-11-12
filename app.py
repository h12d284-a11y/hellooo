from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="BT×DS 생체 데이터 데모", page_icon="🩸", layout="wide")
st.title("🩸 BT×DS 생체 데이터 분석 데모")
st.caption("연구·교육용 프로토타입 · 의료 판단이나 응급 대응에 사용하지 마세요.")
st.warning("이 데모는 실제 저혈당 예측 모델이 아닙니다. 화면의 위험 표시는 임상적으로 검증되지 않았으며 의료 조언을 제공하지 않습니다.")


def demo_data() -> pd.DataFrame:
    rng = np.random.default_rng(12)
    times = pd.date_range(end=pd.Timestamp.now().floor("min"), periods=72, freq="5min")
    glucose = 105 + np.cumsum(rng.normal(0, 1.2, len(times)))
    return pd.DataFrame({
        "timestamp": times,
        "glucose_mg_dl": glucose.round(1),
        "heart_rate_bpm": rng.normal(72, 5, len(times)).round(1),
        "skin_conductance": rng.normal(35, 4, len(times)).round(1),
    })

uploaded = st.file_uploader("CSV 업로드 (timestamp, glucose_mg_dl 필수)", type=["csv"])
try:
    data = pd.read_csv(uploaded) if uploaded else demo_data()
    required = {"timestamp", "glucose_mg_dl"}
    missing = required - set(data.columns)
    if missing:
        st.error("CSV 필수 열이 없습니다: " + ", ".join(sorted(missing)))
        st.stop()

    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="coerce")
    data["glucose_mg_dl"] = pd.to_numeric(data["glucose_mg_dl"], errors="coerce")
    for col in ("heart_rate_bpm", "skin_conductance"):
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    data = (data.dropna(subset=["timestamp", "glucose_mg_dl"])
                .sort_values("timestamp")
                .drop_duplicates("timestamp")
                .reset_index(drop=True))
    if data.empty:
        st.error("표시할 유효 데이터가 없습니다.")
        st.stop()

    minutes = data["timestamp"].diff().dt.total_seconds().div(60)
    data["glucose_slope_mg_dl_min"] = data["glucose_mg_dl"].diff().div(minutes.where(minutes.ne(0))).fillna(0)

    a, b, c = st.columns(3)
    a.metric("마지막 혈당 기록", f"{data['glucose_mg_dl'].iloc[-1]:.1f} mg/dL")
    a.caption("측정값 표시이며 의학적 해석이 아닙니다.")
    b.metric("최근 변화율", f"{data['glucose_slope_mg_dl_min'].iloc[-1]:.2f} mg/dL/min")
    c.metric("기록 수", f"{len(data):,}")

    st.subheader("혈당 시계열")
    st.line_chart(data.set_index("timestamp")[["glucose_mg_dl"]])
    optional = [col for col in ("heart_rate_bpm", "skin_conductance") if col in data.columns]
    if optional:
        st.subheader("추가 센서 데이터")
        st.line_chart(data.set_index("timestamp")[optional])
    st.subheader("최근 기록")
    st.dataframe(data.tail(20), use_container_width=True)
    st.download_button("정리된 데이터 CSV 다운로드", data.to_csv(index=False).encode("utf-8-sig"), "processed_data.csv", "text/csv")
    st.caption("가상 샘플을 표시 중입니다." if uploaded is None else "업로드한 데이터의 시각화입니다. 데이터는 이 데모에서 모델 학습이나 의료 예측에 사용되지 않습니다.")
except Exception as exc:
    st.error(f"파일을 읽거나 처리하지 못했습니다: {exc}")
