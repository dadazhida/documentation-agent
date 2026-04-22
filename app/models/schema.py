from pydantic import BaseModel

class RequestSchema(BaseModel):
    task: str
    k: int = 5