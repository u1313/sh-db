from app import db

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    img = db.Column(BLOB)
    description = db.Column(db.String(128))
    
    def __repr__(self): '<Img {}>'.format(self.name)

class Boxes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128))

    def __repr__(self):
        return '<Box {}>'.format(self.name)
