#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
firebat-web.database
~~~~~~~~~~~~~~~~~~~~

Describes engine and connection.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from .__init__ import app

engine = create_engine('postgresql://',
#engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'),
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import fireweb.example.models
    Base.metadata.create_all(bind=engine)
