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
# class tv_sepecifications(Base):
#     __tablename__ = 'specifications'
#     In_the_ox = Column("in_the_ox", String)
#     Model_name = Column("model_name", String, primary_key=True)
#     Hdmicolor = Column("color", String)
#     Display_size = Column("display_size", String)
#     Screen_type = Column("screen_type", String)
#     Hd_technology_resolution = Column("hd_technology_resolution", String)
#     Smart_tv = Column("smart_tv", String)
#     Hdmi = Column("hdmi", Integer)
#     Usb = Column("usb", Integer)
#     Built_in_wi_fi = Column("built_in_wi_fi", Integer)
#     Launch_year = Column("launch_year", String)
#     Wall_mount_included = Column("wall_mount_included", String)
#     Led_display_type = Column("led_display_type", Integer)
#     Refresh_rate = Column("refresh_rate", Integer)
#     Number_of_speakers = Column("number_of_speakers", String)
#     Speaker_output_rms = Column("speaker_output_rms", String)
#     Other_audio_features = Column("other_audio_features", String)


#
# @app.route('/fetching_with_update_year', methods=['PATCH'])
# def update_year():
#     update_Hdmi = request.args.get('Hdmi')
#     update_Launch_year = request.args.get('Launch_year')
#
#     session.query(tv_sepecifications).filter(tv_sepecifications.Hdmi == update_Hdmi).\
#         update({"Launch_year": update_Launch_year})
#     session.commit()
#
#     return "Launch_year has been updated"
#
#
#
#
# app.run()
#
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
# postgress://postgresds:2402@localhost:5432/postgress

engine = create_engine(database_url, echo=True, poolclass=NullPool)

session = sessionmaker(bind=engine)
session = session()


class subjectstypes(Base):
    __tablename__ = 'subjects_types'
    Name = Column('name', String)
    Marks = Column('marks', Integer)
    Teacher_name = Column('teacher_name', String)
    mobileNumber = Column("mobile", Integer, primary_key=True)


@app.route('/fetching_subjects_details', methods=['PATCH'])
def fun():
    fetch_name = request.args.get('name')
    updateTeacher_name = request.args.get('teacher_name')
    session.query(subjectstypes).filter(subjectstypes.Name == fetch_name).update({"Teacher_name": updateTeacher_name})

    session.commit()
    return "teacher_name has been updated"


app.run()
