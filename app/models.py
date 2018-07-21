from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class Members(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    nickname = db.Column(db.String(200))
    create_time = db.column(db.DateTime,default=datetime.now)
    update_time = db.Column(db.DateTime,default=datetimec.now,onupdate=datetime.now
    def __init__(self, email, password,nickname):
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.nickname = nicknamecon

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<email %r>' %  self.email

        
