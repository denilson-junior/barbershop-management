DJANGO=python manage.py

run:
	$(DJANGO) runserver

make:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

test:
	$(DJANGO) test

shell:
	$(DJANGO) shell

fmt:
	black .
	ruff check

db.up:
	sudo docker-compose up -d

db.down:
	sudo docker stop barbershop-management-db