from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser

class LearningPath(BaseModel):
    learning_stages: List[str]
    key_topics: List[str]
    learning_goal_summary: str
    learning_phases: List[str]
    recommended_resources: List[str]
    youtube_channels: List[str]
    recommended_projects: List[str]
    quiz_questions: List[str]

parser = PydanticOutputParser(pydantic_object=LearningPath)
