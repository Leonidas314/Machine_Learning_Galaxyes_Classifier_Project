from datetime import datetime
from ..db import db

class ImageModel(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, filename: str, category: str, creation_date: datetime | None = None) -> None:
        super().__init__()
        self.filename = filename
        self.category = category
        self.creation_date = creation_date or datetime.utcnow()
