run:
	uvicorn main:app --reload

docker-status:
	sudo systemctl status docker

docker-start:
	sudo systemctl start docker

docker-stop:
	sudo systemctl stop docker

pg-service-status:
	sudo systemctl status postgresql.service

pg-service-start:
	sudo systemctl start postgresql.service

pg-service-stop:
	sudo systemctl stop postgresql.service

pg-up:
	sudo docker-compose -f docker_compose_dev.yaml --env-file .env.dev.pg up -d

pg-down:
	sudo docker-compose -f docker_compose_dev.yaml --env-file .env.dev.pg down && sudo docker network prune --force

al-in:
	alembic init migrations

al-mm:
	alembic revision --autogenerate -m $(c)

al-uh:
	alembic upgrade heads
