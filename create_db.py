import datetime
import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec


Base = dec.declarative_base()


class File(Base):

    __tablename__ = "files"

    # use BigInteger for Postgres, but doesn't work for SQLite
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    type = sa.Column(sa.String, nullable=True, index=True)
    name = sa.Column(sa.String, nullable=True)
    path = sa.Column(sa.String, nullable=False, unique=True)
    # default is my birthday :)
    last_revisit = sa.Column(sa.DateTime, nullable=True, default=datetime.datetime(1987, 1, 15), index=True)
    revisits = sa.Column(sa.Integer, default=0, index=True)

    def __repr__(self):
        return "{0}: {1}".format(self.revisits, self.name)


# Create an engine that stores data in the local directory's .db file.
engine = sa.create_engine('sqlite:///revisit.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
