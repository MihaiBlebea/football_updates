from tinydb import TinyDB, where
import pathlib

DB_TABLE = "live"
DB_FILE = f"{pathlib.Path(__file__).parent.resolve()}/../store/store.json"

def store_live_results(results: list):
	if len(results) == 0:
		return
	
	db = TinyDB(DB_FILE)
	table = db.table(DB_TABLE)
	for match in results:
		exists = table.search(where("teams") == match["teams"])

		if len(exists) > 0:
			db.update(match, where("teams") == match["teams"])

		table.insert(match)

def get_all_results() -> list:
	db = TinyDB(DB_FILE)
	table = db.table(DB_TABLE)

	return table.all()

def get_matches_by_league(league_name: str) -> list:
	db = TinyDB(DB_FILE)
	table = db.table(DB_TABLE)

	return table.search(where("league") == league_name)

def get_all_leagues() -> list:
	db = TinyDB(DB_FILE)
	table = db.table(DB_TABLE)

	results = {}

	matches = table.all()
	for match in matches:
		results[match["league"]] = True

	return results.keys()