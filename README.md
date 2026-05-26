# 🚀 AI Learning Path Generator

An AI-powered personalized learning roadmap generator built using **LangChain**, **Google Gemini**, **Pydantic**, and **Streamlit**.

This project dynamically generates:
- Personalized learning paths
- Skill roadmaps
- Learning phases
- Recommended resources
- YouTube channel suggestions
- Project recommendations
- Quiz questions
- PDF downloadable roadmaps

based on the user's:
- Skill/domain
- Current level
- Learning goal
- Study hours
- Learning style

---

# 📌 Features

## ✅ Personalized Learning Roadmaps
Generates adaptive learning roadmaps for any skill/domain.

Examples:
- Generative AI
- LangChain
- Data Science
- DevOps
- Cybersecurity
- Power BI
- Salesforce
- NLP
- Machine Learning

---

## ✅ Dynamic AI Prompting
Uses intelligent prompt engineering to generate domain-specific roadmaps dynamically instead of hardcoded responses.

---

## ✅ Learning Phases
Generates structured phase-wise learning plans with realistic timelines.

Example:
- Beginner Phase
- Intermediate Phase
- Advanced Phase
- Project Phase

---

## ✅ Resource Recommendations
Provides:
- Courses
- Documentation
- Books
- Blogs
- Practice platforms

---

## ✅ YouTube Recommendations
Suggests the best YouTube channels and playlists related to the selected skill.

---

## ✅ Project Recommendations
Generates beginner to advanced project ideas based on:
- Learning style
- Skill level
- Career goal

---

## ✅ Quiz Generation
Creates quiz questions for self-assessment and revision.

---

## ✅ AI Mentor Assistant
Integrated AI mentor feature for asking learning-related doubts interactively.

---

## ✅ PDF Download
Allows users to download generated learning roadmaps as PDF files.

---

## ✅ Roadmap Visualization
Visualizes roadmap stages using Graphviz flow diagrams.

---

## ✅ Pydantic Validation
Uses Pydantic models for:
- Input validation
- Structured output parsing

---

## ✅ Modern Streamlit UI
Custom dark-themed responsive UI with:
- Styled headings
- Interactive sidebar
- Clean layout
- Personalized sections

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python
- LangChain
- Google Gemini API

## Validation & Parsing
- Pydantic

## Visualization
- Graphviz

## PDF Generation
- FPDF

---

# 📂 Project Structure

```text
learning-path-generator/
│
├── app.py
├── chain.py
├── mentor.py
├── memory.py
├── models.py
├── parser.py
├── prompt.py
├── utils.py
├── requirements.txt
├── .env
│
├── .streamlit/
│      └── config.toml
│
└── README.md
