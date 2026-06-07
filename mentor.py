from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

def ask_mentor(question):

    print("QUESTION RECEIVED:", question)

    prompt = f"""
    You are an AI Learning Mentor.

    Answer clearly and simply.

    Question:
    {question}
    """

    print("QUESTION:", question)

    response = llm.invoke(prompt)

    print("RESPONSE:", response.content)

    return response.content
