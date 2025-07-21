
import streamlit as st
import openai

st.set_page_config(page_title="Focus Fitness AI Tutor", page_icon="🏋️")

st.title("🏋️ Focus Fitness AI Tutor")
st.markdown("""
Ask any question based on the Level 2 & Level 3 manuals. This assistant uses embedded content from:
- **Q2CGI Manual** (Level 2 Gym Instructor)
- **Q3EXPT Manual** (Level 3 Personal Trainer)
""")
st.markdown("---")

# Get OpenAI API key
openai_api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")
if not openai_api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

# Sample embedded content (would be larger/more detailed in production)
Q2CGI_context = """
Gym instructors must understand the skeletal, muscular, cardiovascular and energy systems. 
They must also apply customer care, safety, and consultation skills in a gym-based setting. 
Anatomy includes long bones (femur, humerus), types of joints (hinge, ball-and-socket), 
muscle contractions (concentric, eccentric), and postural deviations (kyphosis, lordosis).
"""

Q3EXPT_context = """
Personal trainers design progressive programs using FITT principles and periodisation. 
They must assess clients, apply behaviour change models, and account for special populations. 
Knowledge includes macronutrients, aerobic vs anaerobic energy systems, and cardiovascular adaptations.
"""

# User question
question = st.text_input("❓ Ask your study question:")

if question:
    with st.spinner("Thinking..."):
        openai.api_key = openai_api_key
        system_prompt = (
            "You are a helpful and qualified personal training tutor at Focus Fitness. "
            "Use the following course materials to answer questions accurately:

"
            f"Q2CGI Manual:
{Q2CGI_context}

Q3EXPT Manual:
{Q3EXPT_context}"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                temperature=0.5,
                max_tokens=600
            )
            answer = response["choices"][0]["message"]["content"]
            st.markdown("### ✅ Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
