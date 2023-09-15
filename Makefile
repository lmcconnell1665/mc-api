# create a python virtual env
setup:
	python3 -m venv ~/.mc-api

# install the dependencies from requirements.txt
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	rm sql_app.db
	python -m pytest -vv

spinup:
	uvicorn main:app --reload

build:
	docker build -t mcapi .

run: 
	docker run -d --name mcapi -p 80:80 mcapi

stop:
	docker stop mcapi