from pydantic import BaseModel


class BrandBase(BaseModel):
    """Base model for brand data"""
    name: str
    cost_per_cup: float


class BrandCreate(BrandBase):
    """Model for creating a new brand of coffee"""
    pass  # pylint: disable=unnecessary-pass


class Brand(BrandBase):
    """Model for brand data with id"""
    id: int

    class Config:
        """Configures the ORM mode"""
        orm_mode = True


class InventoryAdjustment(BaseModel):
    """Model for inventory adjustment data"""
    brand_id: int
    inventory_adjustment: int
