from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langfuse  import observe
from langfuse.langchain import CallbackHandler
from prompt import prompt
from parser import parser

#-------- Langfuse Callback Handler------
langfuse_handler = CallbackHandler()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0.7)

# from langchain_core.runnables import RunnableSequence  # Code using runnable sequence
# chain = RunnableSequence(
#     first=prompt.partial(format_instructions=parser.get_format_instructions()),
#     last=llm)

chain = (prompt.partial(format_instructions=parser.get_format_instructions())| llm)

@observe()
def generate_learning_path(user_input):
    response = chain.invoke({
        "skill": user_input.skill,
        "level": user_input.level,
        "goal": user_input.goal,
        "style": user_input.style},
    config={
            "callbacks": [langfuse_handler]
        }
    )
    parsed_response = parser.parse(response.content)
    return parsed_response
