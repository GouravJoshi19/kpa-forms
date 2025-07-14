from sqlalchemy import Column, Integer, String, Date, JSON
from .database import base

class WheelSpecification(base):
    __tablename__ = 'wheel_specifications'
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, nullable=False)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(Date, nullable=False)
    fields = Column(JSON, nullable=False)
    status = Column(String, default="Saved")

    