DJANGO=python manage.py

run:
	$(DJANGO) runserver

make:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

test:
	$(DJANGO) test

fmt:
	black .

db.up:
	docker-compose up -d

db.down:
	docker stop barbershop-management-db