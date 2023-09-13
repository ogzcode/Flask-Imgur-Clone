from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique = True)
    email = db.Column(db.String(120), index=True, unique = True)
    password_hash = db.Column(db.String(128))
    profile_pic = db.Column(db.String(120))
    about = db.relationship('UserAbout', backref='author', lazy='dynamic')
    images = db.relationship('Image', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class UserAbout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.Text)
    website = db.Column(db.String(120))
    location = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UserAbout {}>'.format(self.about)
    
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), index=True, unique = True)
    title = db.Column(db.String(120), index=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Image {}>'.format(self.path)
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    user = db.relationship("User", backref="comments")

    def __repr__(self):
        return '<Comment {}>'.format(self.content)
    

