import streamlit as st
import streamlit as st
import pandas as pd
import yfinance as yf

# 타이틀
st.title("💱 선물환 매수 매도 추천")
st.markdown("### 미국달러(USD) vs 한국원화(KRW)")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = yf.download("USDKRW=X", start="2023-01-01", end="2024-12-31")
    df.reset_index(inplace=True)
    return df

df = load_data()

# 날짜 범위 슬라이더
start_date, end_date = st.slider(
    "날짜 범위 선택",
    min_value=df["Date"].min().date(),
    max_value=df["Date"].max().date(),
    value=(df["Date"].min().date(), df["Date"].max().date())
)

# 필터링
mask = (df["Date"].dt.date >= start_date) & (df["Date"].dt.date <= end_date)
filtered_df = df[mask]

# 차트 그리기
st.line_chart(filtered_df.set_index("Date")["Close"])

# 최근 환율 보여주기
latest_price = float(df['Close'].iloc[-1])
st.metric(label="📌 최신 환율", value=f"{latest_price:,.2f} KRW/USD")





