from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence

from prompt import prompt
from parser import parser


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)


chain = (
    prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | llm
)


def generate_learning_path(user_input):

    response = chain.invoke({

        "chat_history": "",

        "skill": user_input.skill,

        "level": user_input.level,

        "goal": user_input.goal,

        "hours": user_input.hours,

        "style": user_input.style
    })

    parsed_response = parser.parse(
        response.content
    )

    return parsed_response