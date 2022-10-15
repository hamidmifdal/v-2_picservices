from app import app ,db

class Products(db.Model):
    __tablename__ = 'Products'
    id    = db.Column(db.Integer, primary_key = True)
    img   = db.Column(db.LargeBinary)
    nm    = db.Column(db.String(999))
    title = db.Column(db.String(999))
    def __repr__(self,id,img,nm,title):
        self.id    = id
        self.img   = img
        self.nm    = nm
        self.title = title