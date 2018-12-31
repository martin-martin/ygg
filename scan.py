import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from create_db import Base, File
from pathlib import Path


# PART 1 - Getting the info of the desired files
DOC_DIR = Path('/Users/martin/Documents/personal')  # remove /personal for production
# selection of file types to add to revisit db
f_types = (".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".csv", ".ppt", ".jpg", ".png")
# fetches the absolute paths of files with specified extensions, to later save into db
all_files = [f for f in sorted(DOC_DIR.rglob('*')) if f.suffix.lower() in f_types and not f.stem.startswith("~")]

# PART 2 - Putting the file info into our database
engine = sa.create_engine('sqlite:///revisit.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert File objects in the files table
for f in all_files:
    new_file = File(type=f.suffix[1:], name=f.stem, path=str(f))  # auto id and revisits
    session.add(new_file)
    session.commit()
