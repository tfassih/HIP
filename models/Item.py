from sqlalchemy import URL, Boolean, DateTime, Float, Sequence, Text, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

Base = declarative_base() 

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=True, default=0.00)
    location = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    primary_type = Column(Text, nullable=True)
    
    #PHYSICAL ITEM FIELDS
    physical_type = Column(Text, nullable=True)
    physical_weight = Column(Float, nullable=True)
    physical_weight_unit = Column(Text, nullable=True)
    physical_height = Column(Float, nullable=True)
    physical_height_unit = Column(Text, nullable=True)
    physical_width = Column(Float, nullable=True)
    physical_width_unit = Column(Text, nullable=True)
    physical_length = Column(Float, nullable=True)
    physical_length_unit = Column(Text, nullable=True)
    item_type = Column(Text, nullable=True)

    #DIGITAL ITEM FIELDS
    digital_file_size = Column(Float, nullable=True)
    digital_file_size_unit = Column(Text, nullable=True)
    digital_file_format = Column(Text, nullable=True)

    #CONSUMABLE ITEM FIELDS
    expiration_date = Column(DateTime, nullable=True)

    #ACTIVITY ITEM FIELDS
    scheduled_date = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)
    duration_unit = Column(Text, nullable=True)
    recurring = Column(Boolean, nullable=True)
    activity_type = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
    participants = Column(Text, nullable=True)

    #LINK ITEM FIELDS
    url = Column(Text, nullable=True)

    #LIST ITEM FIELDS
    list = Column(Text, nullable=True)

    #RAW ITEM FIELDS
    raw_data = Column(Text, nullable=True)

    #CUSTOM ITEM FIELDS CAN BE ADDED AS NEEDED, MAY REQUIRE NEW TABLES OR JUST ADDING MORE COLUMNS TO THIS TABLE DEPENDING ON THE TYPE OF CUSTOM DATA BEING ADDED
