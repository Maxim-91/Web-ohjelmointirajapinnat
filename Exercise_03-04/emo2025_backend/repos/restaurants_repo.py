from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

import models
from custom_exceptions.custom_not_found import CustomNotFound
from db import connect_to_db


class RestaurantRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_rating_by_id(self, rating_id):
        rating = self.db.query(models.Rating).filter(models.Rating.id == rating_id).first()
        if rating is None:
            raise CustomNotFound('Rating not found')
        return rating

    def remove_rating(self, _id):
        rating = self.get_rating_by_id(_id)
        self.db.delete(rating)
        self.db.commit()
        return None


    def add_rating(self, rating: models.Rating):
        self.db.add(rating)
        self.db.commit()


    def get_ratings(self):

        res = self.db.execute(text('SELECT re.id, name, cuisine, price_range, address, open_status, ROUND(AVG(ra.value), 1) AS rating, COUNT(ra.restaurant_id) AS review_count FROM restaurant AS re LEFT JOIN rating AS ra ON ra.restaurant_id = re.id GROUP BY re.id'))
        return res.mappings().all()

    def get_restaurant(self, _id):
        res = self.db.execute(text(
            'SELECT re.id, name, cuisine, price_range, address, open_status, ROUND(AVG(ra.value), 1) AS rating, COUNT(ra.restaurant_id) AS review_count FROM restaurant AS re LEFT JOIN rating AS ra ON ra.restaurant_id = re.id WHERE re.id = :reid GROUP BY re.id'), {'reid': _id})
        return res.mappings().first()

    def get_ratings_by_restaurant(self, _id):
        res = self.db.execute(text(
            'SELECT ra.id, user_id, value, description, date_rated FROM rating AS ra  WHERE restaurant_id = :reid'), {'reid': _id})
        return res.mappings().all()




def init_restaurant_repo(db: Session = Depends(connect_to_db)):
    return RestaurantRepo(db)
