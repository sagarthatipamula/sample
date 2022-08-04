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
class studentinfo(Base):
    __tablename__ = 'student_info'
    name = Column("name", String)
    Gender = Column("gender", String)
    Age = Column("age", Integer)
    mobile_no = Column("mobile", Integer, primary_key=True)

# @app.route('/Update_name', methods=['PATCH'])
# def update():
#     update_mobile = request.args.get('mobile')
#     update_name = request.args.get('name')
#     session.query(studentinfo).filter(studentinfo.mobile_no == update_mobile).update({"name": update_name})
#     session.commit()
#     return "name has been updated"

# @app.route('/Update_name', methods=['PATCH'])
# def update():
#     update_age = request.args.get('age')
#     update_name = request.args.get('name')
#     session.query(studentinfo).filter(studentinfo.Age == update_age).update({"name": update_name})
#     session.commit()
#     return "name has been updated"


# @app.route('/Update_mobile_num', methods=['PATCH'])
# def update():
#     update_name = request.args.get('name')
#     update_mobile_num = request.args.get('mobile_no')
#     session.query(studentinfo).filter(studentinfo.name == update_name).update({"mobile_no": update_mobile_num})
#     session.commit()
#     return "name has been updated"


@app.route('/Update_mobile_nos', methods=['PATCH'])
def update1():
    update_gender = request.args.get('gender')
    update_mobile_nos = request.args.get('mobile_nos')
    session.query(studentinfo).filter(studentinfo.gender == update_gender).update({"mobile_nos": update_mobile_nos})
    session.commit()
    return "name has been updated"

@app.route('/delete-record', methods=['DELETE'])
def delete_records_fun():
        mobile = request.args.get('mobile')
        session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber == mobile).delete()
        session.commit()
        return "Customer record with {} number has been deleted".format(mobile)



app.run(debug=False)
