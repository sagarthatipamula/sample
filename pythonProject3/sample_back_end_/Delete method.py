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



class studentinfo(Base):
    __tablename__ = 'student_info'
    name = Column("name", String)
    Gender = Column("gender", String)
    Age = Column("age", Integer)
    mobile_no = Column("mobile", Integer, primary_key=True)


@app.route('/delete-record', methods=['DELETE'])
def delete_records_fun():
    delete_name = request.args.get('name')
    delete_age = request.args.get('age')
    session.query(studentinfo).filter(studentinfo.name == delete_name).delete()
    session.commit()
    return "Customer record with {} number has been deleted".format(mobile)




app.run(debug=False)
