from datetime import datetime
from typing import Annotated

from fastapi import Depends

import models
from repos.restaurants_repo import RestaurantRepo, init_restaurant_repo


class ResServ:
    def __init__(self, repo: RestaurantRepo):
        self.repo = repo

    def get_restaurants_ratings(self):
        return self.repo.get_ratings()

    def get_restaurant(self, _id):
        return self.repo.get_restaurant(_id)

    def add_new_rating(self, resid, request_data):


        rating = models.Rating(value=request_data.rating, date_rated=datetime.now(), restaurant_id=resid,
                               description=request_data.comment)

        self.repo.add_rating(rating)

        return rating


    def remove_rating(self, rating_id):
        self.repo.remove_rating(rating_id)

        return None


    def get_ratings_restaurant(self, _id):
        return self.repo.get_ratings_by_restaurant(_id)


def init_restaurants_service(repo: RestaurantRepo = Depends(init_restaurant_repo)):
    return ResServ(repo)


RestaurantService = Annotated[ResServ, Depends(init_restaurants_service)]
