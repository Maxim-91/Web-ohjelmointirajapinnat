from typing import Optional

from pydantic import BaseModel


class RestaurantRating(BaseModel):
    name:str
    cuisine:str
    price_range:str
    address:str
    open_status: str
    avg_rating:float
    rating_count:int


class AddRatingReq(BaseModel):
    rating: Optional[float] = 0
    comment: Optional[str] = None