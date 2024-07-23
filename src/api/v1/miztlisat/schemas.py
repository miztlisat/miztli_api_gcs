from pydantic import BaseModel


class CreateMiztlisatSchema(BaseModel):
    altitude: float
    latitude: float
    longitude: float
    temperature: float
    pressure: float
    speed: float
    acceleration: float
    orientation: float
    angle_x: float
    angle_y: float
    angle_z: float
    battery_level: float
    transmission_status: str

class ListMiztliSchema(BaseModel):
    altitude: float
    latitude: float
    longitude: float
    temperature: float
    pressure: float
    speed: float
    acceleration: float
    orientation: float
    angle_x: float
    angle_y: float
    angle_z: float
    battery_level: float
    transmission_status: str
