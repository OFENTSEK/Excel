import streamlit as st

st.title("SME Credit Self-Scoring Tool")

with st.form("sme_form"):
    st.subheader("📝 Business Info")
    bus_status = st.selectbox("Do you have a registered bank account?", ["Yes", "No"])
    mnt_prft = st.selectbox("Monthly Profit Range", ["R3000–R8000", "R8000–R13000", "R13000–R20000", "R20000–R30000"])
    tracking = st.selectbox("Inventory Tracking Method", ["Digital", "Manual", "Not at all"])
    credit = st.selectbox("Do you currently have a loan or credit facility?", ["Yes", "No"])
    defaults = st.selectbox("Have you defaulted on a loan before?", ["Yes", "No"])
    media = st.selectbox("Do you use social media to promote your business?", ["Yes", "No", "None"])
    submitted = st.form_submit_button("Calculate My Score")

if submitted:
    score = 0
    score += 10 if bus_status == "Yes" else 0
    score += {"R3000–R8000": 3, "R8000–R13000": 5, "R13000–R20000": 7, "R20000–R30000": 10}.get(mnt_prft, 0)
    score += 10 if tracking == "Digital" else 5 if tracking == "Manual" else 0
    score += 5 if credit == "No" else 0
    score += 10 if defaults == "No" else 0
    score += 5 if media == "Yes" else 0

    if score >= 40:
        risk = "🟢 Low Risk"
    elif score >= 30:
        risk = "🟡 Medium Risk"
    else:
        risk = "🔴 High Risk"

    st.success(f"Your credit score is {score}/50 — {risk}")
