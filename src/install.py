from crontab import CronTab
import getpass
import pathlib
import argparse

COMMENT = "will run the football updates scraper"

def main(cron):
	iter = cron.find_comment(COMMENT)
	for job in iter:
		if job.comment == COMMENT:
			remove(cron)

	install(cron)


def install(cron):
	path = pathlib.Path(__file__).parent.resolve()
	print(path)
	job = cron.new(
		command=f"{path}/../virtualenv/bin/python3 {path}/poll.py >> {path}/../cron.log 2>&1",
		comment=COMMENT
	)
	job.minute.every(5)
	cron.write()

def remove(cron):
	cron.remove_all(comment=COMMENT)
	cron.write()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog= "installer", 
		usage="%(prog)s [options]", 
		description="install the application",
	)

	parser.add_argument(
		"-u",
		"--uninstall",
		dest="uninstall",
		required=False, 
		default=False,
		action="store_true",
		help="uninstall the application",
	)

	args = parser.parse_args()

	cron = CronTab(user=getpass.getuser())
	if args.uninstall:
		remove(cron)
	else:
		main(cron)