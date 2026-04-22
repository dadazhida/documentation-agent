# app/models/schema.py
from pydantic import BaseModel, Field

class RequestSchema(BaseModel):
    task: str = Field(..., description="要件定義書を作成したいプロダクト案")
    k: int = Field(5, ge=1, le=20, description="主要機能の最小数")

class ResponseSchema(BaseModel):
    document: str