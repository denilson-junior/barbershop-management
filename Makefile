DJANGO=py manage.py

run:
	$(DJANGO) runserver

make:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

fmt:
	black .

db.up:
	docker-compose up -d

db.down:
	docker stop barbershop-management-db