import code
from pathlib import Path


DOC_DIR = Path('/Users/martin/Documents/personal')  # remove /personal for production
# selection of file types to add to revisit db
f_types = (".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".csv", ".ppt", ".jpg", ".png")
# fetches the absolute paths of files with specified extensions, to later save into db
all_files = [f for f in sorted(DOC_DIR.rglob('*')) if f.suffix.lower() in f_types and not f.stem.startswith("~")]


code.interact(local=locals())
