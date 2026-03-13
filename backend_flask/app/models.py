from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.String(80), nullable=False)
    
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    def __repr__(self):
        return '<User %r>' % self.name