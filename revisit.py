import os
#import code
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from create_db import Base, File


engine = sa.create_engine('sqlite:///revisit.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


check = session.query(File).filter_by(revisits=0).order_by(func.random()).first()
# note that we revisited this file, and when
check.last_revisit = datetime.datetime.now()
check.revisits += 1
session.commit()  # save changes to db

# open up the current file to revisit in suitable program
os.system('open {0}'.format(check.path))

#code.interact(local=locals())