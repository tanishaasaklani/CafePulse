import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="CafePulse", page_icon="☕")

# Load model & columns
model = joblib.load("cafepulse_model.pkl")
columns = joblib.load("cafepulse_columns.pkl")

# Session state init
if "page" not in st.session_state:
    st.session_state.page = "input"

# =========================
# SCREEN 1 : INPUT PAGE
# =========================
if st.session_state.page == "input":

    st.markdown("<h1 style='text-align:center;'>CafePulse ☕</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;'>Optimize Your Business with Cafe Revenue Prediction.</p>",
        unsafe_allow_html=True
    )

    st.divider()
    st.subheader("Enter cafe details")

    # Row 1
    col1, col2 = st.columns(2)
    with col1:
        footfall = st.slider("Expected Footfall", 20, 300, 80)
    with col2:
        avg_order = st.slider("Average Order Value (₹)", 100, 500, 250)

    # Row 2
    col3, col4 = st.columns(2)
    with col3:
        staff = st.slider("Staff Count", 2, 15, 6)
    with col4:
        hours = st.slider("Opening Hours", 6, 14, 10)

    # Row 3
    col5, col6 = st.columns(2)
    with col5:
        weekend = st.selectbox("Is it a weekend?", ["No", "Yes"])
    with col6:
        offer = st.selectbox("Offers Running?", ["No", "Yes"])

    # Row 4
    col7, col8 = st.columns(2)
    with col7:
        day = st.selectbox(
            "Day of Week",
            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        )
    with col8:
        weather = st.selectbox(
            "Weather",
            ["Sunny", "Cloudy", "Rainy"]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Centered button
    colb1, colb2, colb3 = st.columns([1, 2, 1])
    with colb2:
        predict = st.button("Predict Revenue")

    if predict:
        st.session_state.inputs = {
            "footfall": footfall,
            "avg_order": avg_order,
            "staff": staff,
            "hours": hours,
            "weekend": weekend,
            "offer": offer,
            "day": day,
            "weather": weather
        }
        st.session_state.page = "result"
        st.rerun()

# =========================
# SCREEN 2 : RESULT PAGE
# =========================
if st.session_state.page == "result":

    input_df = pd.DataFrame([st.session_state.inputs])

    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_encoded)[0]

    st.markdown("<h1 style='text-align:center;'>CafePulse ☕</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;'>Predicted Daily Revenue<br>Based on your inputs</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2 style='text-align:center;'>₹ {int(prediction):,}</h2>",
        unsafe_allow_html=True
    )

    # Graph
    chart_df = pd.DataFrame({
        "Revenue Level": ["Low", "Medium", "High"],
        "Revenue": [
            prediction * 0.75,
            prediction * 0.9,
            prediction
        ]
    })

    st.line_chart(chart_df.set_index("Revenue Level"))

    # Button at bottom
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        again = st.button("Next Prediction")

    if again:
        st.session_state.page = "input"
        st.rerun()
