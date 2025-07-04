import streamlit as st

if "form_started" not in st.session_state:
    st.session_state["form_started"] = False

st.title("🏦 SME Credit Readiness Check")

st.markdown("""
Welcome! We're helping small business owners like you discover funding opportunities by assessing credit readiness.  
Answer a few simple questions — it takes less than 3 minutes, and you'll get instant feedback on your business score.
""")


st.header("📋 Business Profile")

with st.form("sme_form"):
    # 👇 form inputs
    bus_status = st.selectbox("Do you have a registered business bank account?", ["Yes", "No"])
    mnt_prft = st.selectbox("Monthly profit range", ["R3000–R8000", "R8000–R13000", "R13000–R20000", "R20000–R30000"])
    tracking = st.selectbox("How do you track your inventory?", ["Digital", "Manual", "Not at all"])

    st.header("💸 Credit Behavior")
    credit = st.selectbox("Do you currently have a loan or credit facility?", ["Yes", "No"])
    defaults = st.selectbox("Have you ever missed loan repayments?", ["Yes", "No"])

    st.header("📢 Digital Presence")
    media = st.selectbox("Do you promote your business on social media?", ["Yes", "No", "None"])

    submitted = st.form_submit_button("🔍 Calculate My Score")

st.caption("Your data stays private and will never be shared. This tool is for self-assessment and learning only.")

# 👇 scoring logic goes OUTSIDE the form block
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

    st.success(f"Your credit score is **{score}/50** — {risk}")

if st.button("🔄 Clear Form"):
    st.experimental_rerun()
