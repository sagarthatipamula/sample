import json
import psycopg2
from flask import Flask, request
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

# app = Flask(__name__)
#
# Base = declarative_base()
# database_url = "postgresql://postgres:2402@localhost:5432/postgres"
#
# engine = create_engine(database_url, echo=True, poolclass=NullPool)
#
# session = sessionmaker(bind=engine)
# session = session()
#
#
# class hero_motor_corp_details(Base):
#     __tablename__ = 'hero_motor_corp'
#     Customer_name = Column("customer_name", String)
#     mobileNo = Column("mobile_no", Integer, primary_key=True)
#     vehicle_model = Column("vehicle_model", String)
#     state = Column("state", String)
#     district = Column("district", String)
#     pincode = Column("pincode", Integer)
#     email_id = Column("email_id", String)
#     expected_date_to_purchase = Column("expected_date_to_purchase", Integer)
#     lead_generated_date = Column("lead_generated_date", Integer)
#     sr_no = Column("sr_no", Integer)
#     sent_to_dealer = Column("sent_to_dealer", BOOLEAN)
#
#
#
#
#
# @app.route('/details', methods=['GET'])
# def home():
#     customer_name = request.args.get("customer_name")
#     result = session.query(hero_motor_corp_details). \
#         filter(hero_motor_corp_details.sent_to_dealer == False,
#                hero_motor_corp_details.Customer_name == customer_name).all()
#     print(type(result))
#     result = [item.__dict__ for item in result]
#     mobileno_container = []
#     for item in result:
#         item.pop('_sa_instance_state')
#         mobileno_container.append(item.get('mobileNo'))
#     enable_sent_flag(mobileno_container)
#     return json.dumps(result)
#
#
# def enable_sent_flag(mobileno_container):
#     print("Container {}".format(mobileno_container))
#     for mobileno in mobileno_container:
#         session.query(hero_motor_corp_details).filter(hero_motor_corp_details.mobileNo == mobileno) \
#             .update({"sent_to_dealer": True})
#         session.commit()
#
# app.run()

#
#


app = Flask(__name__)

Base = declarative_base()
database_url = "postgresql://postgres:2402@localhost:5432/postgres"

engine = create_engine(database_url, echo=True, poolclass=NullPool)

conn = engine.connect()

session = sessionmaker(bind=engine)
session = session()


class hero_motor_corp_details(Base):
    __tablename__ = 'hero_motor_corp'
    Customer_name = Column("customer_name", String)
    mobileNo = Column("mobile_no", Integer, primary_key=True)
    vehicle_model = Column("vehicle_model", String)
    State = Column("state", String)
    District = Column("district", String)
    pincode = Column("pincode", Integer)
    email_id = Column("email_id", String)
    expected_date_to_purchase = Column("expected_date_to_purchase", Integer)
    lead_generated_date = Column("lead_generated_date", Integer)
    sr_no = Column("sr_no", Integer)
    sent_to_dealer = Column("sent_to_dealer", BOOLEAN)


@app.route('/fetching_date', methods=['GET'])
def fun():
    fetch_District = request.args.get("district")
    result = session.query(hero_motor_corp_details). \
        filter(hero_motor_corp_details.District == fetch_District) \
        .filter(hero_motor_corp_details.sent_to_dealer == False).all()
    print(result)
    result = [item.__dict__ for item in result]
    mobileno_container = []
    for item in result:
        print("item is ", item.get('mobileNo'))
        item.pop('_sa_instance_state')
        mobileno_container.append(item.get('mobileNo'))
        print("mobile_container is ", mobileno_container)
    enable_sent_flag(mobileno_container)
    return json.dumps(result)


def enable_sent_flag(mobileno_container):
    print("Container {}".format(mobileno_container))
    for mobileno in mobileno_container:
        print("mobile no is ", mobileno)
        session.query(hero_motor_corp_details).filter(hero_motor_corp_details.mobileNo == mobileno) \
            .update({"sent_to_dealer": True})
        session.commit()


app.run()
