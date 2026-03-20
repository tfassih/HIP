from sqlalchemy import Boolean, Float, Sequence, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base() ############NEEDS REDONE THE TYPES ARE FUCKED UP

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=True, default=0.00)
    location = Column(String, nullable=True)
    description = Column(String)
    # primary_type_id = Column(Integer, ForeignKey('primary_types.id'))
    # primary_type = relationship("PrimaryType", back_populates="items")

# class PrimaryType(Base):
#     __tablename__ = 'primary_types'
    
#     id = Column(Integer, Sequence('primary_type_id_seq'),primary_key=True)
#     name = Column(String, nullable=False)
    
#     # items = relationship("Item", back_populates="primary_type")

# class PhysicalType(Base):
#     __tablename__ = 'physical_types'
    
#     id = Column(Integer, Sequence('physical_type_id_seq'), primary_key=True)
#     weight = Column(Float, nullable=True)
#     weight_unit = Column(String, nullable=True)
#     height = Column(Float, nullable=True)
#     height_unit = Column(String, nullable=True)
#     width = Column(Float, nullable=True)
#     width_unit = Column(String, nullable=True)
#     depth = Column(Float, nullable=True)
#     depth_unit = Column(String, nullable=True)
#     item_type = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="physical_types")

# class DigitalType(Base):
#     __tablename__ = 'digital_types'
    
#     id = Column(Integer, Sequence('digital_type_id_seq'), primary_key=True)
#     file_size = Column(Float, nullable=True)
#     file_size_unit = Column(String, nullable=True)
#     file_format = Column(String, nullable=True)
#     item_type = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="digital_types")

# class ConsumableType(Base):
#     __tablename__ = 'consumable_types'
    
#     id = Column(Integer, Sequence('consumable_type_id_seq'), primary_key=True)
#     expiration_date = Column(String, nullable=True)
#     item_type = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="consumable_types")

# class ActivityType(Base):
#     __tablename__ = 'activity_types'
    
#     id = Column(Integer, Sequence('activity_type_id_seq'), primary_key=True)
#     scheduled_date = Column(String, nullable=True)
#     duration = Column(Integer, nullable=True)
#     duration_unit = Column(String, nullable=True)
#     recurring = Column(Boolean, nullable=True)
#     activity_type = Column(String, nullable=True)
#     location = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="activity_types")

# class LinkType(Base):
#     __tablename__ = 'link_types'
    
#     id = Column(Integer, Sequence('link_type_id_seq'), primary_key=True)
#     url = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="link_types")

# class ListType(Base):
#     __tablename__ = 'list_types'
    
#     id = Column(Integer, Sequence('list_type_id_seq'), primary_key=True)
#     items_list = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="list_types")

# class RawType(Base):
#     __tablename__ = 'raw_types'
    
#     id = Column(Integer, Sequence('raw_type_id_seq'), primary_key=True)
#     raw_data = Column(String, nullable=True)

#     # items = relationship("Item", back_populates="raw_types")

# class CustomType(Base):
#     __tablename__ = 'custom_types'
    
#     id = Column(Integer, Sequence('custom_type_id_seq'), primary_key=True)
#     # items = relationship("Item", back_populates="custom_types")