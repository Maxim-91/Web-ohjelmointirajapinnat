from typing import List, Optional

from sqlalchemy import Column, DateTime, Float, ForeignKeyConstraint, Index, String, Text, LargeBinary
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(255), nullable=False)
    cuisine = mapped_column(String(45), nullable=False)
    price_range = mapped_column(String(45), nullable=False)
    address = mapped_column(String(255), nullable=False)
    open_status = mapped_column(String(45), nullable=False)

    rating: Mapped[List['Rating']] = relationship('Rating', uselist=True, back_populates='restaurant')


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('username_UNIQUE', 'username', unique=True),
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    username = mapped_column(String(255), nullable=False)
    password = mapped_column(LargeBinary, nullable=False)
    role = mapped_column(String(45), nullable=False)

    rating: Mapped[List['Rating']] = relationship('Rating', uselist=True, back_populates='user')


class Rating(Base):
    __tablename__ = 'rating'
    __table_args__ = (
        ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], name='fk_rating_restaurant1'),
        ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_rating_user'),
        Index('fk_rating_restaurant1_idx', 'restaurant_id'),
        Index('fk_rating_user_idx', 'user_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    value = mapped_column(Float, nullable=False)
    date_rated = mapped_column(DateTime, nullable=False)
    restaurant_id = mapped_column(INTEGER(11), nullable=False)
    description = mapped_column(Text)
    user_id = mapped_column(INTEGER(11))

    restaurant: Mapped['Restaurant'] = relationship('Restaurant', back_populates='rating')
    user: Mapped[Optional['User']] = relationship('User', back_populates='rating')

