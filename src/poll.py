import requests
from notify import trigger_desktop_notification, trigger_telegram_notification
from logs import logging
import json
from dotenv import dotenv_values
from typing import Callable
from pathlib import Path

from last_update import get_last_update, store_last_update


BASE_URL = "https://dev-rapidapi-football-scores.cap-rover.purpletreetech.com"

config = dotenv_values(f"{Path(__file__).parent.resolve()}/../.env")

def main():
	logging.info("Starting the script")
	[send_notification(match) for match in match_generator(get_matches)]

def get_auth() -> tuple:
	return (config["USERNAME"], config["PASSWORD"])

def get_headers() -> dict:
	return {
		"X-RapidAPI-Proxy-Secret": config["RAPIDAPI_PROXY_SECRET"]
	}

def get_matches() -> list:
	last_update_ts = get_last_update()

	url = f"{BASE_URL}/matches/updates?last_update={last_update_ts}"
	res = requests.get(url, headers=get_headers(), auth=get_auth())
	logging.info(f"Made request to url {url}")

	if res.status_code != 200:
		logging.error(f"Request failed, status code {res.status_code}")
		return []

	body = res.json()
	logging.info("Received the update from server " + json.dumps(body))

	if "data" not in body:
		logging.error(f"Key data not found in response body")
		return []

	if "last_update_timestamp" not in body:
		store_last_update()
	else:
		store_last_update(body["last_update_timestamp"])

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
	title = f"Update {home_team} - {away_team}"
	body = f"{home_team} {home_score}-{away_score} {away_team}"
	
	trigger_desktop_notification(title, body)

	trigger_telegram_notification(
		body, 
		config["TELEGRAM_CHAT_ID"], 
		config["TELEGRAM_BOT_TOKEN"]
	)

if __name__ == "__main__":
	main()