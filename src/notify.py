from notifypy import Notify
import pathlib
import requests

FOLDER_PATH = pathlib.Path(__file__).parent.resolve()

AUDIO_FILE = f"{FOLDER_PATH}/../assets/alarm.wav"
ICON_FILE = f"{FOLDER_PATH}/../assets/icon.png"

def trigger_desktop_notification(title: str, body: str):
	notification = Notify()
	notification.title = title
	notification.message = body
	notification.application_name = "Football updates"
	notification.audio = AUDIO_FILE
	notification.icon = ICON_FILE
	notification.send()

def trigger_telegram_notification(body: str, chat_id: str, bot_token: str):
	data = {"chat_id": chat_id, "text": body, "parse_mode": "HTML"}
	url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
	response = requests.post(url, data=data)

	return response.json()

if __name__ == "__main__":
	trigger_desktop_notification("demo title", "demo body")