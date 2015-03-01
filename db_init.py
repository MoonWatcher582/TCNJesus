import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Rating(Base):
	__tablename__ = 'rating'
	name = Column(String(250), primary_key=True, nullable=False)
	food_average = Column(Integer, nullable=False)
	food_one = Column(Integer, nullable=False)
	food_two = Column(Integer, nullable=False)
	food_three = Column(Integer, nullable=False)
	food_four = Column(Integer, nullable=False)
	food_five = Column(Integer, nullable=False)
	shirt_average = Column(Integer, nullable=False)
	shirt_one = Column(Integer, nullable=False)
	shirt_two = Column(Integer, nullable=False)
	shirt_three = Column(Integer, nullable=False)
	shirt_four = Column(Integer, nullable=False)
	shirt_five = Column(Integer, nullable=False)
	total = Column(Integer, nullable=False)
	
	def __repr__(self):
		return "<Rating(name='%s', total='%d')>" % (self.name, self.total)

engine = create_engine('sqlite:///ratings.db')
Base.metadata.create_all(engine)
