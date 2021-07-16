from application import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    team = db.Column(db.String(20))
    runs = db.Column(db.String(20))