from marshmallow import Schema, fields
from typing import Dict

class Movie:
    id: int
    title: str

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def toJSON(self) -> Dict:
        return {"id": self.id, "title": self.title}
    
    def __repr__(self) -> str:
        return f"<Movie(id={self.id}, title={self.title})>"
    
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()