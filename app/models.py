from . import db
from werkzeug.security import generate_password_hash


class Members(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    nickname = db.Column(db.String(200))
    create_time = db.column(db.DateTime)
    update_time = db.Column(db.DateTime)
    def __init__(self, email, password,nickname):
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.nickname = nickname

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

        
class Transfer(db.Model):
     __tablename__ = 'transfer'

     id = db.Column(db.Integer, primary_key=True)
     tran_id = db.Column(db.Integer)
     email = db.Column(db.String(30))
     phone = db.Column(db.String(20))
     currency =  db.Column(db.String(20))
     amount = db.Column(db.Float)
     fee = db.Column(db.Float)
     address = db.Column(db.String(255))
     withdraw_time = db.Column(db.DateTime)
     audit_time = db.Column(db.DateTime)
     transfer_time = db.Column(db.DateTime)
     status = db.Column(db.Boolean)
     txid = db.Column(db.String(255))
     tran_status = db.Column(db.Boolean)

     def __init__(self,tran_id,email,phone,currency,amount,fee,address,withdraw_time,audit_time):
         self.tran_id = tran_id
         self.email = email
         self.phone = phone
         self.currency = currency
         self.amount = amount
         self.fee = fee
         self.address = address
         self.withdraw_time = withdraw_time
         self.audit_time = audit_time
        # self.transfer_time = transfer_time
         self.status = False
         self.txid = ''
         self.tran_status = False