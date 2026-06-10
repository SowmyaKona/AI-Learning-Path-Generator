from pydantic import BaseModel, Field

class UserInput(BaseModel):

    skill: str = Field(min_length=2, max_length=100)
    level: str
    goal: str
    style: str
