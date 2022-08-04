import json
import psycopg2
from flask import Flask, request
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import jsonify
import os

# # initilise the app & api
# app = Flask(__name__)
# api = Api(app)
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# # disable sqlalchemy pool using NullPool as by default Postgres has its own pool
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# conn = engine.connect()
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
#
# class heromotorcorp(Base):
#     __tablename__ = "hero_motor_corp"
#     customerName= Column("customer_name", String)
#     mobileNumber = Column("mobile_number", Integer, primary_key=True)
#     emailId = Column("email_id", String)
#     vehicleModel=Column("vehicle_model",String)
#     state=Column("state",String)
#     district=Column("district",String)
#     city=Column("city",String)
#     existingVehicle=Column("existing_vehicle",String)
#     wantTestDrive = Column("want_to_take_a_test_ride", BOOLEAN)
#     dealerState=Column("dealer_state",String)
#     dealerTown=Column("dealer_town",String)
#     dealer=Column("dealer",String)
#     briefAboutEnquery = Column("brief_about_enquiry", String)
#     expectedDateOfPurchase=Column("expected_date_of_purchase", String)
#     gender=Column("gender",String)
#     age = Column("age", Integer)
#     occupation=Column("occupation",String)
#     intendedUsage=Column("intended_usage", String)
#
#
# @app.route('/en-in/reach-us/product-enquiry', methods=['GET'])
# def home():
#     # This is same as below sql
#     # select * from productenquiry;
#     result = session.query(Form).all()
#     result = [item.__dict__ for item in result]
#     for dict_item in result:
#         del dict_item['_sa_instance_state']
#     return json.dumps(result)
#
#
# @app.route('/update-state', methods=['PATCH'])
# def update_state():
#         mobile = request.args.get('mobile')
#         statename = request.args.get('statename')
#         session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber == mobile) \
#             .update({"state": statename})
#         session.commit()
#         return "State has been updated"
#
#
# @app.route('/delete-record', methods=['DELETE'])
# def delete_records_fun():
#         mobile = request.args.get('mobile')
#         session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber == mobile).delete()
#         session.commit()
#         return "Customer record with {} number has been deleted".format(mobile)
#
#
# app.run(debug=False)
#
#
# """


app = Flask(__name__)

Base = declarative_base()
database_url = "postgresql://postgres:2402@localhost:5432/postgres"
# postgress://postgresds:2402@localhost:5432/postgress

engine = create_engine(database_url, echo=True, poolclass=NullPool)

conn = engine.connect()
session = sessionmaker(bind=engine)
session = session()


class subjectstypes(Base):
    __tablename__ = 'subjects_types'
    Name = ('name', String)
    Marks = ('marks', Integer)
    Teacher_name = ('teacher_name', String)
    mobileNumber = Column("mobile_number", Integer, primary_key=True)


@app.route('/fetching_subjects_details', methods=['GET'])
def fun():
    fetch_mobileNumber = request.args.get('mobile')
    results = session.query(subjectstypes).filter(subjectstypes.mobileNumber == fetch_mobileNumber).all()
    return str(results)


app.run()
