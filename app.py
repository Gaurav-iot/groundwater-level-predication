import streamlit as st
import joblib 
import numpy as np

st.title("🌊 Smart Groundwater Level Prediction")
st.markdown("Predict groundwater level using actual rainfall, normal level, and deviation")

# Input fields (must match the trained model's features: actual, normal, deviation)
actual = st.number_input("Actual Rainfall (mm)", min_value=0.0)
normal = st.number_input("Normal Rainfall Level (mm)", min_value=0.0)
deviation = actual - normal  # Automatically calculated

st.markdown(f"📉 **Deviation (actual - normal):** `{deviation:.2f}` mm")

# Load model
try:
    model = joblib.load("src/models/groundwater_model.pkl")

except Exception as e:
    st.error(f"⚠️ Failed to load model: {e}")
    st.stop()

# Predict
if st.button("🔮 Predict Groundwater Level"):
    try:
        input_data = np.array([[actual, normal, deviation]])
        prediction = model.predict(input_data)[0]
        st.success(f"✅ Predicted Groundwater Level: **{prediction:.2f} meters**")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")


