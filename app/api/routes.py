from fastapi import APIRouter
from app.models.schema import RequestSchema, ResponseSchema
from app.services.doc_generator import generate_document

router = APIRouter()

@router.post("/generate", response_model=ResponseSchema)
def generate(req: RequestSchema):
    result = generate_document(req.task, req.k)
    return {"document": result}