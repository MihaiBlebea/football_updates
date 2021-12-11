from pathlib import Path
from datetime import datetime

FOLDER_PATH = Path(__file__).parent.resolve()
FILE_PATH = f"{FOLDER_PATH}/../last_update.txt"

def store_last_update(last_update: str = None):
	if last_update is None:
		last_update = get_current_timestamp()
	f = open(FILE_PATH, "w")
	f.write(last_update)
	f.close()

def get_last_update():
	if Path(FILE_PATH).is_file() == False:
		return get_current_timestamp()

	f = open(FILE_PATH, "r")
	return f.read().strip()

def get_current_timestamp():
	return str(int(datetime.now().timestamp()))