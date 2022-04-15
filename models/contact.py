from db.db import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(50), nullable=True)

    def __init__(self, name, email, subject, message, date=None) -> None:
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.date = date

    def __repr__(self) -> str:
        return f"Contact({self.id}, {self.name}, '{self.email}', '{self.subject}', '{self.message}', '{self.date}')"