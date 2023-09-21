from sqlalchemy import Column, ForeignKey, Integer, String, Float
# from sqlalchemy.orm import relationship

from database import Base


class Brand(Base):
    """Model for brands of coffee data"""
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    cost_per_cup = Column(Float)

    # inventory_adjustments = relationship("Inventory", back_populates="inv_adjustments")


class Inventory(Base):
    """Model for inventory adjustment data"""
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("brand.id"))
    inventory = Column(Integer)

    # brand = relationship("Brand", back_populates="brand")
