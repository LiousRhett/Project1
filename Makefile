.PHONY: sync run build up down clean

sync:
	uv sync

run:
	gunicorn -w 4 -b 0.0.0.0:8000 app:create_app

build:
	docker build . $(if $(TAG),-t whatsapp-bot:$(TAG),-t whatsapp-bot:latest) 

up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down
	docker rmi whatsapp-bot:latest