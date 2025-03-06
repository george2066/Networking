run:
	uvicorn main:app --reload

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
