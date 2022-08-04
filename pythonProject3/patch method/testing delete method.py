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
database_Url = "postgresql://postgres:2402@localhost:5432/postgres"

engine = create_engine(database_Url, echo=True, poolclass=NullPool)

session = sessionmaker(bind=engine)

session = session()


class sagar_info(Base):
    __tablename__ = 'sagar_details'
    Name = Column('name', String)
    Age = Column('age', Integer)
    Mobile_no = Column('mobile', Integer, primary_key=True)


# @app.route('/fetching_sagar_info', methods=['PATCH'])
# def sssss():
#     refer_name = request.args.get('name')
#     update_age = request.args.get('age')
#     session.query(sagar_info).filter(sagar_info.Name == refer_name).update({"Age": update_age})
#     session.commit()
#     return "Age has been updated"
#
#
# app.run()

#
# @app.route('/delete-record', methods=['DELETE'])
# def delete_records_fun():
#         mobile = request.args.get('mobile')
#         session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber == mobile).delete()
#         session.commit()
#         return "Customer record with {} number has been deleted".format(mobile)



