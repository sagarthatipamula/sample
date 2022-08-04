import json
from datetime import datetime
import psycopg2
from flask import Flask

from flask import request

from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import jsonify
import os
from datetime import date

app = Flask(__name__)

Base = declarative_base()
database_url = "postgresql://postgres:2402@localhost:5432/postgres"

engine = create_engine(database_url, echo=True, poolclass=NullPool)

conn = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()


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
    Sr_no = Column("sr_no", Integer)
    Expected_date_to_buy = Column("expected_date_to_buy", Date)
    Sent_to_dealer = Column("sent_to_dealer", BOOLEAN)
    Age = Column("age", Integer)
    Gender = Column("gender", String)


class cus_details(Base):
    __tablename__ = 'customer_details'
    District = Column("district", String)
    mobileNo = Column("mobile_no", Integer, primary_key=True)
    Age = Column("age", Integer)
    Gender = Column("gender", String)
    Isnewcustomer = Column("snewcustomer", BOOLEAN)


@app.route('/update-customer', methods=['PATCH'])
def update_customer_info():
    fetch_district = request.args.get('district')
    result = session.query(hero_motor_corp_details).filter(hero_motor_corp_details.District == fetch_district).all()
    result2 = [item.__dict__ for item in result]
    print(result2)
    for item in result2:
        del item['_sa_instance_state']
    set_customer_status(mobile)

    return json.dumps(result2)


def set_customer_status(mobile):
    customer_name = session.query(hero_motor_corp_details.Customer_name).filter(
        hero_motor_corp_details.District == mobile).all()
    print("name is", customer_name)
    session.query(cus_details).filter(cus_details.Customer_name == customer_name).update({'Isnewcustomer': False})
    session.commit()


app.run()
