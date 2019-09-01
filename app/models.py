from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    img = db.Column(db.BLOB)
    description = db.Column(db.String(128))

    def __repr__(self): '<Img {}>'.format(self.name)

class Box(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    descr = db.Column(db.String(128))
    img_id = db.Column(db.Integer, db.ForeignKey('image.id'))

    def __repr__(self):
        return '<Box {}>'.format(self.name)
