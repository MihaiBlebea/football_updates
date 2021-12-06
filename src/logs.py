import logging
from pathlib import Path

logging.basicConfig(
	filename=f"{Path(__file__).parent.resolve()}/../application.log", 
	encoding="utf-8", 
	level=logging.DEBUG,
	datefmt="%m/%d/%Y %I:%M:%S %p",
	format="%(levelname)s %(asctime)s - %(message)s"
)