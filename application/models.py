from application.database import db
class User(db.Model):
    __tablename__="user"
    phoneNo=db.Column(db.Integer,primary_key=True)
    fName=db.Column(db.String,nullable=False)
    lName=db.Column(db.String,nullable=False)
    mail=db.Column(db.String,nullable=False,unique=True)
    city=db.Column(db.String)
    district=db.Column(db.String)
    password=db.Column(db.String,unique=True)

class Tour(db.Model):
    __tablename__="tour"
    
    country=db.Column(db.String,primary_key=True)
    destination=db.Column(db.String)
    description=db.Column(db.String)
    cost=db.Column(db.Integer)
    
    

class TripPlaced(db.Model):
    __tablename__="tripPlaced"
    phoneNo=db.Column(db.Integer,primary_key=True)
    destination=db.Column(db.String,nullable=False)
    