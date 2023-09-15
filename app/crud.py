from sqlalchemy.orm import Session

import app.db_models as db_models, app.schemas as schemas


def get_brand(db: Session, brand_id: int):
    """Returns the specified brand of coffee"""
    return db.query(db_models.Brand).filter(db_models.Brand.id == brand_id).first()


def get_brand_by_name(db: Session, brand_name: str):
    """Returns the specified brand of coffee, looked up by name"""
    return db.query(db_models.Brand).filter(db_models.Brand.name == brand_name).first()


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    """Returns all brands of coffee, paginated by 100"""
    return db.query(db_models.Brand).offset(skip).limit(limit).all()


def create_brand(db: Session, brand: schemas.BrandCreate):
    """Creates a new brand of coffee"""
    db_brand = db_models.Brand(name=brand.name, cost_per_cup=brand.cost_per_cup)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand
