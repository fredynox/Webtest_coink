
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.Integer)

    def __init__(self, name, email, phone):
        super().__init__()
        self.name = name
        self.email = email
        self.phone = phone

    
    def __str__(self):
        return " (ID: {}, Nombre: {}, E-Mail: {}, Teléfono: {})".format(
            self.rowid,
            self.name,
            self.email,
            self.phone
        )
    
    def serialize(self):
        return {
            "rowid": self.rowid, 
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
