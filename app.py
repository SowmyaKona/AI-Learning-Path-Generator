import streamlit as st
import graphviz

from models import UserInput
from chain import generate_learning_path
from utils import generate_pdf
from memory import chat_history
from mentor import ask_mentor

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Learning Mentor",
    layout="wide"
)

st.markdown(
    """
    <h1 style='
    text-align: center;
    color: #4F8BF9;
    font-size: 55px;
    font-weight: bold;
    '>
    🚀 AI Learning Path Generator
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='
    text-align: center;
    color: #B0B0B0;
    margin-bottom: 40px;
    '>
    Generate personalized learning paths, projects, resources, and career roadmaps using AI.
    </h4>
    """,
    unsafe_allow_html=True
)


# =========================
# SIDEBAR
# =========================

st.sidebar.header("📘 Learner Profile")


# Skill Input

skill = st.text_input(
    "Enter Skill"
)


# Level

level = st.sidebar.selectbox(
    "Current Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


# Learning Goal

goal_option = st.sidebar.selectbox(
    "Learning Goal",
    [
        "Get Started",
        "Build Projects",
        "Crack Interviews",
        "Become Job Ready",
        "Become Data Analyst",
        "Become Data Scientist",
        "Become ML Engineer",
        "Become AI Engineer",
        "Master the Skill",
        "Custom"
    ]
)


if goal_option == "Custom":

    goal = st.sidebar.text_input(
        "Enter Custom Goal"
    )

else:

    goal = goal_option


# Study Hours

hours = st.sidebar.slider(
    "Study Hours Per Day",
    1,
    10,
    2
)


# Learning Style

style = st.sidebar.radio(
    "Learning Style",
    [
        "Theory Based",
        "Project Based",
        "Video Based"
    ]
)


# Reset Memory

if st.sidebar.button("Reset Learning Session"):

    chat_history.clear()

    st.sidebar.success("Chat History Cleared")

# =========================
# GENERATE ROADMAP
# =========================

if st.button("Generate Roadmap"):

    try:

        user_input = UserInput(
            skill=skill,
            level=level,
            goal=goal,
            hours=hours,
            style=style
        )

        with st.spinner("Generating Roadmap..."):

            response = generate_learning_path(
                user_input
            )

        # =========================
        # LEARNING STAGES
        # =========================

        #st.header("📚 Learning Stages")
        st.markdown("## 📚 Learning Stages")
        
        for stage in response.learning_stages:

            st.success(stage)


        # =========================
        # KEY TOPICS
        # =========================

        st.markdown("## 🧠 Key Topics")

        for topic in response.key_topics:

            st.info(topic)


        # =========================
        # LEARNING PHASES
        # =========================

        st.markdown("## 📅 Learning Phases")

        for phase in response.learning_phases:

            st.write(f"✅ {phase}")


        # =========================
        # RESOURCES
        # =========================

        st.markdown("## 📖 Recommended Resources")

        for resource in response.recommended_resources:

            st.write(f"🔗 {resource}")


        # =========================
        # YOUTUBE CHANNELS
        # =========================

        st.markdown("## 🎥 Best YouTube Channels")

        for channel in response.youtube_channels:

            st.write(f"📺 {channel}")


        # =========================
        # PROJECTS
        # =========================

        st.markdown("## 💻 Recommended Projects")

        for project in response.recommended_projects:

            st.write(f"🚀 {project}")


        # =========================
        # QUIZ QUESTIONS
        # =========================

        st.markdown("## ❓ Quiz Questions")

        for question in response.quiz_questions:

            st.write(f"📝 {question}")


        # =========================
        # SUMMARY
        # =========================

        st.markdown("## 📝 Summary")

        st.write(
            response.learning_goal_summary
        )


        # =========================
        # ROADMAP VISUALIZATION
        # =========================

        st.markdown("🗺️ Roadmap Visualization")

        graph = graphviz.Digraph()

        for i in range(
            len(response.learning_stages)
        ):

            graph.node(
                response.learning_stages[i]
            )

            if i > 0:

                graph.edge(
                    response.learning_stages[i - 1],
                    response.learning_stages[i]
                )

        st.graphviz_chart(graph)


        # =========================
        # PDF DOWNLOAD
        # =========================

        pdf_data = generate_pdf(response)
        st.download_button(
            label="📥 Download Roadmap PDF",
            data=pdf_data,
            file_name="learning_roadmap.pdf",
            mime="application/pdf")


    except Exception as e:

        st.error(f"Error: {e}")


# =========================
# AI MENTOR
# =========================

#st.subheader("🤖 Ask AI Mentor")
st.markdown("### 🤖 Ask AI Mentor")


mentor_question = st.text_input(
    "Ask learning doubts"
)

if st.button("Ask Mentor"):

    if mentor_question:

        with st.spinner("Thinking..."):

            mentor_response = ask_mentor(
                mentor_question
            )

        st.success("AI Mentor Response")

        st.write(mentor_response)
