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

engine = create_engine(database_url, echo=True, poolclass=NullPool)

session = sessionmaker(bind=engine)
session = session()


class tv_sepecifications(Base):
    __tablename__ = 'specifications'
    In_the_ox = Column("in_the_ox", String)
    Model_name = Column("model_name", String, primary_key=True)
    Hdmicolor = Column("color", String)
    Display_size = Column("display_size", String)
    Screen_type = Column("screen_type", String)
    Hd_technology_resolution = Column("hd_technology_resolution", String)
    Smart_tv = Column("smart_tv", String)
    Hdmi = Column("hdmi", Integer)
    Usb = Column("usb", Integer)
    Built_in_wi_fi = Column("built_in_wi_fi", Integer)
    Launch_year = Column("launch_year", String)
    Wall_mount_included = Column("wall_mount_included", String)
    Led_display_type = Column("led_display_type", Integer)
    Refresh_rate = Column("refresh_rate", Integer)
    Number_of_speakers = Column("number_of_speakers", String)
    Speaker_output_rms = Column("speaker_output_rms", String)
    Other_audio_features = Column("other_audio_features", String)

#
# @app.route('/fetching_specification_of_tv', methods=['GET'])
# def fun():
#     request_usb = request.args.get('usb')
#     request_hdmi = request.args.get('hdmi')
#     results = session.query(tv_sepecifications).filter(and_(tv_sepecifications.Usb == request_usb, \
#                                                             tv_sepecifications.Hdmi == request_hdmi)).all()
#     converting_dict = [item.__dict__ for item in results]
#
#     for item_dict in converting_dict:
#         del item_dict['_sa_instance_state']
#     return json.dumps(converting_dict)

@app.route('/fetching_with_update_year', methods=['PATCH'])
def update_year():
    update_Hdmi = request.args.get('Hdmi')
    update_Launch_year = request.args.get('Launch_year')

    session.query(tv_sepecifications).filter(tv_sepecifications.Hdmi == update_Hdmi).\
        update({"Launch_year": update_Launch_year})
    session.commit()

    return "Launch_year has been updated"




app.run()
