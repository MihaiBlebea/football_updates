venv-create:
	python3 -m venv virtualenv

venv-activate:
	. ./virtualenv/bin/activate

venv-lock:
	./virtualenv/bin/pip3 freeze > requirements.txt

venv-install-all:
	./virtualenv/bin/pip3 install -r requirements.txt

venv-install:
	./virtualenv/bin/pip3 install $(package)