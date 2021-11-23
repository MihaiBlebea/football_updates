from notifypy import Notify
import pathlib

FOLDER_PATH = pathlib.Path(__file__).parent.resolve()

AUDIO_FILE = f"{FOLDER_PATH}/../assets/alarm.wav"
ICON_FILE = f"{FOLDER_PATH}/../assets/icon.png"

def trigger(title: str, body: str):
	notification = Notify()
	notification.title = title
	notification.message = body
	notification.application_name = "Football updates"
	notification.audio = AUDIO_FILE
	notification.icon = ICON_FILE
	notification.send()

if __name__ == "__main__":
	trigger("demo title", "demo body")