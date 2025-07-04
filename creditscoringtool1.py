import streamlit as st

st.title("🏦 SME Credit Readiness Check")

st.markdown("""
Welcome! We're helping small business owners like you discover funding opportunities by assessing credit readiness.  
Answer a few simple questions — it takes less than 3 minutes, and you'll get instant feedback on your business score.
""")


st.header("📋 Business Profile")

with st.form("sme_form"):
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
