import streamlit as st
import time
from models import UserInput
from chain import generate_learning_path
from mentor import ask_mentor

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Learning Mentor",
    layout="wide"
)
# =========================
# CUSTOM CSS — VIOLET THEME
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Kill ALL default Streamlit top padding/margins */
.block-container {
    padding-top: 3rem !important;
    padding-bottom: 1rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}
.stApp { background: #0d0d14; color: #e8e6f0; }

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: #13121f !important;
    border-right: 1px solid #2a2540;
}
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] header {
    color: #a78bfa !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
}
/* Tighten sidebar element gaps */
[data-testid="stSidebar"] .stSelectbox,
[data-testid="stSidebar"] .stSlider,
[data-testid="stSidebar"] .stRadio { margin-bottom: 0.4rem !important; }

/* ---- Title ---- */
h1 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.8rem !important;
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 50%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0 !important;
    padding-bottom: 0 !important;
    line-height: 1.2 !important;
}
h2, h3 {
    font-family: 'Syne', sans-serif !important;
    color: #a78bfa !important;
    font-weight: 700 !important;
    margin-top: 0.8rem !important;
    margin-bottom: 0.4rem !important;
}
.stCaption p {
    color: #7c6fa0 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-top: 0 !important;
    margin-bottom: 0.3rem !important;
}

/* ---- Divider tight ---- */
hr {
    border-color: #2a2540 !important;
    margin: 0.5rem 0 !important;
}

/* ---- Text input ---- */
[data-testid="stTextInput"] > div > div {
    background: #1a1830 !important;
    border: 1.5px solid #3b2f6e !important;
    border-radius: 10px !important;
    color: #e8e6f0 !important;
}
[data-testid="stTextInput"] > div > div:focus-within {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.15) !important;
}
[data-testid="stTextInput"] label {
    color: #c4b5fd !important;
    font-weight: 500 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 0.2rem !important;
}
/* Remove gap below input */
[data-testid="stTextInput"] { margin-bottom: 0.5rem !important; }

/* ---- Buttons ---- */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #7c3aed, #5b21b6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.55rem 1.5rem !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 16px rgba(124,58,237,0.35) !important;
    width: 100% !important;
    margin-top: 0 !important;
}
div[data-testid="stButton"] > button:hover {
    background: linear-gradient(135deg, #6d28d9, #4c1d95) !important;
    box-shadow: 0 6px 24px rgba(124,58,237,0.5) !important;
    transform: translateY(-1px);
}
[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    background: #1e1b35 !important;
    color: #a78bfa !important;
    border: 1.5px solid #3b2f6e !important;
    box-shadow: none !important;
    font-size: 0.82rem !important;
    padding: 0.4rem 1rem !important;
}
[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    background: #2a2350 !important; transform: none;
}

/* ---- Custom compact stat cards ---- */
.stat-panel {
    background: #13121f;
    border: 1px solid #2a2540;
    border-radius: 12px;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.5rem;
}
.stat-label {
    font-size: 0.66rem;
    color: #7c6fa0;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: block;
    margin-bottom: 0.1rem;
}
.stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    color: #a78bfa;
    line-height: 1.1;
}
.stat-icon-label {
    font-size: 0.66rem;
    color: #7c6fa0;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 0.15rem;
}
.dash-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    color: #a78bfa;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    border-bottom: 1px solid #2a2540;
    padding-bottom: 0.4rem;
    margin-bottom: 0.6rem;
}

/* ---- Tabs — no gap above ---- */
[data-testid="stTabs"] { margin-top: 0.4rem !important; }
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: #13121f !important;
    border-radius: 10px !important;
    padding: 3px !important;
    gap: 3px !important;
    border: 1px solid #2a2540 !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    color: #7c6fa0 !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.82rem !important;
    border: none !important;
    padding: 0.4rem 0.8rem !important;
    transition: all 0.2s !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #5b21b6) !important;
    color: #fff !important;
    font-weight: 600 !important;
}
/* Reduce tab content top padding */
[data-testid="stTabs"] > div:last-child { padding-top: 0.6rem !important; }

/* ---- Alerts ---- */
div[data-testid="stSuccessMessage"] {
    background: #1a2635 !important;
    border-left: 3px solid #10b981 !important;
    border-radius: 10px !important;
    color: #6ee7b7 !important;
    padding: 0.6rem 0.9rem !important;
    margin-bottom: 0.4rem !important;
}
div[data-testid="stInfoMessage"] {
    background: #1a1830 !important;
    border-left: 3px solid #7c3aed !important;
    border-radius: 10px !important;
    color: #c4b5fd !important;
    padding: 0.6rem 0.9rem !important;
    margin-bottom: 0.4rem !important;
}

/* ---- Selectbox / Slider / Radio ---- */
[data-testid="stSelectbox"] > div > div {
    background: #1a1830 !important;
    border: 1.5px solid #3b2f6e !important;
    border-radius: 10px !important;
    color: #e8e6f0 !important;
}
[data-testid="stSelectbox"] label,
[data-testid="stSlider"] label,
[data-testid="stRadio"] label {
    color: #c4b5fd !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
[data-testid="stRadio"] span { color: #e8e6f0 !important; font-size: 0.88rem !important; }

/* ---- Spinner ---- */
[data-testid="stSpinner"] { color: #a78bfa !important; }

/* ---- Scrollbar ---- */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0d0d14; }
::-webkit-scrollbar-thumb { background: #3b2f6e; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #7c3aed; }

/* Kill extra vertical gaps Streamlit adds between elements */
.element-container { margin-bottom: 0.3rem !important; }
.stMarkdown { margin-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================

if "roadmap_count" not in st.session_state:
    st.session_state.roadmap_count = 0

if "mentor_count" not in st.session_state:
    st.session_state.mentor_count = 0

if "last_response_time" not in st.session_state:
    st.session_state.last_response_time = 0

if "response" not in st.session_state:
    st.session_state.response = None

if "mentor_response" not in st.session_state:
    st.session_state.mentor_response = ""

# =========================
# HEADER
# =========================

st.markdown("""
<div style="margin-bottom:0.6rem;">
  <h1 style="font-family:'Syne',sans-serif;font-weight:800;font-size:1.7rem;
             background:linear-gradient(135deg,#a78bfa,#7c3aed,#c4b5fd);
             -webkit-background-clip:text;-webkit-text-fill-color:transparent;
             background-clip:text;margin:0;padding:0;line-height:1.2;">
    🚀 AI Learning Path Generator
  </h1>
  <p style="color:#7c6fa0;font-size:0.75rem;letter-spacing:0.07em;
            text-transform:uppercase;margin:0.2rem 0 0 0;">
    Personalized Roadmaps &bull; AI Mentor &bull; Projects &bull; Resources
  </p>
  <hr style="border:none;border-top:1px solid #2a2540;margin:0.5rem 0 0 0;">
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.header("📘 Learner Profile")

level = st.sidebar.selectbox("Current Level",
    ["Beginner", "Intermediate", "Advanced"])

goal_option = st.sidebar.selectbox("Learning Goal",
    [
        "Get Started", "Build Projects", "Crack Interviews",
        "Become Job Ready", "Become Data Analyst", "Become Data Scientist",
        "Become ML Engineer", "Become AI Engineer", "Master the Skill", "Custom"
    ]
)

if goal_option == "Custom":
    goal = st.sidebar.text_input("Enter Custom Goal")
else:
    goal = goal_option

style = st.sidebar.radio("Learning Style", ["Theory Based", "Project Based"])

st.sidebar.divider()
if st.sidebar.button("🔄 Reset Learning Session"):
    st.session_state.response = None
    st.session_state.mentor_response = ""
    st.sidebar.success("Chat history cleared!")

# =========================
# MAIN LAYOUT
# =========================

main_col, dash_col = st.columns([3, 1], gap="large")

with main_col:
    skill = st.text_input("Enter Skill",
        placeholder="e.g. Data Science , GenAI, Python, SQL..."
    )
    generate_clicked = st.button("🚀 Generate Roadmap")

with dash_col:
    st.markdown(f"""
    <div class="dash-title">📊 Monitoring Dashboard</div>
    <div class="stat-panel">
      <div class="stat-label">📚 Roadmaps Generated</div>
      <div class="stat-value">{st.session_state.roadmap_count}</div>
    </div>
    <div class="stat-panel">
      <div class="stat-label">💬 Mentor Questions</div>
      <div class="stat-value">{st.session_state.mentor_count}</div>
    </div>
    <div class="stat-panel">
      <div class="stat-label">⚡ Last Response Time</div>
      <div class="stat-value">{st.session_state.last_response_time}s</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# GENERATE ROADMAP
# =========================
if generate_clicked:

    try:
        user_input = UserInput(
            skill=skill,
            level=level,
            goal=goal,
            style=style
        )

        with st.spinner("Generating your personalised roadmap..."):
            start_time = time.time()
            response = generate_learning_path(user_input)
            st.session_state.response = response
            st.session_state.roadmap_count += 1
            end_time = time.time()
            st.session_state.last_response_time = round(end_time - start_time, 2)
    except Exception as e:
        st.error(f"Something went wrong: {e}")

if "response" in st.session_state and st.session_state.response is not None:
    response = st.session_state.response

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["🧠 Topics", "📚 Roadmap", "🎥 Resources", "💻 Projects", "🤖 AI Mentor"]
        )

    # ---- TOPICS TAB ----
    with tab1:
        st.subheader("🧠 Key Topics")
        for topic in response.key_topics:
            st.info(topic)

    # ---- ROADMAP TAB ----
    with tab2:
        st.subheader("📅 Learning Phases")
        for phase in response.learning_phases:
            st.markdown(f"### {phase.title}")
            st.write("📚 Topics To Cover:")

            for topic in phase.topics:
                st.write(f"• {topic}")
            st.success(f"🎯 Outcome: {phase.outcome}")
            st.divider()
        st.subheader("📝 Summary")
        st.write(response.learning_goal_summary)
    
    
    # ---- RESOURCES TAB ----
    with tab3:
        st.subheader("📖 Recommended Resources")
        for resource in response.recommended_resources:
            st.write(f"🔗 {resource}")

        st.subheader("🎥 Best YouTube Channels")
        for channel in response.youtube_channels:
            st.write(f"📺 {channel}")

    # ---- PROJECTS TAB ----
    with tab4:
        st.subheader("💻 Recommended Projects")
        for project in response.recommended_projects:
            st.write(f"🚀 {project}")

    # ---- AI MENTOR TAB ----
    with tab5:
        st.subheader("🤖 Ask AI Mentor")
        st.write("Have a doubt? Ask anything below.")
        mentor_question = st.text_input("Your Question",
            placeholder="e.g. What's the difference between supervised and unsupervised learning?",
            key="mentor_question")
        
        if st.button("💬 Ask Mentor", key="mentor_button"):
            if mentor_question:
                st.session_state.mentor_count += 1
                with st.spinner("Mentor is thinking..."):
                    st.session_state.mentor_response = ask_mentor(mentor_question)
            else:
                st.warning("Please type a question first.")    
        if st.session_state.mentor_response:
            st.success("AI Mentor Response")
            st.write(st.session_state.mentor_response)     
                        
