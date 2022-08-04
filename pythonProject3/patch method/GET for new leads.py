import json
import psycopg2
from flask import Flask, request
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

app = Flask(__name__)

Base =  declarative_base()
databaseUrl = "postgres://postgres:2402@localhost:5432/postgres"
engine = create_engine(databaseUrl, echo=True, poolclass=NullPool)

session = sessionmaker(bind=engine)

session = session()

class Banking_details(Base):
    __tablename__ = 'acc_opening_form'
    name = Column('name', String)
    mobile_no = Column('mobile_no', Integer, primary_key=True)
    aadar_no = Column('aadar_no', Integer)
    pancard = Column('pancard', String)
    Pincode = Column('pincode', Integer)
    account_type = Column('account_type', String)
    acc_activation = Column('acc_activation',BOOLEAN)
    act_date = Column('act_date', Date)

@app.route('/fetching_new_leads', methods=['GET'])
def sss():
    take_pincode = request.args.get('pincode')
    result = session.query(Banking_details).filter(Banking_details.Pincode == take_pincode).\
        filter(Banking_details.sent_to_dealer == False).all()
    convertdict = [item.__dict__ for item in result]
    mobile_storage = []




