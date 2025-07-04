import streamlit as st

# 🟣 Page Title and Intro
st.title("🏦 SME Credit Readiness Check")

st.markdown("""
Welcome! We're helping small business owners like you discover funding opportunities by assessing credit readiness.  
Answer a few simple questions — it takes less than 3 minutes, and you'll get instant feedback on your business score.
""")

# 📝 SME Form
st.header("📋 Business Profile")
with st.form("sme_form"):
    bus_status = st.selectbox("Do you have a registered business bank account?", ["Select...", "Yes", "No"])
    mnt_prft = st.selectbox("Monthly profit range", ["Select...", "R3000–R8000", "R8000–R13000", "R13000–R20000", "R20000–R30000"])
    tracking = st.selectbox("How do you track your inventory?", ["Select...", "Digital", "Manual", "Not at all"])

    st.header("💸 Credit Behavior")
    credit = st.selectbox("Do you currently have a loan or credit facility?", ["Select...", "Yes", "No"])
    defaults = st.selectbox("Have you ever missed loan repayments?", ["Select...", "Yes", "No"])

    st.header("📢 Digital Presence")
    media = st.selectbox("Do you promote your business on social media?", ["Select...", "Yes", "No", "None"])

    submitted = st.form_submit_button("🔍 Calculate My Score")

st.caption("Your data stays private and will never be shared. This tool is for self-assessment and learning only.")

# ✅ Validate and Calculate Score
if submitted and (
    bus_status != "Select..." and mnt_prft != "Select..." and
    tracking != "Select..." and credit != "Select..." and
    defaults != "Select..." and media != "Select..."
):
    score = 0
    score += 10 if bus_status == "Yes" else 0
    score += {"R3000–R8000": 3, "R8000–R13000": 5, "R13000–R20000": 7, "R20000–R30000": 10}.get(mnt_prft, 0)
    score += 10 if tracking == "Digital" else 5 if tracking == "Manual" else 0
    score += 5 if credit == "No" else 0
    score += 10 if defaults == "No" else 0
    score += 5 if media == "Yes" else 0

    if score >= 40:
        risk = "🟢 Low Risk"
        tip = "Your business is well positioned for funding opportunities. Keep up the good financial habits!"
    elif score >= 30:
        risk = "🟡 Medium Risk"
        tip = "Consider improving your inventory tracking or promoting your business online to boost your score."
    else:
        risk = "🔴 High Risk"
        tip = "Work on building a digital presence and tracking tools to improve future funding eligibility."

        st.success(f"Your credit score is **{score}/50** — {risk}")
    st.info(tip)

elif submitted:
    st.warning("Please complete all fields before submitting.")

# 🔄 Optional: Refresh Button — safe version
if st.button("🔄 Clear Form"):
    st.session_state.clear()
    st.experimental_rerun()



