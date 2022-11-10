
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String,
                          default="https://socialistmodernism.com/wp-content/uploads/2017/07/placeholder-image.png?w=640", nullable=True)
    age = db.Column(db.String, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, default=True)
