from sqlalchemy import Boolean, Float, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from models.Item import Base, Item

Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))   
    item = relationship("Item", back_populates="inventory")

class ItemLibrary(Base):
    __tablename__ = 'item_library'
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))   
    item = relationship("Item", back_populates="item_library")
