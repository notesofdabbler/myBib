from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from makedb import Base, Articles

engine = create_engine('sqlite:///mybib.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

article1 = Articles(title = "An outer-approximation algorithm for a class of mixed-integer nonlinear programs",
                    authors = "Marco A. Duran; Ignacio E. Grossmann",
                    journal = "Mathematical Programming",
                    volume = 36,
                    pages = "307-339",
                    year = 1986)
session.add(article1)
session.commit()

article1 = Articles(title = "Retrospective on Optimization",
                    authors = "Lorenz T. Biegler; Ignacio E. Grossmann",
                    journal = "Computers and Chemical Engineering",
                    volume = 28,
                    pages = "1169-1192",
                    year = 2004)
session.add(article1)
session.commit()


