from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

## For those how come to the comment session with create_all() to create database error 1:33:45.
# As per the new version, this is the fix:
# def create_database(app):
#     if not path.exists('website/'+ DB_NAME):
#         with app.app_context():
#             db.create_all()
#         print("Created Database!")

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
