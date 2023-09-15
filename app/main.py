"""
mc-api
"""

from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud, app.db_models as db_models, app.schemas as schemas
from app.database import SessionLocal, engine

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """Confirms the database connection is open and closes it when the request is complete"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/coffee/brand", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    """Creates a new brand of coffee"""
    db_brand = crud.get_brand_by_name(db, brand_name=brand.name)
    if db_brand:
        raise HTTPException(status_code=400, detail="Brand already exists")
    return crud.create_brand(db=db, brand=brand)


@app.get("/coffee/brand", response_model=list[schemas.Brand])
def read_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Returns a list of brands of coffee"""
    brands = crud.get_brands(db, skip=skip, limit=limit)
    return brands


@app.get("/coffee/brand/{brand_id}", response_model=schemas.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    """Returns a specific brand of coffee based on the id in the path"""
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


@app.post("/coffee/adjust_inventory")
async def adjust_inventory(brand_id:  Annotated[int, Body()], inventory_adjustment:  Annotated[int, Body()]):
    """Adjusts the inventory for the specified brand of coffee"""
    return HTTPException(status_code=501, detail="Not implemented")