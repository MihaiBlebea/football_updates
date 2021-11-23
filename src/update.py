from store import store_live_results, get_all_results
from scrape import scrape
from notify import trigger


class LiveScoreUpdater():

	def __init__(self):
		self.updates = {}

	def update(self):
		# get the new results from the scraper
		new_updates = scrape()

		# get all old scores frm the database
		for match in get_all_results():
			key = f"{match['teams'][0]} - {match['teams'][1]}"
			self.updates[key] = {}
			self.updates[key]["old"] = match

		for match in new_updates:
			key = f"{match['teams'][0]} - {match['teams'][1]}"
			if key not in self.updates:
				self.updates[key] = {}
			self.updates[key]["new"] = match

		for (key, match) in self.updates.items():

			if "old" not in match:
				continue
			
			# compare the score
			self.__did_home_score(match)

			self.__did_away_score(match)

			self.__is_half_time(match)

			self.__is_full_time(match)

		store_live_results(new_updates)


	def __did_home_score(self, match: dict):
		old_home_score = match["old"]["score"][0]
		new_home_score = match["new"]["score"][0]

		away_score = match['new']['score'][1]

		home_team_name = match['old']['teams'][0]
		away_team_name = match['old']['teams'][1]

		if old_home_score != new_home_score:
			trigger(
				f"Score update {home_team_name} - {away_team_name}",
				f"{home_team_name} scored for {new_home_score} - {away_score}"
			)
	
	def __did_away_score(self, match: dict):
		old_away_score = match["old"]["score"][1]
		new_away_score = match["new"]["score"][1]

		home_score = match['new']['score'][0]

		home_team_name = match['old']['teams'][0]
		away_team_name = match['old']['teams'][1]

		if old_away_score != new_away_score:
			trigger(
				f"Score update {home_team_name} - {away_team_name}",
				f"{away_team_name} scored for {home_score} - {new_away_score}"
			)

	def __is_half_time(self, match: dict):
		old_status = match["old"]["status"]
		new_status = match["new"]["status"]

		home_team = match['old']['teams'][0]
		awayt_team = match['old']['teams'][1]

		home_score = match['new']['score'][0]
		away_score = match['new']['score'][1]

		if old_status != "HT" and new_status == "HT":
			trigger(
				f"Half time in {home_team} - {awayt_team}",
				f"Score is {home_score} - {away_score}"
			)

	def __is_full_time(self, match: dict):
		old_status = match["old"]["status"]
		new_status = match["new"]["status"]

		home_team = match['old']['teams'][0]
		awayt_team = match['old']['teams'][1]

		home_score = match['new']['score'][0]
		away_score = match['new']['score'][1]

		if old_status != "FT" and new_status == "FT":
			trigger(
				f"Full time in {home_team} - {awayt_team}",
				f"Score is {home_score} - {away_score}"
			)

if __name__ == "__main__":
	updater = LiveScoreUpdater()
	updater.update()
