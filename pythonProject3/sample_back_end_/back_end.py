import string
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

Base = declarative_base()
database_url = "postgresql://postgres:2402@localhost:5432/postgres"

# disable sqlalchemy pool using NullPool as by default Postgres has its own pool
engine = create_engine(database_url, echo=True, poolclass=NullPool)

Session = sessionmaker(bind=engine)
session = Session()


# original table
class student_info(Base):
    __tablename__ = 'student_info'
    CustomerName = Column("name", String)
    Gender = Column("gender", String)
    Age = Column("age", Integer)
    mobile = Column("mobile", Integer, primary_key=True)
    email_id = Column("email_id", String)


@app.route('/fetch-student-info', methods=['GET'])
def home():
    results = session.query(student_info).all()
    results = [item.__dict__ for item in results]


    return str(results)


app.run(debug=True)

# disable sqlalchemy pool using NullPool as by default Postgres has its own pool
#  engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
#  Session = sessionmaker(bind=engine)
#  session = Session()
#
#
#  original table
#
#
#
# class employee_details(Base):
#     __tablename__ = 'employee_details'
#     name = Column("name", String)
#     id = Column("id", Integer, primary_key=True)
#     bloodgroup = Column("bloodgroup", String)
#     salary = Column("salary", Integer, )
#
#
#
# @app.route('/fetch-employee-details', methods=['GET'])
# def home():
#     results = session.query(employee_details).all()
#     results = [item.__dict__ for item in results]
#     return str(results)
#
#
# app.run(debug=True)
#
#
# app = Flask(__name__)
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# # disable sqlalchemy pool using NullPool as by default Postgres has its own pool
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# # original table
#
#
# class car_details(Base):
#     __tablename__ = 'car_details'
#     color = Column("color", String)
#     name = Column("name", String)
#     price = Column("price", Integer, primary_key=True)
#     topspeed = Column("topspeed", Integer)
#     mobile_no = Column("mobile_no", Integer, primary_key=True)
#
#
# @app.route('/fetch-car-details', methods=['GET'])
# def home():
#     results = session.query(car_details).all()
#     results = [item.__dict__ for item in results]
#     return str(results)
#
#
# app.run(debug=True)
#
#
# app = Flask(__name__)
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# # disable sqlalchemy pool using NullPool as by default Postgres has its own pool
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# # original table
#
#
# class hero_motor_corp(Base):
#     __tablename__ = 'hero_motor_corp'
#     customer_name = Column("customer_name", String)
#     mobile_no = Column("mobile_no", Integer)
#     vehicle_model = Column("vehicle_model", String, primary_key=True)
#     state = Column("state", String)
#     district = Column("district", String, primary_key=True)
#     pincode = Column("pincode", Integer)
#     email_id = Column("email_id", String)
#     expected_date_to_purchase = Column("expected_date_to_purchase", Integer)
#     lead_generated_date = Column("lead_generated_date", Integer)
#     sr_no = Column("sr_no", Integer)
#
#
# @app.route('/fetch-hero-motor-corp', methods=['GET'])
# def home():
#     results = session.query(hero_motor_corp).all()
#     results = [item.__dict__ for item in results]
#     return str(results)
#
#
# app.run(debug=True)
#
# app = Flask(__name__)
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# # disable sqlalchemy pool using NullPool as by default Postgres has its own pool
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# # original table
#
#
# class acc_opening_form(Base):
#     __tablename__ = 'acc_opening_form'
#     name = Column("name", String)
#     mobile_no = Column("mobile_no", Integer)
#     aadar_no = Column("aadar_no", Integer, primary_key=True)
#     pancard = Column("pancard", Integer)
#     pincode = Column("pincode", Integer)
#     account_type = Column("account_type", String)
#
#
# @app.route('/fetch-acc-opening-form', methods=['GET'])
# def home():
#     results = session.query(acc_opening_form).all()
#     results = [item.__dict__ for item in results]
#     return str(results)
#
#
# app.run()
#
#
# app = Flask(__name__)
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# # disable sqlalchemy pool using NullPool as by default Postgres has its own pool
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # original table
# class subjects_types(Base):
#     __tablename__ = 'subjects_types'
#     name = Column("name", String)
#     marks = Column("marks", Integer)
#     teacher_name = Column("teacher_name", String, primary_key=True)
#
#
# @app.route('/fetch-subjects-types-info', methods=['GET'])
# def home():
#     results = session.query(subjects_types).all()
#     return str(results)
#
#
# app.run(debug=True)
#
#
#
#

#
#
#
# app = Flask(__name__)
#
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# # disable sqlalchemy pool using NullPool as by default Postgres has its own pool
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # original table
# class studentinfo(Base):
#     __tablename__ = 'student_info'
#     name = Column("name", String)
#     Gender = Column("gender", String)
#     Age = Column("age", Integer)
#     mobile = Column("mobile", Integer, primary_key=True)
#
#
# @app.route('/fetch-student-info', methods=['GET'])
# def home():
#     results = session.query(studentinfo).all()
#     results = [item.__dict__ for item in results]
#
#
#     for dict_item in results:
#         del dict_item ['_sa_instance_state']
#
#     return json.dumps(results)
#
# app.run(debug=True)
#


#
# session.query(StudentInfo).all()
#
# session.query(StudentInfo).filter(StudentInfo.mobile==mobile).all()
#
# session.query(StudentInfo).filter(and_(StudentInfo.mobile==mobile,
#                                        StudentInfo.name==name)).all()
#
# session.query(StudentInfo).filter(or_(StudentInfo.mobile==mobile,
#                                        StudentInfo.name==name)).all()
#
# -----------------------------------------------------------------------------------------------
#
#
# myList = [{1:34,4:56},{5:76, 1:89}]
# for item in myList:
#     print(item)              # {1:34,4:56}
#     del item[1]
#
# print(myList')
#
# #http://127.0.0.1:5000/fetch-student-info/mobile-specific?mobile=1&name=Ramesh
# @app.route('/fetch-student-info/mobile-specific', methods=['GET'])
# def home():
#     mobile = request.args.get('mobile')
#     response = session.query(StudentInfo).filter(StudentInfo.mobile==mobile).all()
#     for dict_item in response:
#         del dict_item['__sainstance']
#     return json.dumps(response)







Class rasdfdd(self, name, age)



