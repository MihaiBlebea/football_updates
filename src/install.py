from crontab import CronTab
import getpass
import pathlib

COMMENT = "will run the football updates scraper"

def main():
	cron = CronTab(user=getpass.getuser())
	iter = cron.find_comment(COMMENT)
	for job in iter:
		if job.comment == COMMENT:
			remove(cron)

	# install(cron)


def install(cron):
	path = pathlib.Path(__file__).parent.resolve()
	print(path)
	job = cron.new(
		command=f"{path}/../virtualenv/bin/python3 {path}/update.py >> {path}/../cron.log 2>&1",
		comment=COMMENT
	)
	job.minute.every(1)
	cron.write()

def remove(cron):
	cron.remove_all(comment=COMMENT)
	cron.write()

if __name__ == "__main__":
	main()