import json
from datetime import datetime
import psycopg2
from flask import Flask

from flask import request

from flask_restful import Api

from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import jsonify
import os
from datetime import date
app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:2402@localhost:5432/postgres"

engine = create_engine(database_url, echo=True, poolclass=NullPool)

conn = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()



class Student_detailing(Base):
    __tablename__ = "students_details"
    CustomerName = Column("name", String)
    Age = Column("age", Integer)
    Gender = Column("gender", String)
    Mobile_No = Column("mobile_no", Integer, primary_key=True)
    Fee_Check_List = Column("fee_check_list", String)


# @app.route('/fetch_all_student_details', methods=['GET'])
# def students():
#     response = session.query(Student_detailing).all()
#     result = [item.__dict__ for item in response]
#     for item in result:
#         del item['_sa_instance_state']
#
#     return json.dumps(result)
#
#
# @app.route('/fetch_one_student_mob_no', methods=['GET'])
# def mob():
#     MOBILE = request.args.get('mobile_no')
#     result1 = session.query(Student_detailing).filter(Student_detailing.Mobile_No == MOBILE)
#     result2 = [item.__dict__ for item in result1]
#     for item in result2:
#         del item['_sa_instance_state']
#
#     return json.dumps(result2)


@app.route('/update_fee_paid', methods=['GET'])
def fees():
    MOBILE = int(request.args.get('mobile_no'))
    fee_paid = request.args.get('fee_check_list')
    result2 = session.query(Student_detailing).filter(Student_detailing.Mobile_No == MOBILE) \
        .update({'Fee_Check_List': fee_paid})
    session.commit()
    return {'mobile': "mobile_no", "status": "Fee paid", "error": ""}

#after executing the results will update in data base


@app.route('/unpaid_fee_list', methods=['GET'])
# def unpaid_fee():
#     result3 = session.query(Student_detailing).filter(Student_detailing.Fee_Check_List=='no')
#     proper_format = [item.__dict__ for item in result3]
#     for item in proper_format:
#         del item['_sa_instance_state']
#     return json.dumps(proper_format)
#
#
# @app.route('/paid_fee_list', methods=['GET'])
# def paid_fee():
#     result4 = session.query(Student_detailing).filter(Student_detailing.Fee_Check_List=='yes')
#     proper_statement = [item.__dict__ for item in result4]
#     for item in proper_statement:
#         del item['_sa_instance_state']
#     return json.dumps(proper_statement)


app.run()

