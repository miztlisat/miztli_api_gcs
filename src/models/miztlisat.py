
from sqlalchemy import Column, Float, Text

from models.base_model import BaseModelClass


class Miztlisat(BaseModelClass):
    __tablename__ = "miztlisat"

    altitude = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    temperature = Column(Float)
    pressure = Column(Float)
    speed = Column(Float)
    acceleration = Column(Float)
    orientation = Column(Float)
    angle_x = Column(Float)
    angle_y = Column(Float)
    angle_z = Column(Float)
    battery_level = Column(Float)
    transmission_status = Column(Text)
