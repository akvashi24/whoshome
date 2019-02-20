from app import db

class Resident(db.Model):
    __tablename__ = 'residents'

    mac = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    is_home = db.Column(db.Boolean())
    is_confirmed = db.Column(db.Boolean())

    def __init__(self, mac, name, is_home=False, is_confirmed=False):
        self.mac = mac
        self.name = name
        self.is_home = is_home
        self.is_confirmed = is_confirmed
