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
    SrNo=db.Column(db.Integer,primary_key=True)
    Destination=db.Column(db.String)
    Country=db.Column(db.String)
    Climate=db.Column(db.String)
    Budget=db.Column(db.String)
    Description=db.Column(db.String)
    

class TripPlaced(db.Model):
    __tablename__="tripPlaced"
    phoneNo=db.Column(db.Integer,primary_key=True)
    destination=db.Column(db.String,nullable=False)
    