from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class ClUser(db.Model, SerializerMixin):
    __tablename__ = "cl_user"
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Person(db.Model, SerializerMixin):
    __tablename__ = "person"
    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    dob = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    details = relationship("PersonDtl", backref="person", lazy=True)
    accounts = relationship("PersonBankAccount", backref="person", lazy=True)

class Customer(db.Model, SerializerMixin):
    __tablename__ = "customer"
    id = db.Column(db.BigInteger, primary_key=True)
    person_id = db.Column(db.BigInteger, db.ForeignKey("person.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PersonDtl(db.Model, SerializerMixin):
    __tablename__ = "person_dtl"
    id = db.Column(db.BigInteger, primary_key=True)
    person_id = db.Column(db.BigInteger, db.ForeignKey("person.id"))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PersonBankAccount(db.Model, SerializerMixin):
    __tablename__ = "person_bank_account"
    id = db.Column(db.BigInteger, primary_key=True)
    person_id = db.Column(db.BigInteger, db.ForeignKey("person.id"))
    bank_name = db.Column(db.String(255))
    account_number = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
