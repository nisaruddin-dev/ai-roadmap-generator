import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Roadmap Generator", page_icon="🧭")
st.title("🧭 AI Learning Roadmap Generator")
st.caption("Get a personalized learning path powered by Groq")

# Inputs
domain = st.text_input("Domain", placeholder="e.g., Machine Learning, Web Development")
level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
time_available = st.text_input("Time Available", placeholder="e.g., 8 weeks, 5 hours/week")

if st.button("Generate Roadmap", type="primary"):
    if not domain or not time_available:
        st.warning("Please fill in all fields.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            prompt = f"""Create a complete learning roadmap for {domain}.
Level: {level}. Time available: {time_available}.

Include:
1. Prerequisites (what to know before starting)
2. Weekly breakdown (what to learn each week)
3. Phases (group weeks into logical phases)
4. Resources (books, courses, tutorials)

Keep it practical and actionable."""

            with st.spinner("Generating your roadmap..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=2048
                )
            
            st.markdown("---")
            st.markdown(response.choices[0].message.content)
            
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check that GROQ_API_KEY is set in Streamlit Secrets.")