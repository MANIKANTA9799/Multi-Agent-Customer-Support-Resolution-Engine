"""Concept: The Declarative Base and Data Models.
Why it exists: We wrote raw SQL
 earlier to understand the schema, 
 but in the app, we want to interact 
 with database rows as Python objects
 . SQLAlchemy maps Python 
classes to database tables."""

"""This is a very important SQLAlchemy concept. Base is the foundation that tells SQLAlchemy:
"The classes that inherit from me are database models, and SQLAlchemy should track their table definitions."""



from sqlalchemy.orm import declarative_base
Base = declarative_base()