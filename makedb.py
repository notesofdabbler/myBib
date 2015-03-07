# adapted from http://github.com/lobrown

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    authors = Column(String)
    journal = Column(String)
    volume = Column(String)
    year = Column(Integer)
    pages = Column(String)
    weburl = Column(String)
    localurl = Column(String)
    keywords = Column(String)

engine = create_engine('sqlite:///mybib.db')

Base.metadata.create_all(engine)
