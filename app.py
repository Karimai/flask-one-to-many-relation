from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

class Owner(db.Model):
    __tablename__ = "owner"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    pets = db.relationship("Pet", backref="owner")

class Pet(db.Model):
    __tablename__ = "pet"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"))

if __name__ == "__main__":
    app.run()
