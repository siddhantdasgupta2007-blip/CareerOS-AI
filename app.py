import streamlit as st
import random

# Page config
st.set_page_config(page_title="CareerOS AI", layout="centered")

# ---------------- STYLES ---------------- #
st.markdown("""
<style>
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #111827;
    color: white;
    margin-top: 15px;
    border-left: 5px solid #22c55e;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ---------------- #
st.title("🚀 CareerOS AI")
st.subheader("GenAI-powered Career Intelligence Engine")

st.info("💡 Get AI-powered career insights based on your profile")

# ---------------- INPUT ---------------- #
st.header("🧠 Tell us about yourself")

interest = st.selectbox(
    "Select your interest",
    ["Coding", "Design", "Business", "Finance", "Research"]
)

skill = st.selectbox(
    "Your current skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

goal = st.text_input("Your career goal (optional)")

# ---------------- LOGIC ---------------- #
def generate_smart_output(interest, skill, goal):

    difficulty_map = {
        "Beginner": "Start with basics and build strong foundations",
        "Intermediate": "Focus on advanced concepts and real-world projects",
        "Advanced": "Specialize deeply and target high-level roles"
    }

    level_text = difficulty_map[skill]

    career_map = {
        "Coding": ["Software Engineer", "Data Scientist", "AI Engineer"],
        "Design": ["UI/UX Designer", "Product Designer", "Graphic Designer"],
        "Business": ["Product Manager", "Business Analyst", "Entrepreneur"],
        "Finance": ["Financial Analyst", "Investment Banker", "Chartered Accountant"],
        "Research": ["Research Analyst", "Data Analyst", "Academic Researcher"]
    }

    careers = career_map.get(interest)

    bonus_tip = random.choice([
        "Build strong portfolio projects",
        "Focus on internships early",
        "Participate in competitions and hackathons",
        "Network with industry professionals"
    ])

    return f"""
## 🎯 Recommended Careers

### 1. {careers[0]}
### 2. {careers[1]}
### 3. {careers[2]}

---

## 🛤 Career Roadmap

### 📅 6 Months
- Learn fundamentals in {interest}
- Build 2–3 beginner projects
- {level_text}

### 📅 1 Year
- Work on real-world applications
- Build strong portfolio
- Gain practical exposure

### 📅 3 Years
- Specialize in your chosen domain
- Gain internships or job experience
- Become industry-ready

---

## 🧠 Skills to Focus
- Problem solving
- Communication
- Domain expertise
- Practical implementation

---

## 🔄 Alternative Career Paths
- Consulting
- Freelancing
- Startup ecosystem

---

## 💡 Pro Tip
{bonus_tip}

---

📊 Market Insight:
High demand field with strong growth potential over next 5–10 years.
"""

# ---------------- BUTTON ---------------- #
if st.button("Generate Career Roadmap"):

    with st.spinner("Analyzing your profile..."):
        output = generate_smart_output(interest, skill, goal)

    st.success("Here’s your personalized career plan 👇")

    st.markdown(f"📌 Personalized for: **{interest} | {skill} level**")
    st.markdown("---")

    # Split sections for cleaner display
    sections = output.split("---")

    for section in sections:
        st.markdown(section.strip())
        st.markdown("")

    # Summary Card
    st.markdown(
    f"""
    <div class="card">
    📌 <b>Summary</b><br><br>
    Based on your interest in <b>{interest}</b> and skill level <b>{skill}</b>, 
    you are well-positioned for high-growth career paths.<br><br>
    A structured roadmap can significantly accelerate your progress.
    </div>
    """,
    unsafe_allow_html=True
)

    st.markdown("---")