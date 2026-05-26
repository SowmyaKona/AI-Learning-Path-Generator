from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)


def ask_mentor(question):

    prompt = f"""
    You are an AI Learning Mentor.

    Answer the user's learning question clearly and simply.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content