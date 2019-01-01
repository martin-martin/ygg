import os
import code
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from create_db import Base, File
# keeps track of which round of revisits you're on
from settings import REVISIT_ROUND


engine = sa.create_engine('sqlite:///revisit.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# increments after the first round of revisits is done, to step you into the next round
# TODO: move this logic into a separate CRON job that checks only every once in a while to improve performance
# TODO: potentially move ino a separate Stats table
if session.query(File).filter_by(revisits=REVISIT_ROUND).count() == 0:
    REVISIT_ROUND += 1
    with open('settings.py', 'w') as f:
        f.write('REVISIT_ROUND = {0}'.format(REVISIT_ROUND))

check = session.query(File).filter_by(revisits=REVISIT_ROUND).order_by(func.random()).first()
# note that we revisited this file, and when
check.last_revisit = datetime.datetime.now()
check.revisits += 1
session.commit()  # save changes to db

# open up the current file to revisit in suitable program
os.system('open {0}'.format(check.path))

code.interact(local=locals())