from pydantic import StrictInt
from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class Metadata(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
class docs_input(BaseModel):
    text : str = Field(...,min_length=10, max_length=20000000)

class docs_response(BaseModel):
    ID: StrictInt
    text: str
    MetaData : Metadata
    

