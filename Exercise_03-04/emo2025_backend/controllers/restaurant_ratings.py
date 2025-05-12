from fastapi import APIRouter
from starlette.exceptions import HTTPException

from custom_exceptions.custom_not_found import CustomNotFound
from dtos.restaurant_rating import AddRatingReq
from services.restaurants_service import RestaurantService

router = APIRouter(tags=["restaurant_ratings"], prefix="/api/restaurants")


@router.get("/ratings")
async def get_restaurants_ratings(service: RestaurantService):
    """
    Get all the restaurants and their ratings

    :param service:
    :return:
    """
    return service.get_restaurants_ratings()

@router.get("/{resid}")
async def get_restaurant(resid: int, service: RestaurantService):

    """
    Get one restaurant by its primary key value
    :param resid:
    :param service:
    :return:
    """

    return service.get_restaurant(resid)


@router.get("/{resid}/ratings")
async def get_ratings_by_restaurant(resid: int, service: RestaurantService):
    """
    Get all individual ratings for a restaurant by its primary key value
    :param resid:
    :param service:
    :return:
    """

    return service.get_ratings_restaurant(resid)

@router.post("/{resid}/ratings")
async def add_rating_by_restaurant(resid: int, request_data: AddRatingReq, service: RestaurantService):
    """
    Add new rating for a restaurant by its primary key value
    :param resid:
    :param request_data:
    :param service:
    :return:
    """
    return service.add_new_rating(resid, request_data)

@router.delete("/{resid}/ratings/{rating_id}")
async def remove_rating(resid: int, rating_id:int , service: RestaurantService):
    """
    Delete a rating by its primary key value
    :param resid:
    :param rating_id:
    :param service:
    :return:
    """
    try:
        return service.remove_rating(rating_id)
    except CustomNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
