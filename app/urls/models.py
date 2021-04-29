from app.database import db, BaseModelMixin
from datetime import datetime

class Url(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    original_url = db.Column(db.String)
    clicks = db.Column(db.Integer, default=0)

    def __repr__(self):
        return(
            f'Id: {self.id}, '
            f'Created: {self.created}, '
            f'Original URL: {self.original_url}, '
            f'Clicks: {self.clicks}'
        )

    def __str__(self):
        return(
            f'Id: {self.id}, '
            f'Created: {self.created}, '
            f'Original URL: {self.original_url}, '
            f'Clicks: {self.clicks}'
        )