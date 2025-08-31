from pydantic import BaseModel, Field



class CreateUser(BaseModel):
    email: str
    password: str = Field(min_length=6)