from pydantic import BaseModel
from typing import List
from langchain_core.output_parsers import PydanticOutputParser

class LearningPhase(BaseModel):
    title: str
    topics: List[str]
    outcome: str
    
class LearningPath(BaseModel):
    key_topics: List[str]
    learning_goal_summary: str
    learning_phases: List[LearningPhase]
    recommended_resources: List[str]
    youtube_channels: List[str]
    recommended_projects: List[str]

parser = PydanticOutputParser(pydantic_object=LearningPath)
