"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""
from sqlalchemy import create_engine, and_, or_

from sqlalchemy.orm import sessionmaker

from model import *

DB_URI = 'sqlite:///auto.db'

engine = create_engine(DB_URI, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
# init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
q1 = session.query(Brand).get(8)

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
q2 = session.query(Model).filter_by(name = 'Corvette', brand_name = 'Chevrolet')

# # Get all models that are older than 1960.
q3 = session.query(Model).filter(Model.year < 1960).all()

# # Get all brands that were founded after 1920.
q4 = session.query(Brand).filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
q5 = session.query(Model).filter(Model.name.like('Cor%')).all()

# # Get all brands with that were founded in 1903 and that are not yet discontinued.
q6 = session.query(Brand).filter(and_(Brand.discontinued.is_(None), Brand.founded == '1903')).all()

# # Get all brands with that are either discontinued or founded before 1950.
q7 = session.query(Brand).filter(or_(Brand.discontinued != None, Brand.founded < 1950)).all()

# # Get any model whose brand_name is not Chevrolet.
q8 = session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    joined_model_brand = session.query(Model, Brand).join(Brand).filter(Model.year == year).all()

    for car_model, car_brand in joined_model_brand:
    	print car_model.name + " " + car_model.brand_name + " " + car_brand.headquarters
    	
get_model_info(1960)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_names = session.query(Brand, Model).join(Model).all()

    for car_brand, car_model in brand_names:
    	print car_brand.name + " " + car_model.name

get_brands_summary()


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
