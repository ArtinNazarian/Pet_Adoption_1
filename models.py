from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://media.istockphoto.com/id/1180989037/vector/cartoon-cute-beagle-puppy-vector-character-mascot.jpg?s=612x612&w=0&k=20&c=MLy9ynEYeJNQVUWk4SdESllseqmv0E1zSTeVtrFRRzQ="

db = SQLAlchemy()

def connect_db(app):
    
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    avilable = db.Column(db.Boolean, nullable = False, default=True)

    def pet_image(self):
        return self.photo_url or DEFAULT_IMAGE
