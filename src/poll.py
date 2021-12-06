import requests
from notify import trigger
from logs import logging
import json
from dotenv import dotenv_values
from typing import Callable

BASE_URL = "https://dev-rapidapi-football-scores.cap-rover.purpletreetech.com"

def main():
	logging.info("Starting the script")
	[send_notification(match) for match in match_generator(get_matches)]

def get_auth() -> tuple:
	config = dotenv_values(".env")
	return (config["USERNAME"], config["PASSWORD"])

def get_headers() -> dict:
	return {
		"X-RapidAPI-Proxy-Secret": "abcd"
	}

def get_matches() -> list:
	url = f"{BASE_URL}/matches/updates"
	res = requests.get(url,  headers=get_headers(), auth=get_auth())
	if res.status_code != 200:
		logging.error(f"Request failed, status code {res.status_code}")
		return []

	body = res.json()
	logging.info("Received the update from server " + json.dumps(body))

	if "data" not in body:
		logging.error(f"Key data not found in response body")
		return []

	return body["data"]

def match_generator(source: Callable) -> dict:
	for match in source():
		yield {
			"home_team": match["teams"][0],
			"away_team": match["teams"][1],
			"home_score": match["score"][0],
			"away_score": match["score"][1]
		}

def send_notification(data: dict):
	home_team = data["home_team"]
	away_team = data["away_team"]
	home_score = data["home_score"]
	away_score = data["away_score"]
	logging.info(f"Found match update {home_team} {home_score}-{away_score} {away_team}")
	trigger(
		f"Update {home_team} - {away_team}",
		f"{home_team} {home_score}-{away_score} {away_team}"
	)

if __name__ == "__main__":
	main()