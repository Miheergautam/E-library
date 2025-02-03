from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    pdf_url: Optional[str] = None 