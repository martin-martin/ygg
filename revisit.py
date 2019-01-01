import os
#import code
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from create_db import Base, File


# set here which round of revisits you're on
REVISITS = 0

engine = sa.create_engine('sqlite:///revisit.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# increments after the first round of revisits is done, to step you into the next round
if session.query(File).filter_by(revisits=REVISITS).count() == 0:
    REVISITS += 1

check = session.query(File).filter_by(revisits=REVISITS).order_by(func.random()).first()
# note that we revisited this file, and when
check.last_revisit = datetime.datetime.now()
check.revisits += 1
session.commit()  # save changes to db

# open up the current file to revisit in suitable program
os.system('open {0}'.format(check.path))

#code.interact(local=locals())