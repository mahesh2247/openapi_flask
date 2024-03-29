from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class People(db.Model):
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200), primary_key=True)

def __repr__(self):
    return '<People %r>' %self.fname

def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
