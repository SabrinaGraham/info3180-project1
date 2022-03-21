from . import db
from werkzeug.security import generate_password_hash


class Properties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    bedroom = db.Column(db.String(80))
    bathroom = db.Column(db.String(80))
    location = db.Column(db.String(80))
    price = db.Column(db.Integer)
    propertyType= db.Column(db.String(80))
    photo_name=db.Column(db.String(80))
    
    
    """def __init__(self, title, description, bedroom, bathroom, location, price, propertyType, photo_name):
        self.title=title
        self.description=description
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.location = location
        self.price= price
        self.propertyType= propertyType
        self.photoname = photoname"""
    
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
        return '<User %r>' % (self.username)
