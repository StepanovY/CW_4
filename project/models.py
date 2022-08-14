from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))

    favourite_genre = Column(Integer, ForeignKey(Genre.id))
    genre = relationship("Genre")


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey(Director.id), nullable=False)
    director = relationship("Director")
