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
    Expected_date_to_buy = Column("expected_date_to_buy", Date)
    sent_to_dealer = Column("sent_to_dealer", BOOLEAN)




@app.route('/fetching_date', methods=['GET'])
def rrr():
    start_date = request.args.get("startdate")
    end_date = request.args.get("enddate")
    result = session.query(hero_motor_corp_details). \
        filter(and_(hero_motor_corp_details.Expected_date_to_buy >= start_date,\
                    hero_motor_corp_details.Expected_date_to_buy <= end_date)).all()
    result = [item.__dict__ for item in result]
    for item in result:
        item.pop('_sa_instance_state')
    return str(result)

app.run()


session.query(hero_motor_corp_details).filter(hero_motor_corp_details.sent_to_dealer == False).all()

app.run()

# #
# @app.route('/fetching_with_date', methods=['GET'])
# def historic_leads():
#     start_date = request.args.get("startdate")
#     end_date = request.args.get("enddate")
#     result = session.query(hero_motor_corp_details).\
#         filter(and_(hero_motor_corp_details.Expected_date_to_buy >= start_date,\
#                     hero_motor_corp_details.Expected_date_to_buy <= end_date)).all()
#     result = [item.__dict__ for item in result]
#     for item in result:
#         item.pop('_sa_instance_state')
#     return str(result)
# session.query(hero_motor_corp_details).filter(hero_motor_corp_details.sent_to_dealer == False ).all()
#
# @app.route('/fetching_with_dates', methods=['GET'])
# def www():
#     start_date = request.args.get("startdate")
#     end_date = request.args.get("enddate")
#     result = session.query(hero_motor_corp_details). \
#         filter(and_(hero_motor_corp_details.Expected_date_to_buy >= start_date,\
#                     hero_motor_corp_details.Expected_date_to_buy <= end_date)).all()
#     result = [item.__dict__ for item in result]
#     for item in result:
#         item.pop('_sa_instance_state')
#     return str(result)
#
#
# session.query(hero_motor_corp_details).filter(hero_motor_corp_details.sent_to_dealer == False).all()
#
# app.run()




# @app.route('/dasda', methods=['GET'])
# def sdds():
#     start_date = request.args.get('startdate')
#     end_date = request.args.get('enddate')
#     result = session.query(hero_motor_corp_details).filter(and_(hero_motor_corp_details.Expected_date_to_buy <= start_date,\
#                                                                 hero_motor_corp_details.Expected_date_to_buy >= end_date)).all()
#     result = item.__dict__ for item in result
#         item.pop('_sa_instance_state')
#         return str(result)
#
# session.query(hero_motor_corp_details).filter(hero_motor_corp_details.sent_to_dealer == False).all()
#
# app.run()