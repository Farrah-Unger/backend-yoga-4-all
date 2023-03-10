from app import db

class Reflex(db.Model):
    reflex_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String) #ForeignKey?
    videos=db.Column(db.ARRAY(db.String))
    image= db.Column(db.Text)
    education = db.Column(db.String)
    diaries = db.relationship("Diary", back_populates="reflex") #lazy=True