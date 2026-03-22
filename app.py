import streamlit as st
from prompts import build_prompt
from utils import get_career_response

st.set_page_config(page_title="CareerOS AI")

st.title("🚀 CareerOS AI")
st.subheader("GenAI-powered Career Intelligence Engine")

# Sidebar
api_key = st.sidebar.text_input("Enter Claude API Key", type="password")

# Input
st.header("Tell us about yourself")

interest = st.selectbox(
    "Interest",
    ["Coding", "Design", "Business", "Finance", "Research"]
)

skill = st.selectbox(
    "Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

goal = st.text_input("Goal (optional)")

# Button
if st.button("Generate Career Roadmap"):

    if not api_key:
        st.warning("Enter API key first")
    else:
        with st.spinner("Generating..."):

            prompt = build_prompt(interest, skill, goal)
            output = get_career_response(prompt, api_key)

        st.success("Here is your career plan 👇")
        st.markdown(output)
