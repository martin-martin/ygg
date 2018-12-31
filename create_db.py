import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec


Base = dec.declarative_base()


class File(Base):

    __tablename__ = "files"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    type = sa.Column(sa.String)
    name = sa.Column(sa.String)
    path = sa.Column(sa.String)
    revisits = sa.Column(sa.Integer, default=0)

    def __repr__(self):
        return "{0}: {1}".format(self.name, self.revisits)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = sa.create_engine('sqlite:///revisit.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
