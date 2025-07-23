from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    """This is user model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Project(db.Model):
    __tablename__ = "projects"
    """This is project model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('projects', lazy=True))

    def __repr__(self):
        return f"<Project {self.title}>"