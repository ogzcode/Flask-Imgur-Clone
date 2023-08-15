from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique = True)
    email = db.Column(db.String(120), index=True, unique = True)
    password_hash = db.Column(db.String(128))
    images = db.relationship('Image', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), index=True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Image {}>'.format(self.name)